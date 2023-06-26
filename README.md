# Employees
### Run project:
1. Create virtual environment `python -m venv venv`
2. Activate virtual environment `source venv/bin/Scripts/activate` (Windows:`venv\Scripts\activate`)
3. Update pip to latest version `python -m pip install --upgrade pip`
4. Update setuptools to latest version `python -m pip install --upgrade setuptools`
5. Install requirements `pip install -r requirements.txt`
6. Run migrate `python manage.py migrate`
7. Create superuser `python manage.py createsuperuser`
8. Run server `python manage.py runserver`