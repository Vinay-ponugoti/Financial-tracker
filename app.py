# app.py
from flask import Flask, request, jsonify, render_template
import os
import re
import numpy as np
from sklearn.linear_model import LinearRegression
from db.database import Database

app = Flask(__name__)
db = Database()

# AI: Predefined keyword-to-category mapping (expandable for future NLP)
CATEGORY_KEYWORDS = {
    "Food": ["lunch", "dinner", "restaurant", "coffee", "groceries"],
    "Transport": ["uber", "lyft", "gas", "bus", "train"],
    "Entertainment": ["movie", "game", "concert"],
    "Salary": ["payday", "wage", "income"],
    "Other": []  # Default
}

def predict_category(description):
    """Predicts a category based on description (future: trainable NLP model)."""
    description = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(re.search(rf"\b{keyword}\b", description) for keyword in keywords):
            return category
    return "Other"

# API Endpoints
@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    """Add a new transaction with AI-suggested category."""
    data = request.get_json()
    amount = data["amount"]
    category = data.get("category") or predict_category(data["description"])
    description = data["description"]
    db.add_transaction(amount, category, description)
    return jsonify({"message": "Transaction added successfully", "category": category}), 201

@app.route("/get_balance", methods=["GET"])
def get_balance():
    """Get the total balance."""
    balance = db.get_balance()
    return jsonify({"balance": balance})

@app.route("/get_transactions", methods=["GET"])
def get_transactions():
    """Get all transactions with anomaly detection."""
    category = request.args.get("category")
    transactions = db.get_transactions(category)

    # AI: Anomaly detection (mean ± 2 std dev)
    amounts = [t[0] for t in transactions]
    is_anomaly = lambda amt: False  # Default for no data
    if amounts:
        mean = np.mean(amounts)
        std = np.std(amounts)
        lower_bound, upper_bound = mean - 2 * std, mean + 2 * std
        is_anomaly = lambda amt: bool(amt < lower_bound or amt > upper_bound)  # Convert np.bool_ to Python bool

    transaction_list = [
        {"amount": t[0], "category": t[1], "date": t[2], "description": t[3], "id": t[4], 
         "is_anomaly": is_anomaly(t[0])}
        for t in transactions
    ]
    return jsonify({"transactions": transaction_list})

@app.route("/delete_transaction/<int:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    """Delete a transaction by ID."""
    db.delete_transaction(transaction_id)
    return jsonify({"message": "Transaction deleted successfully"}), 200

@app.route("/predict_expenses", methods=["GET"])
def predict_expenses():
    """AI: Predict next month's expenses using linear regression."""
    monthly_data = db.get_monthly_expenses()
    if len(monthly_data) < 2:
        return jsonify({"prediction": "Insufficient data for prediction"})

    X = np.array(range(len(monthly_data))).reshape(-1, 1)  # Month index
    y = np.array([float(row[1]) for row in monthly_data])   # Expenses
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict(np.array([[len(monthly_data)]]))[0]
    return jsonify({"prediction": round(prediction, 2)})

@app.route("/")
def index():
    """Serve the frontend."""
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)