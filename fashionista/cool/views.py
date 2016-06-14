from django.shortcuts import render
from django.http import HttpResponse
# using generic view
from django.views import generic
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django.views.generic import View
from .models import Accounts
from .forms import ProfileForm


def index(request):
    return render(request, 'cool/index.html')

def yo(request):
    return render(request, 'cool/index.html')

def mypage(request, user_id):
    return render(request, 'cool/mypage.html', {'user_id': user_id} )


def voting(request):
    return render(request, 'cool/mypage.html',  )

def profile(request):
    return render(request, 'cool/mypage.html',  )

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'cool/index.html', context)

# create Accounts object
class AccountsCreate(CreateView):
    model = Accounts
    fields = ['name', 'mobile', 'photo', 'additional_info', 'contest_pic',]



# Login
class UserFormView(View):
    form_class = UserForm
    template_name = 'cool/accounts_form.html'

    # New user coming to the site, send him blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # form data processing
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned and normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()
            # registration complete

            # Login and redirect

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cool:mypage')

        return render(request, self.template_name, {'form': form})

