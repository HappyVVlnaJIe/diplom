from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .dynamic_models import NapravlenieStudenta, Prikaz, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


class NapravlenieStudentaForm(ModelForm):
	index='1'
	name='НаправлениеСтудента'
	class Meta:
		model = NapravlenieStudenta
		fields = ('mf', 'yf', 'cel_poezdki', 'gruppa', 'iofglavnyi_st', 'df', 'dolzn_podrazd_st', 'ys', 'ms', 'ds', 'fiofull',)


		labels = {
			'mf':_('Месяц прибытия'),
			'yf':_('Год прибытия'),
			'cel_poezdki':_('Цель поездки'),
			'gruppa':_('Студенческая группа'),
			'iofglavnyi_st':_('ФИО главного по подразделению'),
			'df':_('День прибытия'),
			'dolzn_podrazd_st':_('Должностное подразделение'),
			'ys':_('Год отправления'),
			'ms':_('Месяц отправления'),
			'ds':_('День отправления'),
			'fiofull':_('ФИО обучающегося'),
		}
		help_texts = {
			'mf':_('Подсказка:'),
			'yf':_('Подсказка:'),
			'cel_poezdki':_('Подсказка:'),
			'gruppa':_('Подсказка:'),
			'iofglavnyi_st':_('Подсказка:'),
			'df':_('Подсказка:'),
			'dolzn_podrazd_st':_('Подсказка:'),
			'ys':_('Подсказка:'),
			'ms':_('Подсказка:'),
			'ds':_('Подсказка:'),
			'fiofull':_('Подсказка:полные ФИО'),
		}
class PrikazForm(ModelForm):
	index='1'
	name='Приказ'
	class Meta:
		model = Prikaz
		fields = ('glavbyxfio', 'preambula', 'table_spisokdolznostnixprikaz', 'stringprikaz',)


		labels = {
			'glavbyxfio':_('ФИО Главного бухгалтера'),
			'preambula':_('Преамбула'),
			'table_spisokdolznostnixprikaz':_(''),
			'stringprikaz':_('Текст приказа'),
		}
		help_texts = {
			'glavbyxfio':_('Подсказка:'),
			'preambula':_('Подсказка:Вводная часть'),
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
		fields = ('kol_chel', 'table_smetastudenta', 'table_spisokdolznostnixsmeta', 'rektorfio',)


		labels = {
			'kol_chel':_('Количество командируемых лиц'),
			'table_smetastudenta':_(''),
			'table_spisokdolznostnixsmeta':_(''),
			'rektorfio':_('ФИО Ректора'),
		}
		help_texts = {
			'kol_chel':_('Подсказка:'),
			'table_smetastudenta':_('Подсказка:'),
			'table_spisokdolznostnixsmeta':_('Подсказка:'),
			'rektorfio':_('Подсказка:'),
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
