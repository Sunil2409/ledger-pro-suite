"""
WSGI config for finance_portfolio project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_portfolio.settings')

application = get_wsgi_application()
