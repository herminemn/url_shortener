from django.db import models

from urlsh.models import Url


class ClickUrlManager(models.Manager):
    def create_count(self, urlInstance):
        if isinstance(urlInstance, Url):
            obj, created = self.get_or_create(url_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickUrl(models.Model):
    url_url = models.OneToOneField(Url)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickUrlManager()

    def __str__(self):
        return '{i}'.format(i=self.count)
