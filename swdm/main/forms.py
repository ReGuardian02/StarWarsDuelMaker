from django.forms import ModelForm
from .models import Duelist, Group, Duel

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class DuelistForm(ModelForm):
    class Meta:
        model = Duelist
        fields = '__all__'

class DuelForm(ModelForm):
    class Meta:
        model = Duel
        fields = '__all__'