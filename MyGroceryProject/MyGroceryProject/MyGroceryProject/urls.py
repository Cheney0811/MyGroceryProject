"""
Definition of urls for MyGroceryProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^GeneralUserRegister', app.views.generalUserReg, name = 'GeneralUserReg'),
    url(r'^PremiumUserRegister', app.views.premiumUserReg, name = 'PremiumUserReg'),
    url(r'^app/login',  app.views.userLogin, name = 'LogIn'),       
    url(r'^app/searchForStores', app.views.searchStores, name = 'searchStores'),
    url(r'^app/searchForProduct', app.views.searchProduct, name = 'searchProduct')
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
