from django.forms import ModelForm
from .dynamic_models import dva, odin, common


class dvaForm(ModelForm):
	class Meta:
		model = dva
		fields = ('rektorFio', 'table_smetaStudenta', 'kol_chel', 'table_spisokDolznostnixSmeta')


class odinForm(ModelForm):
	class Meta:
		model = odin
		fields = ('glavbyxFio', 'table_spisokStudentov', 'preambula', 'mesto_naznacheniya', 'ioFrektor', 'kompensaciya', 'stringPrikaz', 'forma_obucheniya', 'osnova_obucheniya')


class commonForm(ModelForm):
	class Meta:
		model = common
		fields = ('nazvanie_meropriyatie', 'daystart', 'dayend', 'dolzn_podrazd', 'ioFglavnyi')


