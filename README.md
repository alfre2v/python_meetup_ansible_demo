# python_meetup_ansible_demo

Demo code for "An Evening of Python Coding" event hosted by the Austin Python Meetup group on Jun 18, 2024.

This demo code consist of two parts each contained in a folder:

1. `tutor_site`: Contains a simple Django Application resulting of following the Django tutorial.
2. `deployment`: Contains ansible files needed to deploy the application as well as Vagrant files 

--------------------------------------------------------------------

## The application tutor_site

This is a demo Django application creating from following Django official tutorial.

This application should be as simple as possible while still introducing beginners to the most basic Django concepts.

Links to the tutorial sections we followed:

- Part 1: Requests and responses [https://docs.djangoproject.com/en/5.0/intro/tutorial01/](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- Part 2: Models and the admin site [https://docs.djangoproject.com/en/5.0/intro/tutorial02/](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)
- Part 3: Views and templates [https://docs.djangoproject.com/en/5.0/intro/tutorial03/](https://docs.djangoproject.com/en/5.0/intro/tutorial03/)
- Part 4: Forms and generic views [https://docs.djangoproject.com/en/5.0/intro/tutorial04/](https://docs.djangoproject.com/en/5.0/intro/tutorial04/)
- Part 5: Testing [https://docs.djangoproject.com/en/5.0/intro/tutorial05/](https://docs.djangoproject.com/en/5.0/intro/tutorial05/)
- Part 6: Static files [https://docs.djangoproject.com/en/5.0/intro/tutorial06/](https://docs.djangoproject.com/en/5.0/intro/tutorial06/)
- Part 7: Customizing the admin site [https://docs.djangoproject.com/en/5.0/intro/tutorial07/](https://docs.djangoproject.com/en/5.0/intro/tutorial07/)
- Part 8: Adding third-party packages [https://docs.djangoproject.com/en/5.0/intro/tutorial08/](https://docs.djangoproject.com/en/5.0/intro/tutorial08/)

### Running the app in local development mode (never use this in production)

Run the local server: `$ python manage.py runserver`

Then:

- If you go to `http://127.0.0.1:8000/` you will get a 404 because no url pattern matches the root url.
- To access the Polls app navigate to: `http://127.0.0.1:8000/polls/` . This app demonstrates using functional views, has limited tests but does customize the admin interface.
- To access the Polls generic app navigate to: `http://127.0.0.1:8000/polls_gen/` . This app demonstrates using generic class views, has all the tests, but does not customize the admin interface.
- To access the admin interface: `http://127.0.0.1:8000/admin/` . The admin interface has been customized for the polls app. Admin customizations include the admin question list view: `http://localhost:8000/admin/polls/question/` and also the question detail view: `http://localhost:8000/admin/polls/question/2/change/`.

### Admin user

For the admin interface I created an admin user:

```text
$ python manage.py createsuperuser

user: admin
email: admin@tutor_site.net
pass: Gr3enM0nkeyL4tte%_
```

--------------------------------------------------------------------

## The deployment folder

This folder contains everything related to our Ansible deployment logic. This is not part of the Django app logic.

For simplicity, in small projects it's ok to keep our ansible files in the same git repository than our application.
However, for real projects I would recommend having a separate repository for the deployment.

