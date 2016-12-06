"""
Definition of forms.
"""

from django import forms
from django.forms.formsets import BaseFormSet
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class generalUserRegForm(forms.Form):
    General_User_Name = forms.CharField(label = 'User Name', max_length = 10,widget=forms.TextInput({'class': 'form-control'}))
    General_User_Password = forms.CharField(label = 'Password', max_length = 20 , widget=forms.PasswordInput({'class': 'form-control','placeholder':'Password'}))
    General_User_Password_Confirm = forms.CharField(label = 'Confirm Password', max_length = 20, widget=forms.PasswordInput({'class': 'form-control','placeholder':'Password'}))
    Email = forms.EmailField(label = 'E-Mail',widget=forms.EmailInput({'class': 'form-control'}))

class premiumUserRegForm(forms.Form):
    Premium_User_Name = forms.CharField(label = 'User Name', max_length = 10,widget=forms.TextInput({'class': 'form-control'}))
    Premium_User_Password = forms.CharField(label = 'Password', max_length = 20, widget=forms.PasswordInput({'class': 'form-control','placeholder':'Password'}))
    Premium_User_Password_Confirm = forms.CharField(label = 'Confirm Password', max_length = 20, widget=forms.PasswordInput({'class': 'form-control','placeholder':'Password'}))
    Email = forms.EmailField(label = 'E-Mail', widget=forms.EmailInput({'class': 'form-control'}))
    Store_Name = forms.CharField(label = 'Store Name', max_length = 10,widget=forms.TextInput({'class': 'form-control'}))
    Address = forms.CharField(label = 'Store Address', widget=forms.TextInput({'class': 'form-control'}))
    Zip = forms.CharField(label = 'Zip', max_length = 11, widget=forms.TextInput({'class': 'form-control'}))
    Phone = forms.CharField(label = 'Phone Num', max_length = 10, widget=forms.TextInput({'class': 'form-control','placeholder':'555-555-5555'}))

class userLoginForm(forms.Form):
    User_Name = forms.CharField(label = 'User Name', max_length = 10,widget=forms.TextInput({'class': 'form-control'}))
    User_Password = forms.CharField(label = 'Password', max_length = 20, widget=forms.PasswordInput({'class': 'form-control','placeholder':'Password'}))

class searchForStoreForm(forms.Form):
    Search_Zip = forms.CharField(label = 'Zip Code', max_length = 11,widget=forms.TextInput({'class': 'form-control'})
)
class searchForProductForm(forms.Form):
    Product_Name = forms.CharField(label = 'Product Name', max_length = 10, widget=forms.TextInput({'class': 'form-control'}))

class publishAdvertisementForm(forms.Form):
    AD_Subject = forms.CharField(label = 'Product Name', max_length = 10, widget=forms.TextInput({'class': 'form-control'}))
    AD_Content = forms.FileField(label = 'Upload Poster', widget=forms.FileInput({'class': 'form-control'}))


class InventoryForm(forms.Form):
    Item_Name = forms.CharField(label = 'Product Name', max_length = 10)
    Item_Price = forms.DecimalField(label = 'Product Price', decimal_places = 2, max_digits = 5)
    Item_Quantity = forms.IntegerField(label = 'Product Quantity')




    
         