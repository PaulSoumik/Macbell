from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from forms import views
# SET THE NAMESPACE!
app_name = 'forms'


urlpatterns=[
    url(r'^cofndprofile/$',views.cofndprofile,name='cofndprofile'),
    url(r'^signup/$',views.register,name='register'),
    url(r'^login/$',views.Userlogin,name='login'),
    url(r'^$',views.user_logout,name='logout'),
    url(r'^Company_profile/$',views.CompanyProfile,name='Company_profile'),
    url(r'^Add_Products/$',views.addProduct,name='addproduct'),
    url(r'^CreateJob/$',views.CreateJob,name='createjob'),
    url(r'^productedit/(?P<pk>.*)/$',views.editproddetails,name='editproductdetails'),
    url(r'^JobApplication/(?P<pk>.*)/$',views.applyforjob,name='joobapplication'),
    url(r'^ApplicantsList/(?P<pk>.*)/$',views.applicants,name='applicantslist'),
    url(r'^FullApplication/(?P<pk>.*)/$',views.fullapplication,name='fullapplication')
    ]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)