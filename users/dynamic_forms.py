from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, Prikaz, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


class NapravlenieStudentaForm(ModelForm):
	name='НаправлениеСтудента'
	naselennyj_punkt=forms.CharField(label="Населенный пункт",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	class Meta:
		model = NapravlenieStudenta
		fields = ('yf', 'ys', 'iofglavnyi_st', 'cel_poezdki', 'ds', 'gruppa', 'df', 'ms', 'mf', 'fiofull', 'dolzn_podrazd_st',)

		labels = {
			'yf':_('Год прибытия'),
			'ys':_('Год отправления'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'cel_poezdki':_('Цель поездки'),
			'ds':_('День отправления'),
			'gruppa':_('Студенческая группа'),
			'df':_('День прибытия'),
			'ms':_('Месяц отправления'),
			'mf':_('Месяц прибытия'),
			'fiofull':_('ФИО обучающегося'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
		}
		help_texts = {
			'yf':_('Подсказка:'),
			'ys':_('Подсказка:'),
			'iofglavnyi_st':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'df':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'mf':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
			'dolzn_podrazd_st':_('Подсказка:'),
		}
class PrikazForm(ModelForm):
	name='Приказ'
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	daystart=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата отбытия",help_text="Подсказка:")
	dayend=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата прибытия",help_text="Подсказка:")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	class Meta:
		model = Prikaz
		fields = ('preambula', 'table_spisokdolznostnixprikaz', 'stringprikaz', 'glavbyxfio',)

		labels = {
			'preambula':_('Преамбула'),
			'table_spisokdolznostnixprikaz':_(''),
			'stringprikaz':_('Текст приказа'),
			'glavbyxfio':_('ФИО Главного бухгалтера'),
		}
		help_texts = {
			'preambula':_('Подсказка:Вводная часть'),
			'table_spisokdolznostnixprikaz':_('Подсказка:'),
			'stringprikaz':_('Подсказка:'),
			'glavbyxfio':_('Подсказка:'),
		}
class SluzhebnajaZapiskaForm(ModelForm):
	name='СлужебнаяЗаписка'
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	daystart=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата отбытия",help_text="Подсказка:")
	dayend=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата прибытия",help_text="Подсказка:")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	class Meta:
		model = SluzhebnajaZapiska
		fields = ('podrazdelenie',)

		labels = {
			'podrazdelenie':_('Название подразделения'),
		}
		help_texts = {
			'podrazdelenie':_('Подсказка:'),
		}
class SmetaForm(ModelForm):
	name='Смета'
	class Meta:
		model = Smeta
		fields = ('table_spisokdolznostnixsmeta', 'kol_chel', 'table_smetastudenta', 'rektorfio',)

		labels = {
			'table_spisokdolznostnixsmeta':_(''),
			'kol_chel':_('Количество командируемых лиц'),
			'table_smetastudenta':_(''),
			'rektorfio':_('ФИО Ректора'),
		}
		help_texts = {
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
			'kol_chel':_('Подсказка:'),
			'table_smetastudenta':_('Подсказка:'),
			'rektorfio':_('Подсказка:'),
		}
class OtchetStudentaForm(ModelForm):
	name='ОтчетСтудента'
	class Meta:
		model = OtchetStudenta
		fields = ('this_start', 'fioshort',)

		labels = {
			'this_start':_(''),
			'fioshort':_('ФИО сокращенно'),
		}
		help_texts = {
			'this_start':_('Подсказка:'),
			'fioshort':_('Подсказка:Полностью фамилию и инициалы'),
		}
