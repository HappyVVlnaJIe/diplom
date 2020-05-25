from django.db import models
from django.contrib.auth.models import User

class NapravlenieStudenta(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	iofglavnyi_st = models.CharField(max_length=100)
	ys = models.DateField()
	ds = models.DateField()
	yf = models.DateField()
	dolzn_podrazd_st = models.CharField(max_length=100)
	ms = models.DateField()
	cel_poezdki = models.CharField(max_length=100)
	mf = models.DateField()
	fiofull = models.CharField(max_length=100)
	df = models.DateField()
	gruppa = models.CharField(max_length=100)


class Prikaz(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	stringprikaz = models.CharField(max_length=100)
	preambula = models.CharField(max_length=100)
	table_spisokdolznostnixprikaz = models.CharField(max_length=100)
	glavbyxfio = models.CharField(max_length=100)


class SluzhebnajaZapiska(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	podrazdelenie = models.CharField(max_length=100)


class Smeta(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	kol_chel = models.IntegerField()
	rektorfio = models.CharField(max_length=100)
	table_smetastudenta = models.CharField(max_length=100)
	table_spisokdolznostnixsmeta = models.CharField(max_length=100)


class OtchetStudenta(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	fioshort = models.CharField(max_length=100)
	this_start = models.CharField(max_length=100)


class common(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
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


