from models import *
from django.contrib import admin
#from datetime import date, timedelta
#from django.utils.dateformat import DateFormat
class ProjectDetailInline(admin.StackedInline):
    model = ProjectDetail
    max_num = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline,]

admin.site.register(Industry)
admin.site.register(Recipient)
admin.site.register(DevelopmentPartner)
admin.site.register(Project, ProjectAdmin)