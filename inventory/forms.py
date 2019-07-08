from django import forms
#from django.forms import ModelForm


from .models import *



class LaptopForms(forms.ModelForm):
	class Meta:
		model=Laptop
		fields= ('Type','price','status','issues')


class DesktopForms(forms.ModelForm):
	class Meta:
		model=Desktop
		fields= ('Type','price','status','issues')


class MobileForms(forms.ModelForm):
	class Meta:
		model=Mobiles
		fields= ('Type','price','status','issues')