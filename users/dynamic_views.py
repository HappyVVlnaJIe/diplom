from .dynamic_forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
@login_required
def stage1(request):
	unique_forms=[]
	obj=common()
	if request.method == 'POST':
		SluzhebnajaZapiska=SluzhebnajaZapiskaForm(data=request.POST)
		if SluzhebnajaZapiska.is_valid():
			obj.mesto_naznacheniya=SluzhebnajaZapiska.cleaned_data['mesto_naznacheniya'] 
			obj.dayend=SluzhebnajaZapiska.cleaned_data['dayend'] 
			obj.daystart=SluzhebnajaZapiska.cleaned_data['daystart'] 
			obj.dolzn_podrazd=SluzhebnajaZapiska.cleaned_data['dolzn_podrazd'] 
			obj.nazvanie_meropriyatie=SluzhebnajaZapiska.cleaned_data['nazvanie_meropriyatie'] 
			obj.forma_obucheniya=SluzhebnajaZapiska.cleaned_data['forma_obucheniya'] 
			obj.osnova_obucheniya=SluzhebnajaZapiska.cleaned_data['osnova_obucheniya'] 
			obj.iofglavnyi=SluzhebnajaZapiska.cleaned_data['iofglavnyi'] 
			obj.kompensaciya=SluzhebnajaZapiska.cleaned_data['kompensaciya'] 
			obj.iofrektor=SluzhebnajaZapiska.cleaned_data['iofrektor'] 
			obj.table_spisokstudentov=SluzhebnajaZapiska.cleaned_data['table_spisokstudentov'] 
			SluzhebnajaZapiska2=SluzhebnajaZapiska.save(commit=False)
			SluzhebnajaZapiska2.user=request.user
			SluzhebnajaZapiska2.save()
			unique_forms.append(SluzhebnajaZapiska2)
		Smeta=SmetaForm(data=request.POST)
		if Smeta.is_valid():
			Smeta2=Smeta.save(commit=False)
			Smeta2.user=request.user
			Smeta2.save()
			unique_forms.append(Smeta2)
		obj.user=request.user
		obj.save()
		return redirect('/stage2')
	else:
		unique_forms.append(SluzhebnajaZapiskaForm())
		unique_forms.append(SmetaForm())
		return render(request,"profile/stage1.html",{"forms": unique_forms})

@login_required
def stage2(request):
	unique_forms=[]
	obj = common.objects.filter(user=request.user).order_by('-id')[0]
	if request.method == 'POST':
		Prikaz=PrikazForm(data=request.POST)
		if Prikaz.is_valid():
			obj.mesto_naznacheniya=Prikaz.cleaned_data['mesto_naznacheniya'] 
			obj.dayend=Prikaz.cleaned_data['dayend'] 
			obj.daystart=Prikaz.cleaned_data['daystart'] 
			obj.dolzn_podrazd=Prikaz.cleaned_data['dolzn_podrazd'] 
			obj.nazvanie_meropriyatie=Prikaz.cleaned_data['nazvanie_meropriyatie'] 
			obj.forma_obucheniya=Prikaz.cleaned_data['forma_obucheniya'] 
			obj.osnova_obucheniya=Prikaz.cleaned_data['osnova_obucheniya'] 
			obj.iofglavnyi=Prikaz.cleaned_data['iofglavnyi'] 
			obj.kompensaciya=Prikaz.cleaned_data['kompensaciya'] 
			obj.iofrektor=Prikaz.cleaned_data['iofrektor'] 
			obj.table_spisokstudentov=Prikaz.cleaned_data['table_spisokstudentov'] 
			Prikaz2=Prikaz.save(commit=False)
			Prikaz2.user=request.user
			Prikaz2.save()
			unique_forms.append(Prikaz2)
		obj.save()
		return redirect('/stage3')
	else:
		unique_forms.append(PrikazForm())
		return render(request,"profile/stage2.html",{"forms": unique_forms})

@login_required
def stage3(request):
	unique_forms=[]
	obj = common.objects.filter(user=request.user).order_by('-id')[0]
	if request.method == 'POST':
		NapravlenieStudenta=NapravlenieStudentaForm(data=request.POST)
		if NapravlenieStudenta.is_valid():
			obj.mesto_naznacheniya=NapravlenieStudenta.cleaned_data['mesto_naznacheniya'] 
			obj.naselennyj_punkt=NapravlenieStudenta.cleaned_data['naselennyj_punkt'] 
			NapravlenieStudenta2=NapravlenieStudenta.save(commit=False)
			NapravlenieStudenta2.user=request.user
			NapravlenieStudenta2.save()
			unique_forms.append(NapravlenieStudenta2)
		obj.save()
		return redirect('/stage4')
	else:
		unique_forms.append(NapravlenieStudentaForm())
		return render(request,"profile/stage3.html",{"forms": unique_forms})

@login_required
def stage4(request):
	unique_forms=[]
	obj = common.objects.filter(user=request.user).order_by('-id')[0]
	if request.method == 'POST':
		OtchetStudenta=OtchetStudentaForm(data=request.POST)
		if OtchetStudenta.is_valid():
			OtchetStudenta2=OtchetStudenta.save(commit=False)
			OtchetStudenta2.user=request.user
			OtchetStudenta2.save()
			unique_forms.append(OtchetStudenta2)
		obj.save()
		return redirect('/settings')
	else:
		unique_forms.append(OtchetStudentaForm())
		return render(request,"profile/stage4.html",{"forms": unique_forms})

