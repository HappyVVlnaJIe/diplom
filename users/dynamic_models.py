from django.db import models


class NapravlenieStudenta(models.Model):
	ys = models.DateTimeField()
	gruppa = models.CharField(max_length=100)
	yf = models.DateTimeField()
	iofglavnyi_st = models.CharField(max_length=100)
	df = models.DateTimeField()
	fiofull = models.CharField(max_length=100)
	mf = models.DateTimeField()
	ds = models.DateTimeField()
	ms = models.DateTimeField()
	dolzn_podrazd_st = models.CharField(max_length=100)
	cel_poezdki = models.CharField(max_length=100)


class Prikaz(models.Model):
	preambula = models.CharField(max_length=100)
	glavbyxfio = models.CharField(max_length=100)
	table_spisokdolznostnixprikaz = models.CharField(max_length=100)
	stringprikaz = models.CharField(max_length=100)


class SluzhebnajaZapiska(models.Model):
	podrazdelenie = models.CharField(max_length=100)


class Smeta(models.Model):
	rektorfio = models.CharField(max_length=100)
	table_smetastudenta = models.CharField(max_length=100)
	table_spisokdolznostnixsmeta = models.CharField(max_length=100)
	kol_chel = models.IntegerField()


class OtchetStudenta(models.Model):
	this_start = models.CharField(max_length=100)
	fioshort = models.CharField(max_length=100)


class osnovnye(models.Model):
	mesto_naznacheniya = models.CharField(max_length=100,required=False)
	naselennyj_punkt = models.CharField(max_length=100,required=False)
	nazvanie_meropriyatie = models.CharField(max_length=100,required=False)
	daystart = models.DateTimeField(required=False)
	dayend = models.DateTimeField(required=False)
	forma_obucheniya = models.CharField(max_length=100,required=False)
	osnova_obucheniya = models.CharField(max_length=100,required=False)
	table_spisokstudentov = models.CharField(max_length=100,required=False)
	kompensaciya = models.CharField(max_length=100,required=False)
	iofrektor = models.CharField(max_length=100,required=False)
	dolzn_podrazd = models.CharField(max_length=100,required=False)
	iofglavnyi = models.CharField(max_length=100,required=False)


