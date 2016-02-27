How to contribute
-----------------

Running code schools is a collaborative effort involving multiple individuals and companies. Therefore, the website [koodikoulu.fi](https://koodikoulu.fi) is open source as well. We are more than happy to recieve contributions to the project.

### Bugs and features

If you find a bug in the application or you come up with a good feature, please go to the [issues page](https://github.com/koodikoulu/koodikoulu.fi/issues) and submit it there. We will then evaluate the issue and get back to you.

### Getting Started

If you want to participate to the development of koodikoulu.fi, please follow these steps:

* Make sure you have a [GitHub](https://github.com) account.
* Fork the application (Tutorial [here](https://help.github.com/articles/fork-a-repo/)).
* Develop the feature on your own local copy of the application. See the [development section]() on how to run the application locally
* Create a pull request (Tutorial [here](https://help.github.com/articles/using-pull-requests/)). If the feature has an issue listed on the [issues page](https://github.com/koodikoulu/koodikoulu.fi/issues), please refer to it in the pull request/commit message (an example commit message: `Normal commit message here. Fixes #5`).

### Development environment
[Koodikoulu.fi](http://koodikoulu.fi) is a Django application that requires Python 3.4.

Using [virtualenv](https://virtualenv.pypa.io/en/latest/) is the preferred way to manage dependencies while developing Python applications and we suggest using it.

##### Installing requirements
Requirements for the applications are located in the `requirements.txt`file. You can install the requirements easily with the command:  
`pip install -r requirements.txt`

##### Database

You can use either [SQLite](https://www.sqlite.org/) or [PostgreSQL](http://www.postgresql.org/) as the database for the application. Our production environment uses PostgreSQL but it is easier to use SQLite while developing the application.

##### Initializing the application

Running the Django application for the first time requires a few commands.

First, you need to initialize the database:  
`python3 manage.py syncdb`

You can create a superuser while running the syncdb command or separately by running the command:  
`python3 manage.py createsuperuser`

After that you can run the development server with the command:  
`python3 manage.py runserver`

##### Making changes to the database models

If you make any changes to the database models, you have to create migrations for the changes. You can do that by running the command:  
`python3 manage.py makemigrations`

After making the migrations, you can run them with the command:  
`python3 manage.py migrate`

### Production

Running the application on [Heroku](https://heroku.com) requires setting a few environment variables.

* `SECRET_KEY`
  * There is a default value for this but in order to be safe, change it.
* `SENDGRID_USERNAME`
    * Username for your [Sendgrid](https://sendgrid.com/) account.
* `SENDGRID_PASSWORD`
    * Password for your [Sendgrid](https://sendgrid.com/) account.
* `GOOGLE_KEY`
  * The API key for Google maps.
* `SLACK_CHANNEL`
  * The email address where notifications about new events will be sent. It doesn't have to be a Slack channel, but we think that it's a good idea.