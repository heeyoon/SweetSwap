from mysite.models import UserProfile
from django.contrib.auth.models import User
from mysite.models import UserUpdate, SelectCountry
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('street_address', 'city', 'state', 'country', 'zipcode', 'country_requested', 'about')



class UserUpdateForm(forms.ModelForm):
	new_password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = UserUpdate
        fields = ('first_name', 'last_name', 'new_password', 'confirm_password', 'email')



class SelectCountryForm(forms.ModelForm):
	class Meta:
		model = SelectCountry
		fields = ('add_country',)