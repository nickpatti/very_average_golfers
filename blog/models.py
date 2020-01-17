from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    logo = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


##################  Model for Competition posts and edits ####################


class CompetitionsPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    content2 = RichTextUploadingField(null=True, blank=True)
    priority = models.IntegerField(default='1')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('competitions-detail', kwargs={'pk': self.pk})


class SocialsPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    content2 = RichTextUploadingField(null=True, blank=True)
    priority = models.IntegerField(default='1')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('socials-detail', kwargs={'pk': self.pk})


class TraditionsPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    content2 = RichTextUploadingField(null=True, blank=True)
    priority = models.IntegerField(default='1')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('traditions-detail', kwargs={'pk': self.pk})


#################### ROLL OF HONOUR TABLE MODEL ##############################

class YearRoll(models.Model):
    title = models.IntegerField(verbose_name='year')
    table = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('year-detail', kwargs={'pk': self.pk})


class EventRoll(models.Model):
    title = models.CharField(max_length=50, verbose_name='Competition')
    table = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(default='1')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


class AllTimeRoll(models.Model):
    title = models.CharField(max_length=50, verbose_name='Competition')
    table = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(default='1')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('alltime-detail', kwargs={'pk': self.pk})
#################### LINKS ######################


class LinksPost(models.Model):
    title = RichTextUploadingField()
    image = models.ImageField(default='transparent.png')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('links-detail', kwargs={'pk': self.pk})


################## CURRENT MEMBERS + SUMMARY  ######################

class Members(models.Model):
    title = models.CharField(max_length=100)
    high_chair = models.CharField(max_length=100, verbose_name="High Chair")
    high_chair_image = models.ImageField(blank="True", null="True")
    chair = models.CharField(max_length=100, verbose_name="Chair")
    chair_image = models.ImageField(blank="True", null="True")
    under_chair = models.CharField(max_length=100, verbose_name="Under Chair")
    under_chair_image = models.ImageField(blank="True", null="True")
    humble = models.CharField(max_length=100, verbose_name="Humble")
    humble_image = models.ImageField(blank="True", null="True")

    def get_absolute_url(self):
        return reverse('members-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


################ TROPHY ROOM ######################

class TrophyPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trophy-detail', kwargs={'pk': self.pk})
