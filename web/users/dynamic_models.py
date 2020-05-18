from django.db import models


class dva(models.Model):
	rektorFio = models.CharField(max_length=200)
	table_smetaStudenta = models.CharField(max_length=200)
	kol_chel = models.CharField(max_length=200)
	table_spisokDolznostnixSmeta = models.CharField(max_length=200)


class odin(models.Model):
	glavbyxFio = models.CharField(max_length=200)
	table_spisokStudentov = models.CharField(max_length=200)
	preambula = models.CharField(max_length=200)
	mesto_naznacheniya = models.CharField(max_length=200)
	ioFrektor = models.CharField(max_length=200)
	kompensaciya = models.CharField(max_length=200)
	stringPrikaz = models.CharField(max_length=200)
	forma_obucheniya = models.CharField(max_length=200)
	osnova_obucheniya = models.CharField(max_length=200)


class common(models.Model):
	nazvanie_meropriyatie = models.CharField(max_length=200)
	daystart = models.CharField(max_length=200)
	dayend = models.CharField(max_length=200)
	dolzn_podrazd = models.CharField(max_length=200)
	ioFglavnyi = models.CharField(max_length=200)


