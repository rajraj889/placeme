from django.shortcuts import render
import warnings
from django.contrib.auth import logout
from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
#from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
#from django.utils.deprecation import RemovedInDjango110Warning
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


from django.views import generic
from .models import Post,company,study
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import company_added,exp_added,study_exp
from django.contrib.auth.models import User

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'placement.html'
    
class stuy(generic.ListView):
    queryset = study.objects.filter(status=1).order_by('-created_on')
    template_name = 'study.html'
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class studydetail(generic.DetailView):
    model = study
    template_name = 'study_detail.html'

class view_company(generic.ListView):
    #model=company
    queryset = company.objects.filter(status=1).order_by('-created_on')
    #print(queryset)
    template_name = 'company_added.html'

#def company_add(request):
#    return render(request,'company_added.html',{'view_company':view_company})

def add_company(request):
    form=company_added()
    if request.method == 'POST':
        form = company_added(request.POST)
        if form.is_valid():
            form.save(commit=True)

            print(form.cleaned_data)
            #return company_add(request)
            return HttpResponseRedirect('company_add')
    return render(request,'add_company.html',{'form':form })

def study_e(request):
    f=study_exp()
    if request.method == 'POST':
        f = study_exp(request.POST)
        if f.is_valid():
            f.save(commit=True)

            print(f.cleaned_data)
            #return company_add(request)
            return HttpResponseRedirect('study')
    return render(request,'study_exp.html',{'f':f })

def add_exp(request):
    fo=exp_added()
    if request.method == 'POST':
        fo = exp_added(request.POST)
        if fo.is_valid():
            fo.save(commit=True)

            print(fo.cleaned_data)
            #return company_add(request)
            return HttpResponseRedirect('placement')
    return render(request,'exp.html',{'form':fo })

def log(request):
	logout(request)
	return HttpResponseRedirect('/')

def profile(request):
	return render(request, 'profile.html')

def home(request):
	return render(request, 'home.html')

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

