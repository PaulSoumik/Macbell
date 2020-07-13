from django.shortcuts import render, get_object_or_404
import json
# Create your views here.

from forms.models import CofndProfile,EduDetails,CompanyBase,Products,SKILLS,JobApplication,JobOpening,WorkProfile
from forms.forms import CofndProfileForm,EduDetailsform,UserForm,UserProfileForm,CompanyBaseForm,CompanyInfoForm,ProductForm,JobOpeningForm,WorkProfileForm,WorkProfileFormset,JobApplicationForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views import generic


#Skills = []
Skills = SKILLS.objects.all()
#skills_js = serializers.serialize('json',Skills);
#skills_js = json.dumps(Skills)
skillsall = []

for theskill in Skills.all():
	skillsall.append(theskill.name)

def index(request):
	CmpProducts = []
	cmp_reg = False;
	jobsavailable = []
	usercreatedjobs = []
	if request.user.is_authenticated:
		try:
			usercompany = CompanyBase.objects.get(user_id = request.user.id)
			print(usercompany)
		except CompanyBase.DoesNotExist:
			usercompany = None
		if usercompany:
			cmp_reg= False
			CmpProducts = Products.objects.filter(productcompany_id = usercompany.id)
		else:
			cmp_reg = True
		try:
			jobsavailable = []
			for job in JobOpening.objects.filter(valid= True):
				if job.ForCompany.user != request.user:
					jobsavailable.append(job)
					print(job)
				else:
					usercreatedjobs.append(job)
					print("user created job",job)
		except JobOpening.DoesNotExist:
			jobsavailable = None
	isjobsavailable = len(jobsavailable)
	return render(request,'forms/index.html',{'cmp_reg':cmp_reg,'CmpProducts':CmpProducts,'isjobsavailable':isjobsavailable,'jobsavailable':jobsavailable,'usercreatedjobs':usercreatedjobs})


@login_required
def cofndprofile(request):
	useractive = False
	print("request found")
	if request.method == 'POST':
		User = get_user_model()
		if request.user.is_authenticated:
			useractive = True
		cofn_form = CofndProfileForm(data= request.POST)
		print("data found")
		print(cofn_form)
		if cofn_form.is_valid() and useractive:
			userdata = User.objects.get(username = request.user.username)
			print(userdata.username , userdata.id, userdata.email)
			cofn =cofn_form.save(commit=False)
			cofn.user = userdata
			#print(cofn.skills)
			cofn.save()
			cofn_form.save_m2m()
			print("data saved")
		else:
			print(cofn_form.errors)
			print("not_vald")
		cofnform = CofndProfileForm()
		return render(request,'forms/cofndprofile.html',{'cofnform' : cofnform,'Skills' : Skills,"allskills": skillsall})
	cofnform = CofndProfileForm()
	return render(request,'forms/cofndprofile.html',{'cofnform' : cofnform,'Skills' : Skills,"allskills": skillsall})






def register(request):
    registered = False
    flag =1
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        User = get_user_model()
        if user_form.is_valid() and profile_form.is_valid():
            for User in User.objects.filter():
            	if user_form.cleaned_data['email'] == User.email:
            		flag =0
            		user_form.cleaned_data['username'] = " "
            		print("This mail address already exists!")
     
            if flag ==1:
            	user = user_form.save()
            	print("user saved")
            	user.set_password(user.password)
            	user.save()
            	
            	profile = profile_form.save(commit=False)
            	profile.user = user

            	if 'profile_pic' in request.FILES:
            	    print('found it')
            	    profile.profile_pic = request.FILES['profile_pic']
            	profile.save()
            	registered = True
            else :
            	print("not-saved")
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'forms/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'flag':flag})






def Userlogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account was inactive.")
		else:
			print("Someone tried to login and failed.")
			print("They used username: {} and password: {}".format(username,password))
			return HttpResponse("Invalid login details given")
	else:
		return render(request, 'forms/login.html', {})














@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))





















def CompanyProfile(request):
	User = get_user_model()
	if request.method == 'POST':
			companybase_form = CompanyBaseForm(data=request.POST)
			companyinfo_form = CompanyInfoForm(data=request.POST)
			print("Post method")
			if companybase_form.is_valid() and companyinfo_form.is_valid():
				print("forms valid")
				
				
				print("forms saved locally")
				if request.user.is_authenticated:
					print(request.user.username)
					theuser = User.objects.get(username = request.user.username)
					print(theuser.username , theuser.id, theuser.email)

					#companybase_form.user = theuser
					#companybase_form.user_id = theuser.id
					print("goint to loc save")
					companybase = companybase_form.save(commit=False)
					print("loc save")
					companybase.user = theuser
					print("companybase user done")
					print(companybase.user)
					
					
					
					companyinfo = companyinfo_form.save(commit=False)
					print(companybase)
					companybase.save()
					companyinfo.Company = companybase

					
					companyinfo.save()

					print("company details are saved")
				else:
					print("user mot authenticated")
			else:
				print(companybase_form.errors, companyinfo_form.errors)


	companybase_form = CompanyBaseForm()
	companyinfo_form = CompanyInfoForm()
	return render(request,'forms/company_profile.html',{'companybase_form':companybase_form,'companyinfo_form':companyinfo_form} )
















product_limit = 20;
@login_required
def addProduct(request):
	addpossible = True
	companyexist = True
	thatexist = 1
	company_is = None
	product_form = ProductForm()
	User = get_user_model()
	useris = User.objects.get(username = request.user.username)
	try:
		company_is = CompanyBase.objects.get(user_id = useris.id)
	except CompanyBase.DoesNotExist:
		company_is = None
		companyexist = False
		return render(request, 'forms/addproduct.html',{'product_form' : product_form,'thatexist':thatexist,'companyexist':companyexist,'addpossible':addpossible})
	if companyexist:
		products_num = Products.objects.filter(productcompany_id = company_is.id).count()
		if products_num >= product_limit:
			addpossible = False
			return render(request, 'forms/addproduct.html',{'product_form' : product_form,'thatexist':thatexist,'companyexist':companyexist,'addpossible':addpossible})
	
	if request.method == "POST":
		product = ProductForm(data = request.POST)
		print("product form saved")
		if product.is_valid():
			print("product form is valid")
			product_tosave = product.save(commit=False)
			print("product is new and locally saved")
			product_tosave.productcompany = company_is
			print("product company assigned")
			print(product_tosave)
			print(product_tosave.productcompany)
			product_tosave.save()
			thatexist =2
			print("product saved")
		else:
			print(product.errors)
			if Products.objects.filter(productcompany_id = company_is.id).filter(Prod_name=product.data['Prod_name']):
				print("product already exists")
				thatexist = 0

	product_form = ProductForm()
	return render(request, 'forms/addproduct.html',{'product_form' : product_form,'thatexist':thatexist,'companyexist':companyexist,'addpossible':addpossible})




def editproddetails(request, pk):
	theproduct = None
	print(pk)
	theproduct = get_object_or_404(Products,pk=pk)
	print(pk)
	print(theproduct)
	response ={}
	response['productid'] = theproduct.id
	product_form = ProductForm(request.POST or None, instance= theproduct)
	print(product_form)
	if product_form.is_valid():
		prodname = request.POST['Prod_name']
		proddesc = request.POST['Description']
		print(prodname,proddesc)
		theproduct = product_form.save(commit=False)
		theproduct.save()
		return render(request, 'forms/editdone.html')
	else:
		print("not post")
		#return render(request, 'forms/editdone.html')Prod_name = theproduct.Prod_name,Description = theproduct.Description
	product_form = ProductForm()
	return render(request, 'forms/editproduct.html',{'product_form' : product_form,'theproduct':theproduct},response)













@login_required
def CreateJob(request):
	jobform = JobOpeningForm()
	companynotfound = False
	User = get_user_model()
	useris = User.objects.get(username = request.user.username)
	if request.method == "POST":
		jobformdata = JobOpeningForm(data= request.POST)
		print(jobformdata)
		print("job data is: ")
		company_is = None
		try:
			company_is = CompanyBase.objects.get(user_id = useris.id)
		except CompanyBase.DoesNotExist:
			company_is = None
		if jobformdata.is_valid():
			newjob = jobformdata.save(commit=False)
			if company_is == None:
				companynotfound = True
				return render(request, 'forms/createjob.html',{'jobform':jobform,'Skills' : Skills,'companynotfound':companynotfound})
			newjob.ForCompany = company_is
			newjob.save()
			jobformdata.save_m2m()

	return render(request, 'forms/createjob.html',{'jobform':jobform,'Skills' : Skills,'companynotfound':companynotfound})

















@login_required
def applyforjob(request , pk):
	User = get_user_model()
	useris = User.objects.get(username = request.user.username)
	pass
	if request.method == "GET":
		jobapplyform = JobApplicationForm(request.GET or None)
		workset = WorkProfileFormset(request.GET or None)
	elif request.method == "POST":
		jobapplyformdata = JobApplicationForm(request.POST)
		worksetdata = WorkProfileFormset(request.POST)
		jobdetails = JobOpening.objects.get(pk = pk)
		if jobapplyformdata.is_valid() and worksetdata.is_valid():
			jobapplication = jobapplyformdata.save(commit=False)
			jobapplication.applicant = useris
			jobapplication.jobtilte = jobdetails
			jobapplication.save()
			jobapplications = JobApplication.objects.filter(jobtilte= jobapplication.jobtilte)
			thejobapplication = jobapplications.get(applicant = jobapplication.applicant)
			print(thejobapplication.id, thejobapplication)
			print(type(thejobapplication.id))
			for work in worksetdata:
				print(work)
				workprofile = work.save(commit=False)
				workprofile.jobapplication = thejobapplication
				workprofile.save()
				print("work saved:", workprofile.Company_name )
			print("jobapplication saved:", jobapplication.applicant)

	jobapplyform = JobApplicationForm()
	workset = WorkProfileFormset()

	return render(request, 'forms/jobapplication.html', {'jobapplyform':jobapplyform, 'workset': workset})



@login_required
def applicants(request, pk):
	jobdetails = JobOpening.objects.get(pk = pk)
	alljobapplications = JobApplication.objects.filter(jobtilte = jobdetails)



	return render(request, 'forms/listapplicants.html',{'jobdetails':jobdetails,'alljobapplications':alljobapplications})



@login_required
def fullapplication(request , pk):
	fulljobapplication = JobApplication.objects.get(pk = pk)
	workexp = WorkProfile.objects.filter(jobapplication= fulljobapplication)

	return render(request, 'forms/fullapplication.html',{'fulljobapplication':fulljobapplication,'workexp':workexp})
