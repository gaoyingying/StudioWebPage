from django import forms
from models import UserProfile, Category, Page
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'subtitle')


class PostForm(forms.ModelForm):
    name = forms.CharField()
    content = forms.Textarea()

    class Meta:
        model = Page
        fields = ('name', 'content', 'category',)
