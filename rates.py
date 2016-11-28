import requests
import os
import random
from utilities import load_json, uprint, write_json

def main():
    rates = load_json('./json/rates.json')
    for currency_rate in rates.items():
        currency = currency_rate[0][3:]
        try:
            Currency_object = models.Currency.objects.get(iso_code=currency)
        except:
            break
        Currency_object.usd_rate = currency_rate[1]


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    import django
    django.setup()
    from app import models

    main()
