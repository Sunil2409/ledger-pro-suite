from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transactions'
    verbose_name = 'Financial Transactions'
    
    def ready(self):
        import transactions.models  # noqa - Ensure signals are registered
