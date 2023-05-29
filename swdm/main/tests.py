from django.test import TestCase, SimpleTestCase
from .models import Group, Duelist, Duel
from .views import *
from django.urls import resolve, reverse

class TestSuperCases(TestCase):

    #тест создания новой фракции в базе данных
    def test_group_creation(self):
        #создаем массив с 2 именами фракций
        new_groups = ['group 1', 'group 2']
        #создаем объекты фракций в бд
        for group in new_groups:
            Group.objects.create(name=group)

        #проверяем, что количество созданных в бд объектов равно количеству создаваемых в предыдущем шаге
        self.assertEqual(Group.objects.all().count(), len(new_groups), "Created groups are not the same as meant to be") 
    
    #тест создания нового дуэлянта в базе данных
    def test_duelist_creation(self):
        #создаем массив с 2 именами фракций
        new_groups = ['group 1', 'group 2']
        #создаем объекты фракций в бд
        for group in new_groups:
            Group.objects.create(name=group)
        #получаем все созданные фракции
        all_groups = Group.objects.all()
        
        #создаем массив с 2 именами дуэлянтов
        new_duelists = ['duelist 1', 'duelist 2']
        #создаем объекты дуэлянтов в бд
        for i in range(2):
            Duelist.objects.create(name=new_duelists[i], group=all_groups[i])

        #проверяем, что количество созданных в бд объектов (дуэлянтов) равно количеству создаваемых в предыдущем шаге
        self.assertEqual(Duelist.objects.all().count(), len(new_duelists), "Created duelists are not the same as meant to be") 
    
    #тест проведения дуэли
    def test_duel_creation(self):
        #создаем массив с именами фракций
        new_groups = ['group 1', 'group 2']
        #создаем объекты фракций в бд
        for group in new_groups:
            Group.objects.create(name=group)
        #получаем все созданные фракции
        all_groups = Group.objects.all()
        
        #создаем массив с 2 именами дуэлянтов
        new_duelists = ['duelist 1', 'duelist 2']
        #создаем объекты дуэлянтов в бд
        for i in range(2):
            Duelist.objects.create(name=new_duelists[i], group=all_groups[i])
        all_duelists = Duelist.objects.all()

        #создаем пустой массив, в который помещаем имена созданных дуэлянтов
        players_list = []
        for i in all_duelists:
            players_list.append(i.name)

        #выводим результат views функции, которая решает исход дуэли
        print(whoIsWinner(players_list))

    #тест соответствия URLs
    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)