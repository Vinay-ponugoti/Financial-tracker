## 🏃‍♂️ Quick Start

### Local Setup
1. **Clone**:
   ```bash
  :- git clone https://github.com/Vinay-ponugoti/finance-tracker.git
     cd finance-tracker

  :- pip install -r requirements.txt

  :- python app.py

🌐 API Endpoints
POST /add_transaction: curl -X POST -d '{"amount": -50, "description": "Lunch"}' -H "Content-Type: application/json" http://localhost:5000/add_transaction
GET /get_balance: Fetch balance.
GET /get_transactions: List with ?category=Food option.
DELETE /delete_transaction/<id>: Remove entry.
GET /predict_expenses: Expense forecast.

🤖 AI Features
Smart Categorization: Keyword-based (scalable to NLP).
Expense Prediction: Linear regression.
Anomaly Detection: Mean ± 2 std dev.

Author
Name: Vinay Ponugoti
GitHub: github.com/Vinay-ponugoti
LinkedIn: linkedin.com/in/vinay-ponugoti 
Email: ponugotiviany.v@gmail.com
