[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-382/)

# Stocketmarket app
Stockmarket app let's you save stock ticker symbols to the database, then connects to a third party API to collect stock market information about your stocks!
## How to start?
Your first commands would be:
```
git clone <SSH address of this repo>
cd stocks/
python3 -m myenv venv
source venv\bin\activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver
```
You can see deployed project here - 