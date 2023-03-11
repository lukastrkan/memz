from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup import cleanup


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


@cleanup.select
class Meme(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='memes', blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=False, null=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def preview_tag(self):
        return mark_safe(u'<img src="%s" width="200"/>' % self.image.url)

    def image_tag(self):
        return mark_safe(u'<img src="%s"/>' % self.image.url)
