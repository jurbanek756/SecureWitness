from django.db import models

'''

# Create your models here.

from django.contrib.auth.models import User, Group

class ReportManager(models.Manager):
    def create_report(self, report_title, author, pub_date, report_text_short):
        report = self.create(report_title = report_title, author = author, pub_date = pub_date, report_text_short = report_text_short)
        return report

class Report(models.Model):
    # file support to be added
    report_title = models.CharField(max_length=50)
    report_text_short = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    report_text_long = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    incident_date = models.DateTimeField()
    keyword_list = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    # group = models.ForeignKey(Custom_Group)
    # author = models.ForeignKey(Custom_User)
    objects = ReportManager()

'''
