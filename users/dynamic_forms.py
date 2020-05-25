from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, Prikaz, SluzhebnajaZapiska, Smeta, OtchetStudenta, common


class NapravlenieStudentaForm(ModelForm):
	name='НаправлениеСтудента'
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	naselennyj_punkt=forms.CharField(label="Населенный пункт",help_text="Подсказка:")
	class Meta:
		model = NapravlenieStudenta
		fields = ('dolzn_podrazd_st', 'cel_poezdki', 'ds', 'fiofull', 'iofglavnyi_st', 'df', 'ms', 'mf', 'gruppa', 'yf', 'ys',)

		labels = {
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'cel_poezdki':_('Цель поездки'),
			'ds':_('День отправления'),
			'fiofull':_('ФИО обучающегося'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'df':_('День прибытия'),
			'ms':_('Месяц отправления'),
			'mf':_('Месяц прибытия'),
			'gruppa':_('Студенческая группа'),
			'yf':_('Год прибытия'),
			'ys':_('Год отправления'),
		}
		help_texts = {
			'dolzn_podrazd_st':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
			'iofglavnyi_st':_('Подсказка:'),
			'df':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'mf':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'yf':_('Подсказка:'),
			'ys':_('Подсказка:'),
		}
class PrikazForm(ModelForm):
	name='Приказ'
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	daystart=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата отбытия",help_text="Подсказка:")
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	dayend=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата прибытия",help_text="Подсказка:")
	class Meta:
		model = Prikaz
		fields = ('stringprikaz', 'glavbyxfio', 'table_spisokdolznostnixprikaz', 'preambula',)

		labels = {
			'stringprikaz':_('Текст приказа'),
			'glavbyxfio':_('ФИО Главного бухгалтера'),
			'table_spisokdolznostnixprikaz':_(''),
			'preambula':_('Преамбула'),
		}
		help_texts = {
			'stringprikaz':_('Подсказка:'),
			'glavbyxfio':_('Подсказка:'),
			'table_spisokdolznostnixprikaz':_('Подсказка:'),
			'preambula':_('Подсказка:Вводная часть'),
		}
class SluzhebnajaZapiskaForm(ModelForm):
	name='СлужебнаяЗаписка'
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	daystart=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата отбытия",help_text="Подсказка:")
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	dayend=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата прибытия",help_text="Подсказка:")
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
