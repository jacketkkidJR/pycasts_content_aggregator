**PyCasts content aggregator**

This project was created with the help of the Real Python project https://realpython.com/build-a-content-aggregator-python/ and Linekdin learning courses: https://www.linkedin.com/learning/paths/become-a-django-developer?u=76816450.
To run this project you will need to install django, django-crispy-forms, crispy-bootstrap5 and pillow. 

**Note:** this project can be run only on the localhost!

In this project I implemented both front-end and back-end development. The main aim of this project is to create an app that can take information from different sources and porperly display it on the page, so users
will see some preview info, such as the header/topic and some short description. In my case I stopped on the Python podcasts. I used two feeds: Real Python and Talk Python To Me podcasts. 

Additionally, I implemented login/logout and registration systems. Users can create their accounts and manage them on the profile page: avatar, username and email can be changed. All forms use csrf token so as to 
make all interactions safe and protected from the cross-site request forgery. Also all passwords are stored encrypted in the database using Argon2 Password Hasher.

**Homepage.**

When you run the server it will first lead you to the homepage. You can see the current time in your region and a link to the podcasts page. Also on all the pages you can see the navigation bar, that can navigate you throughout 
all pages.

**Podcasts page.**

When you go to the podcasts page, you will see 10 most recent podcasts form the sources with their topic, description and link to listen to a podcast. If you wish to check whether there are some new podcasts that should 
be added, then you need to run in a new terminal:

```python manage.py startjobs```

If you want to add more feeds it can be simply made by adding a couple of lines of code: go to podcasts/management/commands/startjobs.py and add the following:

```
def name_of_the_function():
    """Fetches new episodes or some other info from RSS for name_of_the_source."""
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

**Profile page.**

On this page you can see all the info about your account without only the password. Also there is a form so you can change all this information.

**Logout page.**

This page simply outputs the message after your logout. The navigation bar on this page represents only login and signup, so the users cannot even try to go to the pages, that requires login (login requirement was 
implemented using LoginRequiredMixin from django).

**Login page and Signup page.**

Both pages are used for their direct purposes: login and registration correspondingly. After the user registers he will be redirected to the login page. After successful logging in the user will be automatically redirected to the 
podcasts page.


