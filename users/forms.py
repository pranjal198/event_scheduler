from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    DEP_CHOICE =(
    ("0", "select"),
    ("Computer Science and Engineering","Computer Science and Engineering"),
    ("Biosciences and Bioengineering","Biosciences and Bioengineering"),
    ("Chemical Engineering","Chemical Engineering"),
    ("Civil Engineering","Civil Engineering"),
    ("Chemistry","Chemistry"),
    ("Design","Design"),
    ("Electronics and Electrical Engineering","Electronics and Electrical Engineering"),
    ("Mechanical Engineering","Mechanical Engineering"),
    ("Electronics and Communications Engineering","Electronics and Communications Engineering"),
    ("Mathematics and Computing","Mathematics and Computing"),
    ("Engineering Physics","Engineering Physics"),
    ("Humanities and Social Sciences","Humanities and Social Sciences"),
    )

    SEM_CHOICE = (
    ("0", "select"),
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    )
    name = forms.CharField(max_length=50)
    roll = forms.IntegerField()
    semester = forms.ChoiceField(choices = SEM_CHOICE)
    department = forms.ChoiceField(choices = DEP_CHOICE)

    class Meta:
        model = Profile
        fields = ['name','roll','semester','department']

