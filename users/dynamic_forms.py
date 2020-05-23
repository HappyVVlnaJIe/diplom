from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, Prikaz, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


class NapravlenieStudentaForm(ModelForm):
	name='НаправлениеСтудента'
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	naselennyj_punkt=forms.CharField(label="Населенный пункт",help_text="Подсказка:")
	class Meta:
		model = NapravlenieStudenta
		fields = ('ys', 'gruppa', 'yf', 'iofglavnyi_st', 'df', 'fiofull', 'mf', 'ds', 'ms', 'dolzn_podrazd_st', 'cel_poezdki',)

		labels = {
			'ys':_('Год отправления'),
			'gruppa':_('Студенческая группа'),
			'yf':_('Год прибытия'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'df':_('День прибытия'),
			'fiofull':_('ФИО обучающегося'),
			'mf':_('Месяц прибытия'),
			'ds':_('День отправления'),
			'ms':_('Месяц отправления'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'cel_poezdki':_('Цель поездки'),
		}
		help_texts = {
			'ys':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'yf':_('Подсказка:'),
			'iofglavnyi_st':_('Подсказка:'),
			'df':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
			'mf':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'dolzn_podrazd_st':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
		}
class PrikazForm(ModelForm):
	name='Приказ'
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	daystart=forms.DateTimeField(label="Дата отбытия",help_text="Подсказка:")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	dayend=forms.DateTimeField(label="Дата прибытия",help_text="Подсказка:")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	class Meta:
		model = Prikaz
		fields = ('preambula', 'glavbyxfio', 'table_spisokdolznostnixprikaz', 'stringprikaz',)

		labels = {
			'preambula':_('Преамбула'),
			'glavbyxfio':_('ФИО Главного бухгалтера'),
			'table_spisokdolznostnixprikaz':_(''),
			'stringprikaz':_('Текст приказа'),
		}
		help_texts = {
			'preambula':_('Подсказка:Вводная часть'),
			'glavbyxfio':_('Подсказка:'),
			'table_spisokdolznostnixprikaz':_('Подсказка:'),
			'stringprikaz':_('Подсказка:'),
		}
class SluzhebnajaZapiskaForm(ModelForm):
	name='СлужебнаяЗаписка'
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	daystart=forms.DateTimeField(label="Дата отбытия",help_text="Подсказка:")
	iofrektor=forms.CharField(label="ФИО Ректора",help_text="Подсказка:")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	mesto_naznacheniya=forms.CharField(label="Место назначения",help_text="Подсказка:Населенный пункт, университет")
	forma_obucheniya=forms.CharField(label="Форма обучения",help_text="Подсказка:Очная или заочная")
	table_spisokstudentov=forms.CharField(label="",help_text="Подсказка:")
	osnova_obucheniya=forms.CharField(label="Основа обучения",help_text="Подсказка:Контракт или бюджет")
	kompensaciya=forms.CharField(label="Компенсация",help_text="Подсказка:")
	dayend=forms.DateTimeField(label="Дата прибытия",help_text="Подсказка:")
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
	dolzn_podrazd=forms.CharField(label="Название подразделения",help_text="Подсказка:")
	daystart=forms.DateTimeField(label="Дата отбытия",help_text="Подсказка:")
	nazvanie_meropriyatie=forms.CharField(label="Название мероприятия",help_text="Подсказка:")
	dayend=forms.DateTimeField(label="Дата прибытия",help_text="Подсказка:")
	iofglavnyi=forms.CharField(label="ФИО главного по подразделению",help_text="Подсказка:")
	class Meta:
		model = Smeta
		fields = ('rektorfio', 'table_smetastudenta', 'table_spisokdolznostnixsmeta', 'kol_chel',)

		labels = {
			'rektorfio':_('ФИО Ректора'),
			'table_smetastudenta':_(''),
			'table_spisokdolznostnixsmeta':_(''),
			'kol_chel':_('Количество командируемых лиц'),
		}
		help_texts = {
			'rektorfio':_('Подсказка:'),
			'table_smetastudenta':_('Подсказка:'),
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
			'kol_chel':_('Подсказка:'),
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
