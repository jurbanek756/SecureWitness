from django.db import models
from SecureWitness.models import CustomUser


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
    pub_date = models.DateField('Date Published (YYYY-DD-MM)')
    report_text_long = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    incident_date = models.DateField('Incident Date  (YYYY-DD-MM)', null=True)
    file_upload = models.FileField(null=True)
    keyword_list = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    #group = models.ManyToManyField(Group, null=True, related_name='group_login') 
    author = models.CharField(max_length=50)
    objects = ReportManager()

# class Custom_Group(models.Model, Group):
#     group_name = models.CharField(max_length=50)
#     mem_list = models.ForeignKey(Custom_User)
#     def __str__(self):
#         return self.group_name
#
# class Custom_User(models.Model, User):
#     is_admin = models.BooleanField()
#     is_reporter = models.BooleanField()
#     group_list = models.ForeignKey(Custom_Group)
