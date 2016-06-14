from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Accounts(models.Model):
    userid = models.IntegerField(default=0)
    name = models.CharField(max_length=300, default='')
    mobile = models.CharField(max_length=20, default='')
    photo = models.FileField(null=True)
    additional_info = models.CharField(max_length=2000, default='')
    contest_pic = models.FileField(null=True)
    likes_count = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('cool:index')


    def __str__(self):
        return self.name + ' - ' + self.mobile

class Likes(models.Model):
    likers_id = models.IntegerField()
    pic_id  = models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.likers_id



