import os

os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

os.system('python manage.py loaddata dataring/Customer.json')
os.system('python manage.py loaddata dataring/Employee.json')
os.system('python manage.py loaddata dataring/Store.json')
os.system('python manage.py loaddata dataring/Product.json')
os.system('python manage.py loaddata dataring/Order.json')
os.system('python manage.py loaddata dataring/OrderDetail.json')

os.system("""python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('a', 'admin@example.com', 'a')" """)
