from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Tovar, User


class TovarCreateForm(forms.ModelForm):
    name = forms.CharField(label='Название товара', widget=forms.TextInput, required=True)
    information = forms.CharField(label='Информация о товаре (описание)', widget=forms.Textarea, required=True)
    price = forms.DecimalField(label='Стоимость товара', widget=forms.NumberInput, max_digits=10, decimal_places=2, required=True)
    tovar_photo = forms.ImageField(label='Изображение товара', required=True)

    class Meta:
        model = Tovar
        fields = ('name', 'information', 'price', 'tovar_photo')


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput, required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )