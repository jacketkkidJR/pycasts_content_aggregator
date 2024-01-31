from django.test import TestCase
from django.utils import timezone
from .models import Episode
from django.urls.base import reverse

# Creating some simple tests
class PodCastsTests(TestCase):
    def setUp(self):
        """Defining an example Episode object"""
        self.episode = Episode.objects.create(
            title="My Podcast Episode",
            description="I did it!",
            pub_date=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            podcast_name="My Python Podcast",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_episode_content(self):
        """Testing the content of the created Episode object"""
        self.assertEqual(self.episode.description, "I did it!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )

    def test_episode_str_representation(self):
        """Testing the string representation of the created Episode object"""
        self.assertEqual(
            str(self.episode), "My Python Podcast: My Podcast Episode"
        )

    def test_homepage_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepagehomepage.html')

    def test_homepage_list_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'My Podcast Episode')