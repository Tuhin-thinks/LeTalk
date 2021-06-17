from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'mail', 'placeholder':'Email Address'}), )
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'uname'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = ''

		self.fields['password1'].widget.attrs['class'] = 'pass'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = ''

		self.fields['password2'].widget.attrs['class'] = 'spass'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = ''

# class SignUpForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Username'}))
#     conUsername = forms.CharField(label='Confirm Username', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Username'}))
#     firstName = forms.CharField(label='First Name', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Firstname'}))
#     lastName = forms.CharField(label='Last Name', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter LastName'}))
#     email = forms.CharField(label='Email', max_length=220,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email','type':'email'}))
#     conEmail = forms.CharField(label='Confirm Email', max_length=220,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Email','type':'email'}))
#     password = forms.CharField(label="Confirm Password", max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','type':'password','placeholder':'Enter Password'}))
#     conPassword = forms.CharField(label="Confirm Password", max_length=20,widget=forms.TextInput(attrs={'class': 'form-control','type':'password','placeholder':'Confirm Password'}))