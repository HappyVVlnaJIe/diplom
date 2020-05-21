from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


class NapravlenieStudentaForm(ModelForm):
	index='1'
	name='НаправлениеСтудента'
	class Meta:
		model = NapravlenieStudenta
		fields = ('yf', 'ds', 'dolzn_podrazd_st', 'ms', 'iofglavnyi_st', 'gruppa', 'fiofull', 'df', 'ys', 'mf', 'cel_poezdki',)


		labels = {
			'yf':_('Год прибытия'),
			'ds':_('День отправления'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'ms':_('Месяц отправления'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'gruppa':_('Студенческая группа'),
			'fiofull':_('ФИО обучающегося'),
			'df':_('День прибытия'),
			'ys':_('Год отправления'),
			'mf':_('Месяц прибытия'),
			'cel_poezdki':_('Цель поездки'),
		}
		help_texts = {
			'yf':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'dolzn_podrazd_st':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'iofglavnyi_st':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
			'df':_('Подсказка:'),
			'ys':_('Подсказка:'),
			'mf':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
		}
class SluzhebnajaZapiskaForm(ModelForm):
	index='1'
	name='СлужебнаяЗаписка'
	class Meta:
		model = SluzhebnajaZapiska
		fields = ('iofrektor', 'table_spisokstudentov', 'kompensaciya', 'podrazdelenie', 'osnova_obucheniya', 'forma_obucheniya',)


		labels = {
			'iofrektor':_('ФИО Ректора'),
			'table_spisokstudentov':_(''),
			'kompensaciya':_('Компенсация'),
			'podrazdelenie':_('Название подразделения'),
			'osnova_obucheniya':_('Основа обучения'),
			'forma_obucheniya':_('Форма обучения'),
		}
		help_texts = {
			'iofrektor':_('Подсказка:'),
			'table_spisokstudentov':_('Подсказка:'),
			'kompensaciya':_('Подсказка:'),
			'podrazdelenie':_('Подсказка:'),
			'osnova_obucheniya':_('Подсказка:Контракт или бюджет'),
			'forma_obucheniya':_('Подсказка:Очная или заочная'),
		}
class SmetaForm(ModelForm):
	index='1'
	name='Смета'
	class Meta:
		model = Smeta
		fields = ('table_smetastudenta', 'kol_chel', 'table_spisokdolznostnixsmeta', 'rektorfio',)


		labels = {
			'table_smetastudenta':_(''),
			'kol_chel':_('Количество командируемых лиц'),
			'table_spisokdolznostnixsmeta':_(''),
			'rektorfio':_('ФИО Ректора'),
		}
		help_texts = {
			'table_smetastudenta':_('Подсказка:'),
			'kol_chel':_('Подсказка:'),
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
			'rektorfio':_('Подсказка:'),
		}
class OtchetStudentaForm(ModelForm):
	index='2'
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
class osnovnyeForm(ModelForm):
	index='0'
	name='основные'
	class Meta:
		model = osnovnye
		fields = ('mesto_naznacheniya', 'naselennyj_punkt', 'nazvanie_meropriyatie', 'daystart', 'dayend', 'dolzn_podrazd', 'iofglavnyi',)


		labels = {
			'mesto_naznacheniya':_('Место назначения'),
			'naselennyj_punkt':_('Населенный пункт'),
			'nazvanie_meropriyatie':_('Название мероприятия'),
			'daystart':_('Дата отбытия'),
			'dayend':_('Дата прибытия'),
			'dolzn_podrazd':_('Название подразделения'),
			'iofglavnyi':_('ФИО главного по подразделению'),
		}
		help_texts = {
			'mesto_naznacheniya':_('Подсказка:Населенный пункт, университет'),
			'naselennyj_punkt':_('Подсказка:'),
			'nazvanie_meropriyatie':_('Подсказка:'),
			'daystart':_('Подсказка:'),
			'dayend':_('Подсказка:'),
			'dolzn_podrazd':_('Подсказка:'),
			'iofglavnyi':_('Подсказка:'),
		}
