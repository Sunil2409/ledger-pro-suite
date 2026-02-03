#!/bin/bash

echo "================================================"
echo "Finance Portfolio Manager - Setup Script"
echo "================================================"
echo ""

# Check if Django is installed
if ! python3 -c "import django" 2>/dev/null; then
    echo "Installing Django 5.1..."
    pip install Django==5.1 --break-system-packages
    echo "✓ Django installed successfully"
else
    echo "✓ Django is already installed"
fi

echo ""
echo "Creating database tables..."
python3 manage.py makemigrations
python3 manage.py migrate

echo ""
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Create a superuser: python3 manage.py createsuperuser"
echo "2. Run the server: python3 manage.py runserver"
echo "3. Visit http://127.0.0.1:8000/ in your browser"
echo ""
echo "Or run this script with 'run' to start the server:"
echo "./setup.sh run"
echo ""

if [ "$1" = "run" ]; then
    echo "Starting development server..."
    python3 manage.py runserver
fi
