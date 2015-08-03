from django.forms import ModelForm, forms
from .models import User, Category, Products
import re


class PostModelForm(ModelForm):
    class Meta:
        model = User
        exclude = []


class EditUserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class AddProductModleForm(ModelForm):
    class Meta:
        model = Products
        exclude = []
        # fields = ['name', 'price']


class AddCategoryModelForm(ModelForm):
    class Meta:
        model = Category
        # exclude = []
        fields = ['name', 'description', 'user']

    def clean_name(self):
        name_data = self.cleaned_data['name']
        if (name_data[0].isupper()) and (re.findall(r'[0-9]+', name_data)):
            return name_data
        else:
            raise forms.ValidationError('First letter should be a capital and it must contain a number in it !')


class addProductBycatModelForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price']


## for login
# files.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Username"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
