from django.contrib import admin
from django.contrib.admin import site, ModelAdmin

from forms.models import CofndProfile,EduDetails,UserProfile,CompanyBase,CompanyInfo,Products,JobOpening,JobApplication,WorkProfile,SKILLS

# Register your models here.





admin.site.register(CofndProfile)
admin.site.register(SKILLS)
admin.site.register(EduDetails)
admin.site.register(UserProfile)

admin.site.register(CompanyInfo)
admin.site.register(CompanyBase)


admin.site.register(Products)

admin.site.register(JobOpening)



admin.site.register(JobApplication)
admin.site.register(WorkProfile)