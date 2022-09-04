#!/usr/bin/bash

rm -rf ./crm/migrations
rm -rf db.sqlite3

python manage.py makemigrations crm

python manage.py migrate

python manage.py loaddata fixture-rank.json
python manage.py loaddata fixture-seats.json
python manage.py loaddata fixture-setting.json
python manage.py loaddata fixture-tax.json
# python manage.py loaddata fixture-appointservice.json
# python manage.py loaddata fixture-basicservice.json
python manage.py loaddata fixture-productcategory.json
python manage.py loaddata fixture-card.json
python manage.py loaddata fixture-product.json
# python manage.py loaddata fixture-customer.json
# python manage.py loaddata fixture-cast.json
python manage.py loaddata fixture-payment.json
python manage.py loaddata fixture-service.json
# python manage.py loaddata fixture-question.json

# python manage.py loaddata fixture-salesheader.json
# python manage.py loaddata fixture-salesdetail.json
python manage.py create_admin
python manage.py runserver 0.0.0.0:8000
