"""
Definition of forms.
"""

from django import forms
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
    General_User_Name = forms.CharField(label = 'User Name', max_length = 10)
    General_User_Password = forms.CharField(label = 'Password', max_length = 20)
    General_User_Password_Confirm = forms.CharField(label = 'Confirm Password', max_length = 20)
    Email = forms.EmailField(label = 'E-Mail')

class premiumUserRegForm(forms.Form):
    Premium_User_Name = forms.CharField(label = 'User Name', max_length = 10)
    Premium_User_Password = forms.CharField(label = 'Password', max_length = 20)
    Premium_User_Password_Confirm = forms.CharField(label = 'Confirm Password', max_length = 20)
    Email = forms.EmailField(label = 'E-Mail')
    Store_Name = forms.CharField(label = 'Store Name', max_length = 10)
    Address = forms.CharField(label = 'Store Address')
    Zip = forms.CharField(label = 'Zip', max_length = 11)
    Phone = forms.CharField(label = 'Phone Num', max_length = 10)

class userLoginForm(forms.Form):
    User_Name = forms.CharField(label = 'User Name', max_length = 10)
    User_Password = forms.CharField(label = 'Password', max_length = 20)

class searchForStoreForm(forms.Form):
    Search_Zip = forms.CharField(label = 'Zip Code', max_length = 11)

class searchForProductForm(forms.Form):
    Product_Name = forms.CharField(label = 'Product Name', max_length = 10)

class publishAdvertisementForm(forms.Form):
    AD_Subject = forms.CharField(label = 'Product Name', max_length = 10)
    AD_Content = forms.FileField()


class InventoryForm(forms.Form):
    Item_Name = forms.CharField(label = 'Product Name', max_length = 10)
    Item_Price = forms.DecimalField(label = 'Product Price', decimal_places = 2, max_digits = 5)
    Item_Quantity = forms.IntegerField(label = 'Product Quantity')

    
         