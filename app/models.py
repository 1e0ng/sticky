from django.db import models


class User(models.Model):
    email = models.CharField(max_length=512)
    phone = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.email

class Note(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=500)
    creator = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

