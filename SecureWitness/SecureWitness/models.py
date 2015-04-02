from django.db import models
from django.contrib.auth.models import User, Group


class Report(models.Model):
    # file support to be added
    report_title = models.CharField(max_length=50)
    report_text_short = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    report_text_long = models.CharField()
    location = models.CharField(max_length=100)
    incident_date = models.DateTimeField()
    keyword_list = []
    private = models.BooleanField()
    group = models.ForeignKey(Custom_Group)
    author = models.ForeignKey(Custom_User)


class Custom_Group(models.Model, Group):
    group_name = models.CharField(max_length=50)
    mem_list = models.ForeignKey(Custom_User)
    def __str__(self):
        return self.group_name

class Custom_User(models.Model, User):
    is_admin = models.BooleanField()
    is_reporter = models.BooleanField()
    group_list = models.ForeignKey(Custom_Group)