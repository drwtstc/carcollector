from django.forms import ModelForm
from .models import Maint

class MaintForm(ModelForm):
  class Meta:
    model = Maint
    fields = ['date', 'service']