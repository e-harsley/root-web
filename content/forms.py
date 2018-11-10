from django import forms
from.models import Waybill

class WaybillForms(forms.ModelForm):

    class Meta:
        models = Waybill
        fields = ('name_of_goods','dispath_time','delivery_date','location','status')