from django.db import models


class NapravlenieStudenta(models.Model):
	yf = models.DateField()
	ys = models.DateField()
	iofglavnyi_st = models.CharField(max_length=100)
	cel_poezdki = models.CharField(max_length=100)
	ds = models.DateField()
	gruppa = models.CharField(max_length=100)
	df = models.DateField()
	ms = models.DateField()
	mf = models.DateField()
	fiofull = models.CharField(max_length=100)
	dolzn_podrazd_st = models.CharField(max_length=100)


class Prikaz(models.Model):
	preambula = models.CharField(max_length=100)
	table_spisokdolznostnixprikaz = models.CharField(max_length=100)
	stringprikaz = models.CharField(max_length=100)
	glavbyxfio = models.CharField(max_length=100)


class SluzhebnajaZapiska(models.Model):
	podrazdelenie = models.CharField(max_length=100)


class Smeta(models.Model):
	table_spisokdolznostnixsmeta = models.CharField(max_length=100)
	kol_chel = models.IntegerField()
	table_smetastudenta = models.CharField(max_length=100)
	rektorfio = models.CharField(max_length=100)


class OtchetStudenta(models.Model):
	this_start = models.CharField(max_length=100)
	fioshort = models.CharField(max_length=100)


class osnovnye(models.Model):
	mesto_naznacheniya = models.CharField(max_length=100,blank=True)
	naselennyj_punkt = models.CharField(max_length=100,blank=True)
	nazvanie_meropriyatie = models.CharField(max_length=100,blank=True)
	daystart = models.DateField(blank=True)
	dayend = models.DateField(blank=True)
	forma_obucheniya = models.CharField(max_length=100,blank=True)
	osnova_obucheniya = models.CharField(max_length=100,blank=True)
	table_spisokstudentov = models.CharField(max_length=100,blank=True)
	kompensaciya = models.CharField(max_length=100,blank=True)
	iofrektor = models.CharField(max_length=100,blank=True)
	dolzn_podrazd = models.CharField(max_length=100,blank=True)
	iofglavnyi = models.CharField(max_length=100,blank=True)


