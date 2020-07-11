from django.db import models
from django.contrib.auth.models import User
# Create your models here.

indiv = [('student','student'), ('enterpreneur','enterpreneur'), ('Businessman','Businessman')]
searching = [('startup-idea','startup-idea'), ('startup-company','startup-company')]
joinas = [('cofounder','cofounder'),('team-member','team-member'),('partner','partner'),('others','others')]


class EduDetails(models.Model):
	name = models.CharField(max_length=200,blank=True,null=True)
	college_name = models.CharField(max_length=200,blank=True)
	course_name = models.CharField(max_length=200,blank=True)
	passing_year = models.DateTimeField()
	grade = models.IntegerField(default= 0)

	def __str__(self):
		return self.college_name


class SKILLS(models.Model):
	name = models.CharField(max_length=30)
	class Meta:
		ordering = ['name']
			
	def __str__(self):
		return self.name



class CofndProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Cofounder_user')
	yourself = models.CharField(max_length=100,blank=True,choices=indiv) 
	looking_for = models.CharField(max_length=100,blank=True,choices=searching)
	industry = models.CharField(max_length=200,blank=True)
	join_as = models.CharField(max_length=100,blank=True,choices=joinas)
	name = models.CharField(max_length=200,blank=True,unique=True)
	employment = models.CharField(max_length=200,blank=True)
	college_name = models.CharField(max_length=200,blank=True)
	course_name = models.CharField(max_length=200,blank=True)
	passing_year = models.DateTimeField()
	grade = models.IntegerField(default= 0)
	skills = models.ManyToManyField(SKILLS,blank=True)
	created_at = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.name





def create_profile(sender, **kwargs):
	if kwargs['created']:
		cofnd_profile = CofndProfile.objects.create(user=kwargs['instance'])









profas = [('student','student'), ('enterpreneur','enterpreneur'), ('Businessman','Businessman'),('Investor','Investor'),('Freelancers','Freelancers'),('Student Enterpreneur','Student Enterpreneur')]


class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='UserProfileInfo')
	about = models.CharField(max_length=100,blank=True,choices=indiv)
	profile_as = models.CharField(max_length=100,blank=True,choices=profas)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	Address = models.TextField(max_length=400,blank=True)
	Contact = models.BigIntegerField(unique=True,blank=True)
	Country = models.CharField(max_length=100,blank=True)
	City = models.CharField(max_length=100,blank=True)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)
	def __str__(self):
		return self.user.username



class CompanyBase(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='CompanyUserProfile')
	company_name = models.CharField(max_length=200,blank=True)
	company_email = models.EmailField()
	website = models.CharField(max_length=200,blank=True)
	def __str__(self):
		return self.company_name


class CompanyInfo(models.Model):
	Company = models.OneToOneField(CompanyBase,on_delete=models.CASCADE,related_name='CompanyInfo')
	cmp_address = models.CharField(max_length=200,blank=True)
	City = models.CharField(max_length=200,blank=True)
	industry = models.CharField(max_length=200,blank=True)
	Businesstype = models.CharField(max_length=200,blank=True)
	About_cmp = models.CharField(max_length=500,blank=True)
	def __str__(self):
		return self.Company.company_name



class Products(models.Model):
	productcompany = models.ForeignKey(CompanyBase,on_delete=models.CASCADE, unique=False,related_name='Product_cmp')
	product_pic = models.ImageField(upload_to='product_pics',blank=True)
	Prod_name = models.CharField(max_length=200,blank=True,unique=True)
	Description = models.CharField(max_length=300,blank=True)

	def __str__(self):
		return self.Prod_name




jobtype = [('part_time','part_time'),('full_time','full_time'),('Freelancing_work','Freelancing_work'),('Internship','Internship')]

class JobOpening(models.Model):
	ForCompany = models.ForeignKey(CompanyBase,on_delete=models.CASCADE, unique=False,related_name='Company_details')
	JobTilte = models.CharField(max_length=200,blank=True,unique=True)
	Location = models.CharField(max_length=200,blank=True)
	JobType = models.CharField(max_length=100,blank=True,choices=jobtype)

