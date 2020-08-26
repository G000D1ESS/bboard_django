# BBoard on Django

![Preview](https://i.yapx.ru/Iu7ZZ.jpg)

This project was created to **advertise the sale of goods on the Internet.**

## Instructions

To run the project:

```bash
git clone https://github.com/G000D1ESS/bboard_django.git

cd bboard
pip install -r requirements.txt

# Rename example_settings.py to settings.py in learn folder
# Replace your personal DB info in settings.py

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver localhost:80
```

Server should be live at http://127.0.0.1/ now.