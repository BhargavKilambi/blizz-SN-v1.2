from django.contrib import admin

from django.conf.urls import url,include
from accounts import views
from django.contrib.auth.views import login,logout
from accounts.views import HomeView



urlpatterns = [
    url(r'^$',views.home),
    url(r'^about/$',HomeView.as_view(),name='about'),
    #url(r'^profile/edit_bio/$',views.update_profile,name='edit_bio'),
    url(r'^login/$',login,{'template_name': 'accounts/login.html'}),
    url(r'^logout/$',logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.view_profile,name='view_profile'),
    url(r'^profile/edit/$',views.update_profile, name ='update_profile'),
]
#
