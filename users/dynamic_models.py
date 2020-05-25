from django.db import models
from django.contrib.auth.models import User

class NapravlenieStudenta(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	dolzn_podrazd_st = models.CharField(max_length=100,blank=True)
	cel_poezdki = models.CharField(max_length=100,blank=True)
	ds = models.DateField(blank=True)
	fiofull = models.CharField(max_length=100,blank=True)
	iofglavnyi_st = models.CharField(max_length=100,blank=True)
	df = models.DateField(blank=True)
	ms = models.DateField(blank=True)
	mf = models.DateField(blank=True)
	gruppa = models.CharField(max_length=100,blank=True)
	yf = models.DateField(blank=True)
	ys = models.DateField(blank=True)


class Prikaz(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	stringprikaz = models.CharField(max_length=100,blank=True)
	glavbyxfio = models.CharField(max_length=100,blank=True)
	table_spisokdolznostnixprikaz = models.CharField(max_length=100,blank=True)
	preambula = models.CharField(max_length=100,blank=True)


class SluzhebnajaZapiska(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	podrazdelenie = models.CharField(max_length=100,blank=True)


class Smeta(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	table_spisokdolznostnixsmeta = models.CharField(max_length=100,blank=True)
	kol_chel = models.IntegerField(blank=True)
	table_smetastudenta = models.CharField(max_length=100,blank=True)
	rektorfio = models.CharField(max_length=100,blank=True)


class OtchetStudenta(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	this_start = models.CharField(max_length=100,blank=True)
	fioshort = models.CharField(max_length=100,blank=True)


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


