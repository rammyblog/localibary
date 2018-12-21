import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, AuthorComment



class RenewalForm(forms.Form):
	renewal_date = forms.DateField(
		widget = forms.TextInput(attrs = {'class':"form-control add-listing_form"}),


		help_text = 'Default is 4 Weeks')

	def renewal_date_clean_data(self):
		data = self.cleaned_data['renewal_date']

		if data < datetime.date.today():
			raise ValidationError(_("The date inputed is in the PAST!"))

		if data > datetime.date.today + data.timedelta(weeks = 4):
			raise ValidationError(_("The date inputed is in above 4 weeks!"))

		return data


class Register(UserCreationForm):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
	name = forms.CharField(max_length= 4000, widget = forms.TextInput(attrs = {	'class':"form-control",
		 'placeholder':"Enter name",
		  'aria-label':"Name",
		   'aria-describedby':"add-btn"}))
	message = forms.CharField(max_length= 4000, widget = forms.TextInput(attrs = {'class':"your-rating-content", 'placeholder':"Enter Your Comments"}))

	class Meta:
		model = Comment
		fields=['name', 'message']

class AuthorCommentForm(forms.ModelForm):
	name = forms.CharField(max_length= 4000, widget = forms.TextInput(attrs = {	'class':"form-control",
		 'placeholder':"Enter name",
		  'aria-label':"Name",
		   'aria-describedby':"add-btn"}))
	message = forms.CharField(max_length= 4000, widget = forms.TextInput(attrs = {'class':"your-rating-content", 'placeholder':"Enter Your Comments"}))

	class Meta:
		model = AuthorComment
		fields=['name', 'message']