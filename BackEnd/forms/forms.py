from django import forms
from forms.models import CofndProfile,EduDetails,UserProfile,CompanyBase,CompanyInfo,Products,JobOpening,SKILLS,JobApplication,WorkProfile
from django.forms import formset_factory
class CofndProfileForm(forms.ModelForm):
     class Meta():
         model = CofndProfile
         fields = ('yourself','looking_for','industry','join_as','name','employment','college_name','course_name','passing_year','grade','skills')#

class skillform(object):
	class Meta():
		model = SKILLS

class EduDetailsform(forms.ModelForm):
	class Meta():
		model= EduDetails
		exclude = ('name',)




from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileForm(forms.ModelForm):
     class Meta():
         model = UserProfile
         fields = ('about','profile_as','profile_pic','Address','Contact','Country','City')















class CompanyBaseForm(forms.ModelForm):
	class Meta():
		model = CompanyBase
		fields = ('company_name','company_email','website')

class CompanyInfoForm(forms.ModelForm):
	class Meta():
		model = CompanyInfo
		fields = ('cmp_address','City','industry','Businesstype','About_cmp')

		






class ProductForm(forms.ModelForm):
	class Meta():
		model = Products
		fields = ('Prod_name','product_pic','Description')







class JobOpeningForm(forms.ModelForm):
	class Meta():
		model = JobOpening
		fields = ('JobTilte','Location','JobType','experience','Last_date','valid','reqskills')#




class JobApplicationForm(forms.ModelForm):
	class Meta():
		model = JobApplication
		fields = ('applyas','college_name','course_name','passing_year','grade','aboutapplicant')


class WorkProfileForm(forms.ModelForm):
	class Meta():
		model = WorkProfile
		fields = ('Company_name','Post','Start_date','end_date')



WorkProfileFormset = formset_factory(WorkProfileForm, extra =1)









