from django.db import models



# Create your models here.

class Report(models.Model):
    '''
    Info a reporter provides for each report include the following. (Those labeled "optional" do not have to be proved by a reporter when creating a report.):
    Timestamp when report created.
    Short description. (Say one line of text.)
Detailed description. (Longer.)
Location (optional)
Date of incident being reported (optional).
User-supplied keywords (optional)
One or more files (optional). The report has the option to encrypt the files. Any file format can be uploaded.
Whether the report is public or private.
    '''