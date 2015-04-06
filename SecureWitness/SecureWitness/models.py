from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, givenEmail, reporter, givenPass='wahoowah' ):
        email = self.normalize_email(givenEmail)
        user = self.model(name=username, email=email, groups=Group.objects.get(name='Users'), password= givenPass, admin=False,reporter=reporter)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, givenEmail, reporter, givenPass='wahoowah' ):
        email = self.normalize_email(givenEmail)
        user = self.model(name=username, email=email, password= givenPass, admin=True,reporter=reporter)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    admin = models.BooleanField(default=False)
    reporter = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    groups= models.ForeignKey(Group)
    objects= CustomUserManager()
    email = models.CharField(max_length=50, default= 'none')
    USERNAME_FIELD = 'name'
    def __str__(self):
        return self.name


class Report(models.Model):
    # file support to be added
    report_title = models.CharField(max_length=50)
    report_text_short = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    report_text_long = models.TextField()
    location = models.CharField(max_length=100)
    incident_date = models.DateTimeField()
<<<<<<< HEAD
    keyword_list = []
    private = models.BooleanField()
    group = models.ForeignKey(Custom_Group)
    author = models.ForeignKey(Custom_User)
    objects = ReportManager()

class ReportManager(models.Manager):
    def create_report(self, report_title, author, pub_date, report_text_short):
        report = self.create(report_title = report_title, author = author, pub_date = pub_date, report_text_short = report_text_short)
        return report

class Custom_Group(models.Model, Group):
    group_name = models.CharField(max_length=50)
    mem_list = models.ForeignKey(Custom_User)
=======
    keywords = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    group = models.ForeignKey(Group)
    author = models.ForeignKey(CustomUser)
>>>>>>> abc263547733fb1109379906ae6a1e18fd463e26
    def __str__(self):
        string="{"+ self.report_title + " by "+self.author.name+ "\n"+ self.report_text_short + "\n"+ self.pub_date.__str__()+ "\n" + self.report_text_long + "\n" + self.location + "\n" + self.incident_date.__str__() + "\n" + self.keywords + "\n" + "Private: " + self.private.__str__() + "\n"+ self.group.__str__()+ "}"
        return string


