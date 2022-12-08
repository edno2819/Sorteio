from django.shortcuts import render
from card.models import Card
import random

def home(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('sorteio'):
            cards = list(Card.objects.all())
            cards_qtd = [card.quantidade for card in cards]

            choise = random.choices(
                population=cards,
                weights=cards_qtd,
                k=1
            )[0]
            return render(request, 'home.html', context = {'choise':choise, 'negative': choise.quantidade * -1})

        if request.POST.get('id'):
            id = int(request.POST.get('id'))
            qtd = int(request.POST.get('qtd'))
            print(request.POST.get('qtd'))
            cards = Card.objects.filter(id=id)[0]
            new_value = cards.quantidade + qtd
            cards.quantidade =  new_value if new_value>=0 else 0
            cards.save()


    return render(request, 'home.html')
