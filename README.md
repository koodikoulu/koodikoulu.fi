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

Production
----------

In order for the site to function fully, you must set a few environment variables:

* `SECRET_KEY`
  * There is a default value for this but in order to be safe, change it.
* `MANDRILL_API_KEY`
  * The API key for your [Mandrill](https://www.mandrill.com/) account.
* `GOOGLE_KEY`
  * The API key for Google maps.
* `SLACK_CHANNEL`
  * The email addresss where notifications about new events will be sent. It doesn't have to be a Slack channel, but we think that it's a good idea.
