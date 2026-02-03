# Quick Start Guide

## Getting Started in 3 Steps

### 1. Setup Database
```bash
cd finance_portfolio
python3 manage.py makemigrations
python3 manage.py migrate
```

### 2. Create Admin Account
```bash
python3 manage.py createsuperuser
```
Enter username, email, and password when prompted.

### 3. Run the Application
```bash
python3 manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

## First Login

1. Click "Sign up" to create your account
2. Fill in your details
3. Login with your credentials
4. Start tracking your finances!

## Key Features at a Glance

### Dashboard
- View your total balance
- See monthly income and expenses
- Track budget progress
- View recent transactions

### Transactions
- Add income and expenses
- Filter by type and category
- Search transactions
- Edit or delete entries

### Watchlist
- Track investment opportunities
- Set Buy/Hold/Sell status
- Monitor gains and losses
- Store research notes

### Budget
- Set monthly spending limits
- Get visual progress indicators
- Receive alerts when approaching limit

## Admin Panel

Access advanced features at: **http://127.0.0.1:8000/admin/**

Use the superuser credentials you created.

## Sample Data

Try adding:
- **Income**: Salary, Freelance, Investment returns
- **Expenses**: Groceries, Rent, Transportation
- **Investments**: AAPL, MSFT, BTC, GOOGL

## Need Help?

Check the full README.md for detailed documentation.
