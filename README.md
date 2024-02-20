**PyCasts content aggregator**

This project was created with the help of the Real Python project https://realpython.com/build-a-content-aggregator-python/ and Linekdin learning courses: https://www.linkedin.com/learning/paths/become-a-django-developer?u=76816450. CSS and JS were taken from the Bootstrap version 5.3.2.
To run this project you will need to install django, django-crispy-forms, crispy-bootstrap5, pillow and python-dotenv.

_**Note:** this project can be run only on the local host!_

In this project I implemented both front-end and back-end development. The main aim of this project is to create an app that can take information from different sources and porperly display it on the page, so users will see some preview info, such as the header/topic and some short description. In my case I stopped on the Python podcasts. I used two feeds: Real Python and Talk Python To Me podcasts. 

Additionally, I implemented login/logout, registration and password reset systems. Users can create their accounts and manage their data on the profile page: avatar and email can be changed. I didn't use default user model provided by django in django.contrib.auth.models. Instead of this I created a custom user model that uses email insted of username for login. That was done to make easier the implementation of password reset system.

All forms use csrf token so as to make all interactions safe and protected from the cross-site request forgery. Also all passwords are stored encrypted in the database using Argon2 Password Hasher.

**Homepage.**

When you run the server it will first lead you to the homepage. You can see a welcoming message, current date and time in your region and a link to the podcasts page. Also on all the pages you can see the navigation bar, that can navigate you throughout all pages.

**Pycasts page.**

When you go to the pycasts page, you will see 10 most recent podcasts form the sources with their topic, description and link to listen to a podcast. If you wish to check whether there are some new podcasts that should be added, then you need to run in a new terminal:

```python manage.py startjobs```

If you want to add more feeds it can be simply made by adding a couple of lines of code: go to podcasts/management/commands/startjobs.py and add the following:

```
def name_of_the_function():
    """Fetches new episodes (or some other info) from RSS for name_of_the_source."""
    _feed = feedparser.parse("link_to_the_feed")
    save_new_episodes(_feed)
```

Also you have to adjust the handle function by adding a job to the new source. You will have to add the following:

```
scheduler.add_job(
            name_of_the_function_you_created_without_brackets,
            trigger="interval",
            minutes=2, #or any other number of minutes you would like
            id="name_of_the_source",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: name_of_the_source.")
```

After that you need to complete the added jobs so the new episodes/info from the new sources will be added. Simply run this to a new terminal:

```
python manage.py startjobs
```

_**Note:** this page cannot be accessed without logging in. If a user tries to do this, he will be automatically redirected to the login page._

**Profile page.**

On this page you can see all the info about your account without only a password. Also there is a form so you can change your email and avatar.

**Logout page.**

This page simply outputs the message after your logout. The navigation bar on this page represents only home, login and signup, so the users cannot even try to go to the pages, that require login (login requirement was implemented using LoginRequiredMixin from django.contrib.auth.mixins).

**Login page and Signup page.**

Both pages are used for their direct purposes: login and registration correspondingly. After the user registers he will be redirected to the login page. After successful logging in the user will be automatically redirected to the podcasts page.

**Password reset system.**

When a user goes to the login page he can find a "Forgot Password?" link. It will lead a user to the password reset page, where he should provide his email address. After entering his email adress, the user will automatically be redirected to the "password-reset-sent" page that outputs a message that an email with a password reset link was sent. The system will check whether a provided email address exists in the database and send an email with a unique password reset link. If a provided email address doesn't exist in the database, a user will not be notified in any way. This is done to protect other users from stealing their account email address. After clicking the password reset link in an email the user will be directed to the "password-reset-confirm" page where he will be able to type his new password and successfully change it. After this step he will be redirected to "password-reset-complete" page where a success message will appear with a link to the login page.

_**Note:** in this project email will not be sent to the email address. Instead, it will appear in the console. If you would like to change that, simply change ``` EMAIL_BACKEND = 
'django.core.mail.backends.console.EmailBackend' ``` to ``` EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' ```. After that you should provide your email address to ``` EMAIL_HOST_USER ``` and password to ``` EMAIL_HOST_PASSWORD ```. In my project they (as well as ``` SECRET_KEY ```) are hidden in .env file that is not uploaded to github so as to protect my personal data._ 
