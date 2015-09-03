# koodikoulu.fi

Source code for [koodikoulu.fi](http://koodikoulu.fi/). Python 3 + Django.

Development
-----------

Install Python 3.4, eg. `brew install python3`.

Install dependencies:
`pip3 install -r requirements.txt`

Initialize database:  
`python3 manage.py migrate`

Create superuser:
`python3 manage.py createsuperuser`

Run the development server
`python3 manage.py runserver`

Now you can browse the site at `http://localhost:8000` and manage events manually at `http://localhost:8000/admin`.