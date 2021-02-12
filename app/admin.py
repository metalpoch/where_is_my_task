from django.contrib import admin
from .models import *


class PreviewContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'query_type', 'send_date']
    list_filter = ['query_type']


class PreviewProfile(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'gender',
        'work_area',
        'leader',
        'programming_area',
    ]
    list_filter = ['leader', 'work_area', 'gender']


class PreviewTask(admin.ModelAdmin):
    list_display = [
        'id',
        'sender',
        'receiver',
        'subject',
        'send_date',
        'limit_date',
        'done'
    ]


admin.site.register(Profile, PreviewProfile)
admin.site.register(Contact, PreviewContact)
admin.site.register(Task, PreviewTask)
