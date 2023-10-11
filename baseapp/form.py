from django.forms import ModelForm, TextInput, Textarea, CharField, FileInput
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RoomForm(ModelForm):
    class Meta:
        model = RommModel
        fields = ['title','content','category']
        widgets = {
            'title': TextInput(attrs={
                'class':'inpt',
                'placeholder':'Title'
            }),
            'content': Textarea(attrs={
                'class': 'inpt',
                'placeholder': 'Content'
            }),

        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']
        widgets = {
            'cat_name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Creat category'
            })
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Username'
            }),
            'password': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Password',
                'type': 'password'
            })
        }

class CustumeUserForm(UserCreationForm):
    password1 = CharField(widget=TextInput(attrs={
        'class': 'inpt',
        'type': 'password',
        'placeholder': 'Enter your password'
    }))
    password2 = CharField(widget=TextInput(attrs={
        'class': 'inpt',
        'type': 'password',
        'placeholder': 'Confirm your password'
    }))
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'avatar',
                  'bio',
                  'email',
                  'password1',
                  'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Username'
            }),
            'first_name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'First name'
            }),
            'last_name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Last name'
            }),
            'bio': Textarea(attrs={
                'class': 'inpt',
                'placeholder': 'Bio'
            }),
            'email': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'E-mail'
            }),
        }

class MessageForm(ModelForm):
    class Meta:
        model =Messages
        fields = ['message']
        widgets = {
            'message': Textarea(attrs={
                'class': 'inpt',
                'placeholder': 'Send messages'
            })
        }

