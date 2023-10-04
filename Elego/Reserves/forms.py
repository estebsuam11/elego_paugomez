from django import forms
from .models import Reserve

class ReserveCreateForm(forms.ModelForm):
    class Meta:
        model=Reserve
        fields=('fullname','address', 'phone', 'zip_code', 'service', 'date', 'number_hour', 'start_time', 'pets', 'pet_number')