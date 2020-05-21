from django.db import models


class NapravlenieStudenta(models.Model):
	ms = models.DateTimeField()
	ys = models.DateTimeField()
	iofglavnyi_st = models.CharField(max_length=100)
	fiofull = models.CharField(max_length=100)
	dolzn_podrazd_st = models.CharField(max_length=100)
	gruppa = models.CharField(max_length=100)
	mf = models.DateTimeField()
	df = models.DateTimeField()
	cel_poezdki = models.CharField(max_length=100)
	yf = models.DateTimeField()
	ds = models.DateTimeField()


class Prikaz(models.Model):
	stringprikaz = models.CharField(max_length=100)
	table_spisokdolznostnixprikaz = models.CharField(max_length=100)
	preambula = models.CharField(max_length=100)
	glavbyxfio = models.CharField(max_length=100)


class SluzhebnajaZapiska(models.Model):
	podrazdelenie = models.CharField(max_length=100)


class Smeta(models.Model):
	rektorfio = models.CharField(max_length=100)
	table_spisokdolznostnixsmeta = models.CharField(max_length=100)
	table_smetastudenta = models.CharField(max_length=100)
	kol_chel = models.IntegerField()


class OtchetStudenta(models.Model):
	fioshort = models.CharField(max_length=100)
	this_start = models.CharField(max_length=100)


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


