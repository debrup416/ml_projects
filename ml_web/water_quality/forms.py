from django.forms import ModelForm, fields
from .models import Water

class WaterForm(ModelForm):
    class Meta:
        model=Water
        fields= '__all__'
        
