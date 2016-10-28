"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


#My import
from django.http import HttpResponseRedirect
from app.forms import generalUserRegForm
from app.forms import premiumUserRegForm
from app.forms import userLoginForm
from app.forms import searchForStoreForm
from app.forms import searchForProductForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def generalUserReg(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':  
            f = generalUserRegForm(request.POST)
            if f.is_valid():     
                userName = f.cleaned_data.get('General_User_Name')
                password = f.cleaned_data.get('General_User_Password')   
                Email = f.cleaned_data.get('Email')
                return HttpResponseRedirect('app/login/')
            else:
                return render(
                        request,
                          'app/GeneralUserRegister.html',
                          {
                              'generalUserRegForm':f,
                              'year':datetime.now().year,
                          }
                        )          
    else:
        f = generalUserRegForm()
        return render(
                request,
                      'app/GeneralUserRegister.html',
                      {
                          'generalUserRegForm':f,
                          'year':datetime.now().year,
                      }
                    )



def premiumUserReg(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':  
                f = premiumUserRegForm(request.POST)
                if f.is_valid():     
                    userName = f.cleaned_data.get('Premium_User_Name')
                    password = f.cleaned_data.get('Premium_User_Password')                     
                    Email = f.cleaned_data.get('Email')
                    StoreName =  f.cleaned_data.get('Store_Name')
                    Address = f.cleaned_data.get('Address')
                    Zip = f.cleaned_data.get('Zip')
                    return HttpResponseRedirect('app/login/')
                else:
                    return render(
                                request,
                                'app/PremiumUserRegister.html',
                                {
                                    'premiumUserRegForm':f,
                                    'year':datetime.now().year
                                }
                            )          
    else:
        f = premiumUserRegForm()
        return render(
                    request,
                    'app/PremiumUserRegister.html',
                    {
                        'premiumUserRegForm':f,
                        'year':datetime.now().year
                    }
                ) 

def userLogin(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':  
                f = userLoginForm(request.POST)
                if f.is_valid():     
                    userName = f.cleaned_data.get('User_Name')
                    password = f.cleaned_data.get('User_Password')   
                    return HttpResponseRedirect('searchForStores.html')#TODO: Search page or update information page
                else:
                    return render(
                                request,
                                'app/login.html',
                                {
                                    'userLoginForm':f,
                                    'year':datetime.now().year
                                }
                            )          
    else:
        f = userLoginForm()
        return render(
                    request,
                    'app/login.html',
                    {
                        'userLoginForm':f,
                        'year':datetime.now().year
                    }
                )

def searchStores(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':  
                f = searchForStoreForm(request.POST)
                if f.is_valid():     
                    zip = f.cleaned_data.get('Search_Zip') 
                    return HttpResponseRedirect('app/searchForStores.html')#TODO: Search page or update information page
                else:
                    return render(
                                request,
                                'app/searchForStores.html',
                                {
                                    'searchForStoreForm':f,
                                    'year':datetime.now().year
                                }
                            )          
    else:
        f = searchForStoreForm()
        return render(
                    request,
                    'app/searchForStores.html',
                    {
                        'searchForStoreForm':f,
                        'year':datetime.now().year
                    }
                )

def searchProduct(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':  
                f = searchForProductForm(request.POST)
                if f.is_valid():     
                    product_name = f.cleaned_data.get('Product_Name') 
                    return HttpResponseRedirect('searchForProduct.html')#TODO: Search page or update information page
                else:
                    return render(
                                request,
                                'app/searchForProduct.html',
                                {
                                    'searchForProductForm':f,
                                    'year':datetime.now().year
                                }
                            )          
    else:
        f = searchForProductForm()
        return render(
                    request,
                    'app/searchForProduct.html',
                    {
                        'searchForProductForm':f,
                        'year':datetime.now().year
                    }
                )