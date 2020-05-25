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
		fields = ('iofglavnyi_st', 'ys', 'ds', 'yf', 'dolzn_podrazd_st', 'ms', 'cel_poezdki', 'mf', 'fiofull', 'df', 'gruppa',)

		labels = {
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'ys':_('Год отправления'),
			'ds':_('День отправления'),
			'yf':_('Год прибытия'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'ms':_('Месяц отправления'),
			'cel_poezdki':_('Цель поездки'),
			'mf':_('Месяц прибытия'),
			'fiofull':_('ФИО обучающегося'),
			'df':_('День прибытия'),
			'gruppa':_('Студенческая группа'),
		}
		help_texts = {
			'iofglavnyi_st':_('Подсказка:'),
			'ys':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'yf':_('Подсказка:'),
			'dolzn_podrazd_st':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
			'mf':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
			'df':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
		}
class PrikazForm(ModelForm):
	name='Приказ'
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	dayend=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата прибытия",help_text="Подсказка:")
	daystart=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата отбытия",help_text="Подсказка:")
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	class Meta:
		model = Prikaz
		fields = ('stringprikaz', 'preambula', 'table_spisokdolznostnixprikaz', 'glavbyxfio',)

		labels = {
			'stringprikaz':_('Текст приказа'),
			'preambula':_('Преамбула'),
			'table_spisokdolznostnixprikaz':_(''),
			'glavbyxfio':_('ФИО Главного бухгалтера'),
		}
		help_texts = {
			'stringprikaz':_('Подсказка:'),
			'preambula':_('Подсказка:Вводная часть'),
			'table_spisokdolznostnixprikaz':_('Подсказка:'),
			'glavbyxfio':_('Подсказка:'),
		}
class SluzhebnajaZapiskaForm(ModelForm):
	name='СлужебнаяЗаписка'
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	dayend=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата прибытия",help_text="Подсказка:")
	daystart=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Дата отбытия",help_text="Подсказка:")
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
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
		fields = ('kol_chel', 'rektorfio', 'table_smetastudenta', 'table_spisokdolznostnixsmeta',)

		labels = {
			'kol_chel':_('Количество командируемых лиц'),
			'rektorfio':_('ФИО Ректора'),
			'table_smetastudenta':_(''),
			'table_spisokdolznostnixsmeta':_(''),
		}
		help_texts = {
			'kol_chel':_('Подсказка:'),
			'rektorfio':_('Подсказка:'),
			'table_smetastudenta':_('Подсказка:'),
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
		}
class OtchetStudentaForm(ModelForm):
	name='ОтчетСтудента'
	class Meta:
		model = OtchetStudenta
		fields = ('fioshort', 'this_start',)

		labels = {
			'fioshort':_('ФИО сокращенно'),
			'this_start':_(''),
		}
		help_texts = {
			'fioshort':_('Подсказка:Полностью фамилию и инициалы'),
			'this_start':_('Подсказка:'),
		}
