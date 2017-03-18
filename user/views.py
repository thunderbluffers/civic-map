from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import RegisterForm
from django.contrib.auth import views as auth_views


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
            else:
                # No backend authenticated the credentials
                pass

            return render(request, 'registration/register_success.html')
        else:
            context = {'form': form}
            return render(request, 'registration/register.html', context)
    else:
        form = RegisterForm()

        context = {'form': form}
        return render(request, 'registration/register.html', context)
