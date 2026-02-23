from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm         #basic user form we will extend its functionalities

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username' , 'password1' , 'password2'}  #in django pass1 -> password and pass2-> comfirm password
