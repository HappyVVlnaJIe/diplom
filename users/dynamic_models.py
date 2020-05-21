from django.db import models


class NapravlenieStudenta(models.Model):
	mf = models.DateTimeField()
	yf = models.DateTimeField()
	cel_poezdki = models.CharField(max_length=100)
	gruppa = models.CharField(max_length=100)
	iofglavnyi_st = models.CharField(max_length=100)
	df = models.DateTimeField()
	dolzn_podrazd_st = models.CharField(max_length=100)
	ys = models.DateTimeField()
	ms = models.DateTimeField()
	ds = models.DateTimeField()
	fiofull = models.CharField(max_length=100)


class Prikaz(models.Model):
	glavbyxfio = models.CharField(max_length=100)
	preambula = models.CharField(max_length=100)
	table_spisokdolznostnixprikaz = models.CharField(max_length=100)
	stringprikaz = models.CharField(max_length=100)


class SluzhebnajaZapiska(models.Model):
	podrazdelenie = models.CharField(max_length=100)


class Smeta(models.Model):
	kol_chel = models.IntegerField()
	table_smetastudenta = models.CharField(max_length=100)
	table_spisokdolznostnixsmeta = models.CharField(max_length=100)
	rektorfio = models.CharField(max_length=100)


class OtchetStudenta(models.Model):
	this_start = models.CharField(max_length=100)
	fioshort = models.CharField(max_length=100)


class osnovnye(models.Model):
	mesto_naznacheniya = models.CharField(max_length=100)
	naselennyj_punkt = models.CharField(max_length=100)
	nazvanie_meropriyatie = models.CharField(max_length=100)
	daystart = models.DateTimeField()
	dayend = models.DateTimeField()
	forma_obucheniya = models.CharField(max_length=100)
	osnova_obucheniya = models.CharField(max_length=100)
	table_spisokstudentov = models.CharField(max_length=100)
	kompensaciya = models.CharField(max_length=100)
	iofrektor = models.CharField(max_length=100)
	dolzn_podrazd = models.CharField(max_length=100)
	iofglavnyi = models.CharField(max_length=100)


