from .models import Card


def cards_to_repeat_count(request):
    if request.user.is_authenticated():
        cards_count = Card.objects.filter(user=request.user).to_repeat().count()
    else:
        cards_count = 0
    return {
        'cards_to_repeat_count': cards_count,
        'card_repeat_modes': ['repeat-right', 'repeat-left', ]
    }