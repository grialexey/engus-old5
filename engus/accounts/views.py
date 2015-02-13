from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.shortcuts import redirect, render_to_response
from django.views.generic.base import TemplateView
from django.template import RequestContext
from braces.views import LoginRequiredMixin
from engus.cards.models import Card
from .forms import CustomUserCreationForm
from .models import Invite


class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        all_cards_learning_by_user = Card.objects.filter(user=self.request.user).learning()
        card_to_repeat_by_user = Card.objects.filter(user=self.request.user).to_repeat()
        context['learned_cards_count'] = all_cards_learning_by_user.count() - card_to_repeat_by_user.count()
        context['most_difficult_cards'] = all_cards_learning_by_user.order_by('repeat_count')[:10]
        return context



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
