from django.test import TestCase, SimpleTestCase
from .models import Group, Duelist, Duel
from .views import *
from django.urls import resolve, reverse

class TestSuperCases(TestCase):
    
    def test_duel_creation(self):
        new_players = ['player one', 'player two']
        new_groups = ['group 1', 'group 2']

        for group in new_groups:
            Group.objects.create(name=group)

        i = 0
        players_list = []
        for player in new_players:
            players_list.append(Duelist.objects.create(name=player, group=new_groups[i]))
            i += 1
        
        self.assertEqual(len(new_players), len(players_list))
        whoIsWinner(players_list)

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)