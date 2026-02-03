# Troubleshooting Guide

## Error: "no such table: transactions_userprofile"

This error means the database tables haven't been created yet. Follow these steps:

### Solution 1: Run Migrations (Recommended)

```bash
cd finance_portfolio

# Step 1: Create migration files (if needed)
python3 manage.py makemigrations

# Step 2: Apply migrations to create database tables
python3 manage.py migrate

# Step 3: Create superuser
python3 manage.py createsuperuser

# Step 4: Run the server
python3 manage.py runserver
```

### Solution 2: If makemigrations fails

If you get errors during `makemigrations`, the migration files are already included. Just run:

```bash
python3 manage.py migrate
```

### Solution 3: Fresh Start

If you're still having issues, delete the database and start fresh:

```bash
# Remove existing database
rm db.sqlite3

# Remove migration files (optional)
rm transactions/migrations/0*.py
rm watchlist/migrations/0*.py

# Create new migrations
python3 manage.py makemigrations transactions
python3 manage.py makemigrations watchlist

# Apply migrations
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser

# Run server
python3 manage.py runserver
```

## Other Common Issues

### Issue: "Django is not installed"

**Solution:**
```bash
pip install Django==5.1
# OR for macOS/Linux
pip3 install Django==5.1
```

### Issue: "Permission denied" when running manage.py

**Solution:**
```bash
chmod +x manage.py
# OR run with python explicitly
python3 manage.py migrate
```

### Issue: Port 8000 already in use

**Solution:**
```bash
# Use a different port
python3 manage.py runserver 8080

# OR find and kill the process using port 8000
# On Mac/Linux:
lsof -ti:8000 | xargs kill -9

# On Windows:
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

### Issue: "Module not found" errors

**Solution:**
Make sure you're in the correct directory:
```bash
cd finance_portfolio
ls -la  # Should see manage.py
```

### Issue: CSS not loading / Tailwind not working

**Solution:**
The app uses Tailwind CSS via CDN, so you need an internet connection. If you want offline support:

1. Download Tailwind CSS
2. Place it in `static/css/`
3. Update base.html to reference local file

### Issue: Can't access admin panel

**Solution:**
```bash
# Create superuser first
python3 manage.py createsuperuser

# Then visit:
http://127.0.0.1:8000/admin/
```

## Verification Steps

After setup, verify everything works:

1. **Check Database:**
```bash
python3 manage.py dbshell
.tables  # Should show all tables
.exit
```

2. **Check Migrations:**
```bash
python3 manage.py showmigrations
# Should show [X] for all migrations
```

3. **Run Tests:**
```bash
python3 manage.py check
# Should show "System check identified no issues"
```

## Debug Mode

If you need more detailed error messages:

1. Open `finance_portfolio/settings.py`
2. Make sure `DEBUG = True` (already set)
3. Check terminal for detailed error traces

## Getting Help

If you still have issues:

1. Check the error message carefully
2. Look in the terminal/console for stack traces
3. Verify you're using Python 3.8+
4. Ensure Django 5.1 is installed
5. Make sure you're in the `finance_portfolio` directory

## Quick Checklist

Before running the app, ensure:

- [ ] Python 3.8+ installed
- [ ] Django 5.1 installed (`pip list | grep Django`)
- [ ] In correct directory (contains `manage.py`)
- [ ] Migrations run (`python3 manage.py migrate`)
- [ ] Superuser created
- [ ] No other process on port 8000

## Contact

If none of these solutions work, please provide:
- Exact error message
- Output of `python3 --version`
- Output of `pip list | grep Django`
- Operating system
