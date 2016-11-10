"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


#My import
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.forms.formsets import formset_factory
import sys
#Django Authndication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#Hash lib import
import hashlib
#Import models py
from app.models import *
#Import all the forms
from app.forms import generalUserRegForm,premiumUserRegForm,userLoginForm,searchForStoreForm,searchForProductForm,publishAdvertisementForm,InventoryForm
#Import message lib
from django.contrib import messages
#Set global variable
generalUserID = 0
premiumUserID = 0

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
            if (f.cleaned_data.get('General_User_Password') == f.cleaned_data.get('General_User_Password_Confirm')):     
                userName = f.cleaned_data.get('General_User_Name')
                password = f.cleaned_data.get('General_User_Password')               
                email = f.cleaned_data.get('Email')
                ##Encode password
                #bPassword = password.encode()
                #ePassword = hashlib.sha512()
                #ePassword.update(bPassword)
                #encryptedPassword = ePassword.digest()                
                try:
                    global generalUserID
                    generalUserID +=1
                    genUser = General_User.objects.create(General_User_ID = generalUserID, General_User_Name = userName, Email = email)
                    genAuthUser = User.objects.create_user(userName,email, password);
                except: # catch *all* exceptions
                    messages.error(request,  sys.exc_info()[0])
                    return render(
                        request,
                            'app/GeneralUserRegister.html',
                            {
                                'generalUserRegForm':f,
                                'year':datetime.now().year,
                            }
                        )
                if genAuthUser:  
                    messages.success(request, 'User successfully created and logged in!')
                    return render(                    
                                request,
                                'app/index.html',
                                {
                                    'title':'Home Page',
                                    'year':datetime.now().year,
                                }
                            )         
            else:
                messages.error(request, 'Confirm password entered does not match with password entered!')
                return render(
                    request,
                        'app/GeneralUserRegister.html',
                        {
                            'generalUserRegForm':f,
                            'year':datetime.now().year,
                        }
                    )             
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
                    if (f.cleaned_data.get('Premium_User_Password') == f.cleaned_data.get('Premium_User_Password_Confirm')):
                        userName = f.cleaned_data.get('Premium_User_Name')
                        password = f.cleaned_data.get('Premium_User_Password')                     
                        email = f.cleaned_data.get('Email')
                        StoreName =  f.cleaned_data.get('Store_Name')
                        Address = f.cleaned_data.get('Address')
                        Zip = f.cleaned_data.get('Zip')
                        Phone = f.cleaned_data.get('Phone')
                         #Encode password
                        bPassword = password.encode()
                        ePassword = hashlib.sha512()
                        ePassword.update(bPassword)
                        encryptedPassword = ePassword.digest()                
                        try:
                            global premiumUserID
                            premiumUserID +=1
                            premiumUser = Premium_User.objects.create(Premium_User_ID = premiumUserID, Premium_User_Name = userName,Premium_User_Password = encryptedPassword,
                                                                      Email = email, Store_Name = StoreName,Store_Address = Address, Store_Zip = Zip, Store_Phone = Phone)
                        except: # catch *all* exceptions
                            messages.error(request,  sys.exc_info()[0])
                            return render(
                                request,
                                    'app/PremiumUserRegister.html',
                                    {
                                        'premiumUserRegForm':f,
                                        'year':datetime.now().year,
                                    }
                                )
                        messages.success(request, 'Premium User successfully created and logged in!')
                        return render(                    
                                    request,
                                    'app/PremiumUserDashboard.html',
                                    {
                                        'title':'Premium User Dashboard',
                                        'year':datetime.now().year,
                                    }
                                )
                    else:
                        messages.error(request, 'Confirm password entered does not match with password entered!')
                        return render(
                            request,
                                'app/PremiumUserRegister.html',
                                {
                                    'premiumUserRegForm':f,
                                    'year':datetime.now().year,
                                }
                            )               
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
            passWord = f.cleaned_data.get('User_Password') 
            ##Encode password
            #bPassword = password.encode()
            #ePassword = hashlib.sha512()
            #ePassword.update(bPassword)
            #encryptedPassword = ePassword.digest()  
            #TODO: Add checking condition if it is Premium user or General user login.
            try:
                #genUser = General_User.objects.filter(General_User_Name = userName,General_User_Password = encryptedPassword)
                #if genUser:
                #    messages.success(request, 'General User successfully logged in!')
                #    return HttpResponseRedirect('/')
                genAuthUser = authenticate(username = userName,password = passWord)
                if genAuthUser:
                    messages.success(request, 'General User successfully logged in!')
                    return HttpResponseRedirect('/')
                else:
                    #If Premium User Login go to PremiumUserDashboard.html
                    try:
                        premUser = Premium_User.objects.filter(Premium_User_Name = userName, Premium_User_Password = encryptedPassword)
                        if premUser:
                            messages.success(request, 'User successfully logged in!')
                            return HttpResponseRedirect('PremiumUserDashboard.html')#TODO: Search page or update information page
                        else:
                            messages.success(request, 'User not found')
                            return HttpResponseRedirect('login.html')
            
                    except:
                        messages.error(request,  sys.exc_info()[0])
                        return HttpResponseRedirect('login.html')
                           
            except:
                messages.error(request,  sys.exc_info()[0])
                return HttpResponseRedirect('login.html')
            
        else:
            return render(
                        request,
                        'app/login.html',
                        {
                            'LoginErrorMessage':'User name and password does not match!',
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
                        'LoginErrorMessage':'',
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

def PremiumDashboardLogedIn(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/PremiumUserDashboard.html',
        {
            'title':'Premium User Dashboard',
            'year':datetime.now().year,
        }
    )

def PremiumUserUpdateInventory(request):
    assert isinstance(request, HttpRequest)
    
    Inventory_FormSet = formset_factory(InventoryForm)

    if request.method == 'POST':
        childrenFormset = Inventory_FormSet(request.POST)

        # check whether it's valid:
        if childrenFormset.is_valid():
            childrenFormset.save()

            # redirect to the edit url (eventually will be to the view URL)
            return HttpResponseRedirect('PremiumUserUpdateInventory.html')
        else:
             print (childrenFormset.errors)

    # if a GET 
    else:
        childrenFormset = Inventory_FormSet()
        

    return render(request, 'app/PremiumUserUpdateInventory.html', 
        { 
            'InventoryFormSet' : childrenFormset, 
            'year' : datetime.now().year, 
            'title': "Add/Edit Inventory Items"
            })

def PremiumUserPublishAD(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':  
                f = publishAdvertisementForm(request.POST)
                if f.is_valid():     
                    Subject = f.cleaned_data.get('AD_Subject')
                    File = f.cleaned_data.get('AD_Content') 
                    return HttpResponseRedirect('PremiumUserPublishAD.html')#TODO: Search page or update information page
                else:
                    return render(
                                request,
                                'app/PremiumUserPublishAD.html',
                                {
                                    'publishAdvertisementForm':f,
                                    'year':datetime.now().year
                                }
                            )          
    else:
        f = publishAdvertisementForm()
        return render(
                    request,
                    'app/PremiumUserPublishAD.html',
                    {
                        'publishAdvertisementForm':f,
                        'year':datetime.now().year
                    }
                )