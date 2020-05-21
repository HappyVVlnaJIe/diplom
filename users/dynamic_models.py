from django.db import models


class NapravlenieStudenta(models.Model):
	yf = models.DateTimeField()
	ds = models.DateTimeField()
	dolzn_podrazd_st = models.CharField(max_length=100)
	ms = models.DateTimeField()
	iofglavnyi_st = models.CharField(max_length=100)
	gruppa = models.CharField(max_length=100)
	fiofull = models.CharField(max_length=100)
	df = models.DateTimeField()
	ys = models.DateTimeField()
	mf = models.DateTimeField()
	cel_poezdki = models.CharField(max_length=100)


class SluzhebnajaZapiska(models.Model):
	iofrektor = models.CharField(max_length=100)
	table_spisokstudentov = models.CharField(max_length=100)
	kompensaciya = models.CharField(max_length=100)
	podrazdelenie = models.CharField(max_length=100)
	osnova_obucheniya = models.CharField(max_length=100)
	forma_obucheniya = models.CharField(max_length=100)


class Smeta(models.Model):
	table_smetastudenta = models.CharField(max_length=100)
	kol_chel = models.IntegerField()
	table_spisokdolznostnixsmeta = models.CharField(max_length=100)
	rektorfio = models.CharField(max_length=100)


class OtchetStudenta(models.Model):
	fioshort = models.CharField(max_length=100)
	this_start = models.CharField(max_length=100)


class osnovnye(models.Model):
	mesto_naznacheniya = models.CharField(max_length=100)
	naselennyj_punkt = models.CharField(max_length=100)
	nazvanie_meropriyatie = models.CharField(max_length=100)
	daystart = models.DateTimeField()
	dayend = models.DateTimeField()
	dolzn_podrazd = models.CharField(max_length=100)
	iofglavnyi = models.CharField(max_length=100)


