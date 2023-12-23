from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .forms import TovarCreateForm, SignUpForm
from .models import Tovar


def index(request):
    tovar_list = Tovar.objects.all()
    return render(request, 'index.html', {'tovar_list': tovar_list})


def about(request):
    return render(request, 'about_us.html')


def contacts(request):
    return render(request, 'kontakt.html')


def products(request):
    product_list = Tovar.objects.all()
    return render(request, 'tovar.html', {'product_list': product_list})


class LoginServerView(LoginView):
    template_name = 'registration/login.html'


class LogoutServerView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logged_out.html'


class TovarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tovar
    form_class = TovarCreateForm
    template_name = 'create_product.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()

        return redirect('products')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect("/catalog")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})