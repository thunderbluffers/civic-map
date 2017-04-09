from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from .forms import RegisterForm


def register(request):
    form = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create user account
            form.save()

            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            if user is not None:
                auth_views.login(request, user)

                return redirect('locations:index')
            else:
                return render(request, 'registration/register_success.html')
        else:
            context = {'form': form}
            return render(request, 'registration/register.html', context)
    else:
        form = RegisterForm()

        context = {'form': form}
        return render(request, 'registration/register.html', context)
