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
from django.contrib.auth import authenticate,login
#Import user group lib
from django.contrib.auth.models import Permission,Group

#Hash lib import
import hashlib
#Import models py
from app.models import *
#Import all the forms
from app.forms import *
#Import message lib
from django.contrib import messages
#Import file related lib
from django.core.files.storage import FileSystemStorage
#Import datetime
from datetime import datetime
#Import email
from django.core.mail import EmailMessage
from django.http import BadHeaderError


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
                passWord = f.cleaned_data.get('General_User_Password')               
                email = f.cleaned_data.get('Email')             
                try:
                    genUser = General_User.objects.create(General_User_Name = userName, Email = email)
                    genAuthUser = User.objects.create_user(userName,email, passWord)
                    group = Group.objects.get(name='generalUser')
                    genAuthUser.groups.add(group)
                    genAuthUser.save()
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
                    AuthUser = authenticate(username = userName,password = passWord)
                    login(request,AuthUser) 
                    messages.success(request, 'User successfully created and logged in!')
                    return HttpResponseRedirect('/')        
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
                passWord = f.cleaned_data.get('Premium_User_Password')                     
                email = f.cleaned_data.get('Email')
                StoreName =  f.cleaned_data.get('Store_Name')
                Address = f.cleaned_data.get('Address')
                Zip = f.cleaned_data.get('Zip')
                Phone = f.cleaned_data.get('Phone')                                   
                try:
                    premUser = Premium_User.objects.create(Premium_User_Name = userName,
                                                                Email = email, Store_Name = StoreName,Store_Address = Address, Store_Zip = Zip, Store_Phone = Phone)
                    premAuthUser = User.objects.create_user(userName,email, passWord);
                    group = Group.objects.get(name='premiumUser')
                    premAuthUser.groups.add(group)
                    premAuthUser.save()
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

                AuthUser = authenticate(username = userName,password = passWord)
                login(request,AuthUser)
                messages.success(request, 'Premium User successfully created and logged in!')
                return HttpResponseRedirect('app/PremiumUserDashboard.html')               
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
            request.session.get_expire_at_browser_close()
            try:               
                AuthUser = authenticate(username = userName,password = passWord)
                if AuthUser:
                    login(request,AuthUser)

                    #Check which group the user belongs to
                    user_in_GeneralGroup = Group.objects.get(name='generalUser').user_set.all()
                    user_in_PremiumGroup = Group.objects.get(name='premiumUser').user_set.all()

                    if AuthUser in user_in_GeneralGroup:
                        messages.success(request, 'General User successfully logged in!')
                        return HttpResponseRedirect('/')
                    elif AuthUser in user_in_PremiumGroup:                       
                        messages.success(request, 'Premium User successfully logged in!')
                        return HttpResponseRedirect('PremiumUserDashboard.html')#TODO: Search page or update information page
                else:
                    messages.error(request, 'User not found!')
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
            Qurery_Results = Premium_User.objects.filter(Store_Zip = zip)

            if Qurery_Results:
                return render(
                            request,
                            'app/searchForStores.html',
                            {
                                'searchForStoreForm':f,
                                'query_results':Qurery_Results,
                                'year':datetime.now().year
                            }
                        )  
            else:
                messages.error(request,  "No Store found!") 
                return render(
                        request,
                        'app/searchForStores.html',
                        {
                            'searchForStoreForm':f,
                            'year':datetime.now().year
                        }
                    )
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

            if Product.objects.filter(Product_Name = product_name).exists():
                product_item = Product.objects.get(Product_Name = product_name)
                Qurery_Results = Product_List.objects.filter(product = product_item)

                if Qurery_Results:
                    return render(
                                request,
                                'app/searchForProduct.html',
                                {
                                    'searchForProductForm':f,
                                    'query_results':Qurery_Results,
                                    'year':datetime.now().year
                                }
                            )  
                else:
                    messages.error(request,  "No Product found!") 
                    return render(
                            request,
                            'app/searchForProduct.html',
                            {
                                'searchForProductForm':f,
                                'year':datetime.now().year
                            }
                        ) 
            else:
                    messages.error(request,  "No Product found!") 
                    return render(
                            request,
                            'app/searchForProduct.html',
                            {
                                'searchForProductForm':f,
                                'year':datetime.now().year
                            }
                        )
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
    user_in_PremiumGroup = Group.objects.get(name='premiumUser').user_set.all()
    AuthUser = request.user

    if AuthUser in user_in_PremiumGroup:
        if request.method == 'POST':
            childrenFormset = Inventory_FormSet(request.POST)
        
            # check whether it's valid:
            if childrenFormset.is_valid():
                #Populate the formset into database
                for form in childrenFormset:
                    premium_User = Premium_User.objects.get(Premium_User_Name = request.user.username, Email = request.user.email)
                    Name =  form.cleaned_data.get('Item_Name') 
                    Quantity = form.cleaned_data.get('Item_Quantity') 
                    Price = form.cleaned_data.get('Item_Price')
                    try:                    
                        #Create the product item if it was not there
                        if Product.objects.filter(Product_Name = Name).exists():
                            product_item = Product.objects.get(Product_Name = Name)
                        else:
                            product_item = Product.objects.create(Product_Name = Name)

                        #Create the product list if it was not there
                        if Product_List.objects.filter(premium_user = premium_User, product = product_item).exists():
                            productList_item = Product_List.objects.get(premium_user = premium_User, product = product_item)
                            productList_item.quantity = Quantity
                            productList_item.price = Price
                            productList_item.save()
                        else:
                            productList_item = Product_List.objects.create(premium_user = premium_User, product = product_item,quantity = Quantity, price = Price)
                   
                    except: # catch *all* exceptions
                        messages.error(request,  sys.exc_info()[0])
                        return render(request, 'app/PremiumUserUpdateInventory.html', 
                                        { 
                                            'InventoryFormSet' : childrenFormset, 
                                            'year' : datetime.now().year, 
                                            'title': "Add/Edit Inventory Items"
                                            })
                messages.success(request,  "Inventory successfully updated!")
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
    else:
        messages.error(request, 'Not permitted!')
        return HttpResponseRedirect('/')

def PremiumUserPublishAD(request):
    assert isinstance(request, HttpRequest)
    user_in_PremiumGroup = Group.objects.get(name='premiumUser').user_set.all()
    AuthUser = request.user

    if AuthUser in user_in_PremiumGroup:
        if request.method == 'GET':
            f = publishAdvertisementForm
            return render(
                        request,
                        'app/PremiumUserPublishAD.html',
                        {
                            'publishAdvertisementForm':f,
                            'year':datetime.now().year
                        }
                    )
        else: #POST
            f = publishAdvertisementForm(request.POST, request.FILES)
            if f.is_valid():     
                Subject = f.cleaned_data.get('AD_Subject')            
                File = f.cleaned_data.get('AD_Content')             

                if Product.objects.filter(Product_Name = Subject).exists():
                    premium_User = Premium_User.objects.get(Premium_User_Name = request.user.username, Email = request.user.email)
                    Ad_product = Product.objects.get(Product_Name = Subject)
                    bytes=File.read() #read binary
                    #Upload poster to the database
                    myAdvertisement = Advertisement.objects.create(product = Ad_product, advertisement_concent = bytes, mime_Type = File.content_type,time_of_post = datetime.utcnow()) 
                    myAdvertisement.save()
                    Advertisement_List.objects.create(advertisement = myAdvertisement, premium_user = premium_User)

                    #Send advertisement to general user as email
                    subject = 'MyGrocery Advertisement'
                    message = 'Special Today : ' + Subject 
                    from_email = 'MyGrocery@iastate.com'
                    recipient_list = [] 

                    user_in_GeneralGroup = Group.objects.get(name='generalUser').user_set.all()
                    for receiver in user_in_GeneralGroup:                               
                        recipient_list.append(receiver.email) 
                               
                    email = EmailMessage(subject,message,from_email,bcc = recipient_list)
                    email.attach(File.name,bytes,File.content_type)
                    email.send()
                    
                    messages.success(request,  "Advertisement successfully published!")                     
                    return render(
                                request,
                                'app/PremiumUserPublishAD.html',
                                {
                                    'publishAdvertisementForm':f,
                                    'year':datetime.now().year
                                }
                            )
                else:
                    messages.error(request,  "Item not found in the inventory, add this item first!")                     
                    return render(
                                request,
                                'app/PremiumUserPublishAD.html',
                                {
                                    'publishAdvertisementForm':f,
                                    'year':datetime.now().year
                                }
                            )
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
        messages.error(request, 'Not permitted!')
        return HttpResponseRedirect('/')     
    