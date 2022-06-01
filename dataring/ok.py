import os

os.system('python manage.py loaddata dataring/Customer.json')
os.system('python manage.py loaddata dataring/Employee.json')
os.system('python manage.py loaddata dataring/Store.json')
os.system('python manage.py loaddata dataring/Product.json')
os.system('python manage.py loaddata dataring/Order.json')
os.system('python manage.py loaddata dataring/OrderDetail.json')