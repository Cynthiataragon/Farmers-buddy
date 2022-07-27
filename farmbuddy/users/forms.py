from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Dataset


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


#definition for thr homepage 
class DataSet(Dataset):

    location = models.CharField(max_length= 200)
	soil = models.CharField(max_length= 200)
	weather = models.CharField(max_length= 200)
	crop = models.CharField(max_length= 200)

    class Meta:
        model = DataSet
        Dataset = ['location', 'soil', 'weather', 'crop']