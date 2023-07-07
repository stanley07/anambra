# building/forms.py

from django import forms
from .models import Building

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ('owner_name', 'address', 'building_type', 'amount_value', 'contact', 'ansidd_no', 'image')
