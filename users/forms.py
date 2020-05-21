from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Обязательное поле', label='Электронная почта')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



    def is_valid(self):
        if User.objects.filter(email=self.data.get('email')).count() != 0:
            self.add_error('email', 'Данный адрес электронной почты уже используется')
        return super(CustomUserCreationForm, self).is_valid()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Обязательное поле', label='Электронная почта')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','id')

    def is_valid(self):
        return super(UserEditForm, self).is_valid()

    def email_is_valid(self,id):
        # TODO:как-то достать значение из id и проверить мыло
        user=User.objects.get(username=id)
        if self.data.get('email') == user.email:
            return True
        else:
            if User.objects.filter(email=self.data.get('email')).count() != 0:
                self.add_error('email', 'Данный адрес электронной почты уже используется')
                return False
            else:
                return True
