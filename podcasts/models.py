from django.db import models


# Here we create an Episode model
# It should have title, description, publication date, link to the podcast, image and a podcast name
class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        """Creating the string representation"""
        return f"{self.podcast_name}: {self.title}"
