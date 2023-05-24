from django.shortcuts import render, redirect, get_object_or_404
from .forms import DuelistForm, GroupForm
from .models import Duel, Duelist, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random


def home(request):
    print(request.POST)
    winner = ''
    players = Duelist.objects.all()
    if request.method == "POST":
        if 'player1' in request.POST:
            two_duelists = [request.POST.get('player1'), request.POST.get('player2')]
            result = whoIsWinner(two_duelists)
            player1 = result[0][0]
            player2 = result[0][1]
            if player1 == player2:
                winner = 'Нужен второй дуэлянт'
            else:
                winner = result[1]
            duel = Duel.objects.create(duelist1 = player1, duelist2 = player2, result = winner)
            return render(request, "home.html", {'players':players, 'winner':winner})
        duelist = Duelist.objects.create(name=request.POST.get("name"), group=Group.objects.get(id=int(request.POST.get("group"))))
    return render(request, "home.html", {'players':players, 'winner':winner})

def whoIsWinner(two_duelists):
    coin = random.randrange(0, 3, 1)
    if coin == 0:
        return(two_duelists, two_duelists[0])
    elif coin == 1:
        return(two_duelists, two_duelists[1])
    else:
        return(two_duelists, "Ничья")
    
def result(request):
    games = Duel.objects.all()
    return render(request, 'result.html', {'games':games})