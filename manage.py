#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_mars.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Usando a variável de ambiente PORT (ou 8000 como fallback)
    port = os.environ.get('PORT', '8000')
    execute_from_command_line([sys.argv[0], 'runserver', f'0.0.0.0:{port}'])


if __name__ == '__main__':
    main()
