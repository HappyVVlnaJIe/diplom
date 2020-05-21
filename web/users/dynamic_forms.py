from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, Prikaz, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


class NapravlenieStudentaForm(ModelForm):
	index='1'
	name='НаправлениеСтудента'
	class Meta:
		model = NapravlenieStudenta
		fields = ('ms', 'ys', 'iofglavnyi_st', 'fiofull', 'dolzn_podrazd_st', 'gruppa', 'mf', 'df', 'cel_poezdki', 'yf', 'ds',)


		labels = {
			'ms':_('Месяц отправления'),
			'ys':_('Год отправления'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'fiofull':_('ФИО обучающегося'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'gruppa':_('Студенческая группа'),
			'mf':_('Месяц прибытия'),
			'df':_('День прибытия'),
			'cel_poezdki':_('Цель поездки'),
			'yf':_('Год прибытия'),
			'ds':_('День отправления'),
		}
		help_texts = {
			'ms':_('Подсказка:'),
			'ys':_('Подсказка:'),
			'iofglavnyi_st':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
			'dolzn_podrazd_st':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'mf':_('Подсказка:'),
			'df':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
			'yf':_('Подсказка:'),
			'ds':_('Подсказка:'),
		}
class PrikazForm(ModelForm):
	index='1'
	name='Приказ'
	class Meta:
		model = Prikaz
		fields = ('stringprikaz', 'table_spisokdolznostnixprikaz', 'preambula', 'glavbyxfio',)


		labels = {
			'stringprikaz':_('Текст приказа'),
			'table_spisokdolznostnixprikaz':_(''),
			'preambula':_('Преамбула'),
			'glavbyxfio':_('ФИО Главного бухгалтера'),
		}
		help_texts = {
			'stringprikaz':_('Подсказка:'),
			'table_spisokdolznostnixprikaz':_('Подсказка:'),
			'preambula':_('Подсказка:Вводная часть'),
			'glavbyxfio':_('Подсказка:'),
		}
class SluzhebnajaZapiskaForm(ModelForm):
	index='1'
	name='СлужебнаяЗаписка'
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
	index='1'
	name='Смета'
	class Meta:
		model = Smeta
		fields = ('rektorfio', 'table_spisokdolznostnixsmeta', 'table_smetastudenta', 'kol_chel',)


		labels = {
			'rektorfio':_('ФИО Ректора'),
			'table_spisokdolznostnixsmeta':_(''),
			'table_smetastudenta':_(''),
			'kol_chel':_('Количество командируемых лиц'),
		}
		help_texts = {
			'rektorfio':_('Подсказка:'),
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
			'table_smetastudenta':_('Подсказка:'),
			'kol_chel':_('Подсказка:'),
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
		fields = ('mesto_naznacheniya', 'naselennyj_punkt', 'nazvanie_meropriyatie', 'daystart', 'dayend', 'forma_obucheniya', 'osnova_obucheniya', 'table_spisokstudentov', 'kompensaciya', 'iofrektor', 'dolzn_podrazd', 'iofglavnyi',)


		labels = {
			'mesto_naznacheniya':_('Место назначения'),
			'naselennyj_punkt':_('Населенный пункт'),
			'nazvanie_meropriyatie':_('Название мероприятия'),
			'daystart':_('Дата отбытия'),
			'dayend':_('Дата прибытия'),
			'forma_obucheniya':_('Форма обучения'),
			'osnova_obucheniya':_('Основа обучения'),
			'table_spisokstudentov':_(''),
			'kompensaciya':_('Компенсация'),
			'iofrektor':_('ФИО Ректора'),
			'dolzn_podrazd':_('Название подразделения'),
			'iofglavnyi':_('ФИО главного по подразделению'),
		}
		help_texts = {
			'mesto_naznacheniya':_('Подсказка:Населенный пункт, университет'),
			'naselennyj_punkt':_('Подсказка:'),
			'nazvanie_meropriyatie':_('Подсказка:'),
			'daystart':_('Подсказка:'),
			'dayend':_('Подсказка:'),
			'forma_obucheniya':_('Подсказка:Очная или заочная'),
			'osnova_obucheniya':_('Подсказка:Контракт или бюджет'),
			'table_spisokstudentov':_('Подсказка:'),
			'kompensaciya':_('Подсказка:'),
			'iofrektor':_('Подсказка:'),
			'dolzn_podrazd':_('Подсказка:'),
			'iofglavnyi':_('Подсказка:'),
		}
