from django.contrib import admin
from SecureWitness.models import CustomUser, Report #Custom_Group
from django.forms import Textarea
from django.db import models

class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['report_title']}),
        (None,               {'fields': ['pub_date']}),
        (None,               {'fields': ['report_text_short']}),
        (None,               {'fields': ['report_text_long']}),
        (None,               {'fields': ['location']}),
        (None,               {'fields': ['incident_date']}),
        (None,               {'fields': ['keyword_list']}),
        (None,               {'fields': ['private']}),
        (None,               {'fields': ['group']}),
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['file_upload']})
    ]
"""
class Custom_GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['group_name']})
        (None,               {'fields': ['mem_list']})
    ]
"""


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['admin']}),
        (None,               {'fields': ['reporter']}),
        (None,               {'fields': ['email']}),
        (None,               {'fields': ['groups']})
    ]

admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(Custom_Group, Custom_GroupAdmin)
admin.site.register(Report, ReportAdmin)
