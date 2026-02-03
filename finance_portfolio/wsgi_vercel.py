"""
WSGI application adapter for Vercel serverless deployment
"""
import os
import sys

# Add the project directory to the sys.path
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_portfolio.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel serverless function handler
app = application
