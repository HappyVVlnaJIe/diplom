from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, Prikaz, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


class NapravlenieStudentaForm(ModelForm):
	index='1'
	name='НаправлениеСтудента'
	class Meta:
		model = NapravlenieStudenta
		fields = ('fiofull', 'dolzn_podrazd_st', 'ds', 'cel_poezdki', 'gruppa', 'ys', 'iofglavnyi_st', 'mf', 'ms', 'df', 'yf',)


		labels = {
			'fiofull':_('ФИО обучающегося'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'ds':_('День отправления'),
			'cel_poezdki':_('Цель поездки'),
			'gruppa':_('Студенческая группа'),
			'ys':_('Год отправления'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'mf':_('Месяц прибытия'),
			'ms':_('Месяц отправления'),
			'df':_('День прибытия'),
			'yf':_('Год прибытия'),
		}
		help_texts = {
			'fiofull':_('Подсказка:полные ФИО'),
			'dolzn_podrazd_st':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'ys':_('Подсказка:'),
			'iofglavnyi_st':_('Подсказка:'),
			'mf':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'df':_('Подсказка:'),
			'yf':_('Подсказка:'),
		}
class PrikazForm(ModelForm):
	index='1'
	name='Приказ'
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
		fields = ('rektorfio', 'kol_chel', 'table_spisokdolznostnixsmeta', 'table_smetastudenta',)


		labels = {
			'rektorfio':_('ФИО Ректора'),
			'kol_chel':_('Количество командируемых лиц'),
			'table_spisokdolznostnixsmeta':_(''),
			'table_smetastudenta':_(''),
		}
		help_texts = {
			'rektorfio':_('Подсказка:'),
			'kol_chel':_('Подсказка:'),
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
			'table_smetastudenta':_('Подсказка:'),
		}
class OtchetStudentaForm(ModelForm):
	index='2'
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
