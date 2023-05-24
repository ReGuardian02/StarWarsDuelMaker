from django.db import models


class Group(models.Model):
    name = models.TextField(max_length=50, verbose_name="Фракция/группировка")
    points = models.SmallIntegerField
    def __str__(self):
        return self.name

class Duelist(models.Model):
    name = models.TextField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Duel(models.Model):
    duelist1 = models.TextField(verbose_name="Дуэлянт №1", max_length=50, blank=True)
    duelist2 = models.TextField(verbose_name="Дуэлянт №2", max_length=50, blank=True)
    result = models.TextField(verbose_name="Исход дуэли")
