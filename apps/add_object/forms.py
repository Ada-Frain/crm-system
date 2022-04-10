from django import forms
from django.utils.text import slugify
from apps.core.models import Project

class ProjectCreateForm(forms.ModelForm):
    # slug = forms.CharField(widget=forms.TextInput(attrs={slugify('name', allow_unicode=True) :'number_out'}))
    class Meta:
        model = Project
        fields = ['name', 'slug', 'contract_number', 'brand', 'contractor', 'contractor_contract', 'advance_payment1',
                'advance_payment2', 'advance_payment3', 'final_sum', 'cs_upd', 'adress', 'contacts', 'engineer', 'status']