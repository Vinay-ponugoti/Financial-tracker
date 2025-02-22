# Personal Finance Tracker API

A RESTful web app for managing personal finances with AI-driven features like smart categorization, expense prediction, and anomaly detection. Built with Flask and deployed on **Render**’s free tier, this project showcases Python, APIs, and AI skills.

## 🚀 Live Demo
- **URL**: [https://financial-tracker-kcl5.onrender.com]
- Add transactions, filter categories, and explore AI insights!

## ✨ Features
- **Transaction Management**: Add, view, delete income/expenses.
- **Real-Time Balance**: Instant updates.
- **Transaction History**: Filterable table with anomaly highlighting.
- **AI-Powered**:
  - *Smart Categorization*: Auto-suggests categories (e.g., "Lunch" → "Food").
  - *Expense Prediction*: Forecasts expenses with linear regression.
  - *Anomaly Detection*: Flags outliers statistically.

## 🛠️ Tech Stack
- **Backend**: Python 3.10, Flask 2.3.2
- **Database**: SQLite
- **AI/ML**: Scikit-learn, NumPy, Regex
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render (free tier)
- **Tools**: Git, GitHub
## 🏃‍♂️ Quick Start

### Local Setup
1. **Clone**:
   ```bash
   git clone https://github.com/Vinay-ponugoti/finance-tracker.git
   cd finance-tracker

   pip install -r requirements.txt

   python app.py

## 🌐 API Endpoints
- POST /add_transaction: curl -X POST -d '{"amount": -50, "description": "Lunch"}' -H "Content-Type: application/json" http://localhost:5000/add_transaction
-  GET /get_balance: Fetch balance.
-  GET /get_transactions: List with ?category=Food option.
-  DELETE /delete_transaction/<id>: Remove entry.
-  GET /predict_expenses: Expense forecast.

## 🤖 AI Features
 - Smart Categorization: Keyword-based (scalable to NLP).
 - Expense Prediction: Linear regression.
 - Anomaly Detection: Mean ± 2 std dev.

## Author
- Name: Vinay Ponugoti
- GitHub: github.com/Vinay-ponugoti
- LinkedIn: linkedin.com/in/vinay-ponugoti 
- Email: ponugotivinay.v@gmail.com
