from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import SignupForm


# Create your views here.
class SignupView(View):
    form_class = SignupForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created successfully')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


def index(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def profile(request):
    return render(request, 'main/profile.html')


def view_post(request):
    return render(request, 'main/view_post.html')
