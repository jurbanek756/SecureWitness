from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, BaseUserManager, User
from django.contrib.admin.widgets import AdminDateWidget

class CustomUserManager(BaseUserManager):
    def create_user(self, username, givenEmail, reporter, givenPass='wahoowah' ):
        email = self.normalize_email(givenEmail)
        user = self.model(name=username, email=email, reporter=reporter, groups=Group.objects.get(name='Users'), password= givenPass, admin=False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, given_email, reporter, given_pass='wahoowah'  ):
        email = self.normalize_email(given_email)
        user = self.model(name=username, email=email, reporter=reporter, groups=Group.objects.get(name='Users'), password= given_pass, is_staff= True,  admin=True)
        user.save(using=self._db)
        return user




class CustomUser(AbstractBaseUser):
    user = models.OneToOneField(User, null=True)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    reporter = models.BooleanField(default=False)
    name = models.CharField(max_length=20, unique=True)
    groups= models.ManyToManyField(Group, null=True)
    objects= CustomUserManager()
    email = models.CharField(max_length=50, default= 'none')
    USERNAME_FIELD = 'name'
    def __str__(self):
        return self.name

class ReportManager(models.Manager):
    def create_report(self, report_title, author, pub_date, incident_date, report_text_short, file_upload, report_text_long, location, private, group, keyword_list):
        report = self.create(report_title = report_title, author = author, pub_date = pub_date, incident_date = incident_date, report_text_short = report_text_short, file_upload=file_upload, report_text_long=report_text_long, location=location, private=private, group=group, keyword_list=keyword_list)
        return report



class Report(models.Model):
    # file support to be added
    report_title = models.CharField(max_length=50)
    report_text_short = models.CharField(max_length=150)
    pub_date = models.DateField('Date Pulished (YYYY-MM-DD)')
    report_text_long = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=100)
    incident_date = models.DateField('Incident Date (YYYY-MM-DD)')
    file_upload = models.FileField(null=True, blank = True)
    objects = ReportManager()
    keyword_list = models.CharField(max_length=50, null=True)
    private = models.BooleanField(default=False)
    group = models.ForeignKey(Group)
    author = models.CharField(max_length=50)
    def __str__(self):
        string="{"+ self.report_title + " by "+self.author+ "\nShort Description: "+ self.report_text_short + "\nPublication Date: "+ str(self.pub_date)+ "\nAbstract: " + self.report_text_long + "\nLocation: " + self.location + "\nIncident Date: " + str(self.incident_date) + "\nKeywords: " + str(self.keyword_list) + "\n" + "Private: " + str(self.private) + "}"
        return string



