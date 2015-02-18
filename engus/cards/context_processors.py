from .models import Card


def cards_to_repeat_count(request):
    cards_count = 0
    if request.user.is_authenticated():
        cards_count = Card.objects.filter(user=request.user).to_repeat().count()
    return {
        'cards_to_repeat_count': cards_count,
        'card_repeat_modes': ['repeat-right', 'repeat-left', ]
    }