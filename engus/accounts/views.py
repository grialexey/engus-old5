from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from .forms import CustomUserCreationForm
from .models import Invite


@csrf_protect
@never_cache
def register(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                username = form.clean_username()
                password = form.clean_password2()
                user = form.save()
                invite = Invite.objects.get(code=form.cleaned_data['invite_code'])
                invite.registered_user = user
                invite.save()
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user is not None and authenticated_user.is_active:
                    login(request, authenticated_user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            form = CustomUserCreationForm()
        return render_to_response('registration/register.html', {'form': form, },
                                  context_instance=RequestContext(request))
