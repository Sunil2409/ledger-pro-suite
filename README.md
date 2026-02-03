# Personal Finance & Investment Portfolio Manager

A comprehensive Django 5.x web application for managing personal finances and investment portfolios. Built with a professional FinTech design inspired by Bloomberg and TCS BaNCS.

## 📱 NEW: Fully Mobile-Responsive!

✨ **Works perfectly on ALL devices** - Phone, Tablet, Desktop!

- ✅ **Responsive hamburger menu** on mobile
- ✅ **Touch-optimized interface** for easy tapping
- ✅ **Adaptive layouts** for all screen sizes
- ✅ **Same features** on mobile & desktop
- ✅ **Swipeable tables** for data viewing

👉 **See [MOBILE_RESPONSIVE.md](MOBILE_RESPONSIVE.md)** for complete mobile features guide

---

## 🆓 Deploy FREE in 10 Minutes!

Deploy this app **completely free** (no credit card needed):

👉 **[RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)** - Simple 7-step guide

**Or see detailed options:**
- 📘 [FREE_DEPLOYMENT.md](FREE_DEPLOYMENT.md) - All free platforms compared
- 🚂 [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md) - Railway guide ($5/month credit)
- ⚡ [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md) - Vercel setup (not recommended)
- 📊 [DEPLOYMENT_OPTIONS.md](DEPLOYMENT_OPTIONS.md) - Complete comparison

---

## 🎯 Features

### 💰 Expense Tracker
- **CRUD Operations**: Add, view, edit, and delete financial transactions
- **Transaction Types**: Income and Expense tracking
- **Categories**: Food, Transportation, Shopping, Entertainment, Bills, Healthcare, Education, Investment, Salary, and more
- **Django Forms**: Comprehensive validation for data integrity
- **Search & Filter**: Filter by type, category, and search by description

### 📊 Financial Summary
- **Real-time Balance**: Automatic calculation of total balance (Income - Expenses)
- **Monthly Budget Tracking**: Set spending limits and monitor usage
- **Budget Progress Bar**: Visual representation of spending vs. budget
- **Category-wise Analysis**: See spending breakdown by category
- **Custom Template Tags**: Calculate totals, percentages, and budget status
- **Django Signals**: Automatic balance updates on transaction changes

### 📈 BFSI Watchlist
- **Investment Tracking**: Monitor stocks, ETFs, cryptocurrencies, mutual funds, and bonds
- **Status Badges**: Buy/Hold/Sell indicators with color coding
- **Position Tracking**: Record quantity owned and purchase prices
- **Gain/Loss Calculation**: Automatic calculation of unrealized gains/losses
- **Portfolio Statistics**: Total value, cost basis, and overall performance
- **Research Notes**: Store investment thesis and analysis

### 🔐 Authentication & Security
- **Django Built-in Auth**: Secure user authentication system
- **User Registration**: Sign up with email validation
- **Login/Logout**: Protected routes with LoginRequiredMixin
- **Private Data**: Each user sees only their own transactions and watchlist
- **User Profiles**: Automatic profile creation with Django signals

## 🏗️ Technical Architecture

### Backend
- **Framework**: Django 5.x
- **Views**: Class-Based Views (CBVs) for clean, maintainable code
  - ListView, CreateView, UpdateView, DeleteView, DetailView
  - LoginRequiredMixin for authentication
- **Database**: SQLite (development)
- **ORM**: Django Models with relationships and indexes
- **Signals**: Real-time balance updates on transaction changes

### Frontend
- **Templates**: Django Template System with inheritance
- **Base Template**: Professional sidebar layout
- **Styling**: Tailwind CSS via CDN
- **Design**: Bloomberg/TCS BaNCS inspired FinTech aesthetic
  - Dark theme with high contrast
  - Professional color scheme
  - Responsive design
  - Smooth transitions and hover effects

### Models
1. **Transaction**: Expense and income tracking
   - User (ForeignKey)
   - Type (Expense/Income)
   - Category
   - Amount
   - Date
   - Description

2. **UserProfile**: Extended user information
   - User (OneToOne)
   - Total Balance
   - Monthly Budget
   - Auto-created via signals

3. **Watchlist**: Investment tracking
   - User (ForeignKey)
   - Symbol
   - Asset Type
   - Status (Buy/Hold/Sell)
   - Prices and quantities
   - Gain/loss calculations

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Step 1: Install Dependencies
```bash
pip install Django==5.1
```

### Step 2: Database Setup
```bash
cd finance_portfolio
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 4: Run Development Server
```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

## 🚀 Usage Guide

### First Time Setup
1. Navigate to http://127.0.0.1:8000/
2. Click "Sign up" to create an account
3. Fill in your details and submit
4. Login with your credentials

### Managing Transactions
1. From the dashboard, click "Add New Transaction" or navigate to Transactions
2. Select transaction type (Income/Expense)
3. Choose a category
4. Enter amount and date
5. Add optional description
6. Submit to save (balance updates automatically!)

### Setting Budget
1. Navigate to "Budget Settings" from the sidebar
2. Enter your monthly spending limit
3. Track progress on the dashboard

### Managing Watchlist
1. Navigate to "Watchlist" from the sidebar
2. Click "Add to Watchlist"
3. Enter stock symbol (e.g., AAPL, MSFT)
4. Set status (Buy/Hold/Sell)
5. Optionally add position details if you own the asset
6. View portfolio statistics and gain/loss calculations

### Admin Panel
Access Django admin at: http://127.0.0.1:8000/admin/
- Manage users
- View all transactions
- Edit watchlist items
- Configure system settings

## 📁 Project Structure

```
finance_portfolio/
├── manage.py
├── finance_portfolio/           # Main project folder
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── transactions/               # Expense tracker app
│   ├── models.py              # Transaction & UserProfile models
│   ├── views.py               # CBVs for transactions
│   ├── forms.py               # Django Forms with validation
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App configuration
│   └── templatetags/          # Custom template tags
│       └── finance_tags.py    # Financial calculations
├── watchlist/                  # Investment tracker app
│   ├── models.py              # Watchlist model
│   ├── views.py               # CBVs for watchlist
│   ├── forms.py               # Watchlist forms
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   └── apps.py                # App configuration
├── templates/                  # Django templates
│   ├── base.html              # Base template with sidebar
│   ├── transactions/          # Transaction templates
│   │   ├── dashboard.html
│   │   ├── transaction_list.html
│   │   ├── transaction_form.html
│   │   ├── transaction_confirm_delete.html
│   │   └── budget_update.html
│   ├── watchlist/             # Watchlist templates
│   │   ├── watchlist_list.html
│   │   ├── watchlist_form.html
│   │   ├── watchlist_detail.html
│   │   └── watchlist_confirm_delete.html
│   └── registration/          # Authentication templates
│       ├── login.html
│       └── signup.html
└── static/                     # Static files (CSS, JS, images)
```

## 🎨 Design Features

### Color Scheme
- **Primary**: Blue (#3b82f6) for CTAs and links
- **Success**: Green (#10b981) for positive values
- **Danger**: Red (#ef4444) for negative values
- **Warning**: Yellow (#f59e0b) for warnings
- **Background**: Dark gradient (#0a0e27 to #1f2937)

### UI Components
- **Cards**: Gradient backgrounds with borders and shadows
- **Tables**: High-contrast with hover effects
- **Badges**: Color-coded status indicators
- **Buttons**: Gradient backgrounds with hover animations
- **Forms**: Dark themed with focus states
- **Sidebar**: Fixed navigation with active states

## 🔧 Key Features Explained

### Django Signals
The application uses Django signals to automatically update the user's balance whenever a transaction is created, updated, or deleted. This ensures data consistency without manual intervention.

```python
@receiver(post_save, sender=Transaction)
def update_balance_on_transaction_save(sender, instance, created, **kwargs):
    # Recalculates and updates user balance automatically
```

### Custom Template Tags
Financial calculations are implemented as custom template tags for reusability:
- `calculate_total_spend`: Calculate expenses for a period
- `calculate_total_income`: Calculate income for a period
- `budget_status`: Determine budget health (safe/warning/danger)
- `percentage`: Calculate percentage values
- `format_currency`: Format numbers as currency

### Form Validation
All forms include comprehensive validation:
- Amount must be positive
- Dates are validated
- Symbols are converted to uppercase
- Purchase price is required if quantity is specified

## 📊 Database Schema

### Transaction Model
- user: ForeignKey to User
- transaction_type: Choice (INCOME/EXPENSE)
- category: Choice (multiple categories)
- amount: DecimalField
- description: TextField
- date: DateField
- created_at, updated_at: DateTimeField

### UserProfile Model
- user: OneToOneField to User
- total_balance: DecimalField
- monthly_budget: DecimalField
- created_at, updated_at: DateTimeField

### Watchlist Model
- user: ForeignKey to User
- symbol: CharField (unique per user)
- name: CharField
- asset_type: Choice (STOCK/ETF/CRYPTO/etc)
- status: Choice (BUY/HOLD/SELL)
- target_price, current_price: DecimalField
- quantity, purchase_price: DecimalField
- notes: TextField
- created_at, updated_at: DateTimeField

## 🔒 Security Features

- CSRF protection on all forms
- User authentication required for all views (except login/signup)
- QuerySets filtered by user to ensure data privacy
- Password validation with Django's validators
- Secure session management

## 📝 Future Enhancements

Potential features for future development:
- API integration for real-time stock prices
- Data visualization with charts (Chart.js)
- Export to CSV/PDF
- Email notifications for budget alerts
- Recurring transactions
- Multi-currency support
- Investment portfolio analytics
- Tax reporting features

## 🤝 Contributing

This is a demonstration project. For production use:
1. Change SECRET_KEY in settings.py
2. Set DEBUG = False
3. Configure proper database (PostgreSQL)
4. Set up proper static files handling
5. Implement proper logging
6. Add comprehensive tests
7. Set up CI/CD pipeline

## 📄 License

This project is created for educational and demonstration purposes.

## 👤 Author

Built with Django 5.x, demonstrating professional web development practices and modern FinTech design principles.

---

**Note**: This is a development setup. For production deployment, additional configuration is required including proper security settings, production database, static file serving, and environment variables.
