from .dynamic_forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
@login_required
def stage1(request):
	unique_forms=[]
	if request.method == 'POST':
		obj=osnovnye()
		unique_forms.append(SluzhebnajaZapiskaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		obj.table_spisokstudentov=unique_forms[-1].cleaned_data['table_spisokstudentov'] 
		obj.mesto_naznacheniya=unique_forms[-1].cleaned_data['mesto_naznacheniya'] 
		obj.iofrektor=unique_forms[-1].cleaned_data['iofrektor'] 
		obj.forma_obucheniya=unique_forms[-1].cleaned_data['forma_obucheniya'] 
		obj.nazvanie_meropriyatie=unique_forms[-1].cleaned_data['nazvanie_meropriyatie'] 
		obj.kompensaciya=unique_forms[-1].cleaned_data['kompensaciya'] 
		obj.dolzn_podrazd=unique_forms[-1].cleaned_data['dolzn_podrazd'] 
		obj.osnova_obucheniya=unique_forms[-1].cleaned_data['osnova_obucheniya'] 
		obj.daystart=unique_forms[-1].cleaned_data['daystart'] 
		obj.dayend=unique_forms[-1].cleaned_data['dayend'] 
		obj.iofglavnyi=unique_forms[-1].cleaned_data['iofglavnyi'] 
		unique_forms.append(SmetaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		obj.save()
		request.session['session_id']=obj.id
		return redirect('/stage2')
	else:
		session_id=request.session.get('session_id',None)
		if session_id!=None:
			unique_forms.append(SluzhebnajaZapiskaForm(
				data=SluzhebnajaZapiska.objects.get(pk=session_id)))
			unique_forms.append(SmetaForm(data=Smeta.objects.get(pk=session_id)))
		else:
			unique_forms.append(SluzhebnajaZapiskaForm())
			unique_forms.append(SmetaForm())
		return render(request,"profile/stage1.html",{"forms": unique_forms})

@login_required
def stage2(request):
	unique_forms=[]
	if request.method == 'POST':
		obj=osnovnye.objects.order_by('-id')[0]
		unique_forms.append(PrikazForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		obj.table_spisokstudentov=unique_forms[-1].cleaned_data['table_spisokstudentov'] 
		obj.mesto_naznacheniya=unique_forms[-1].cleaned_data['mesto_naznacheniya'] 
		obj.iofrektor=unique_forms[-1].cleaned_data['iofrektor'] 
		obj.forma_obucheniya=unique_forms[-1].cleaned_data['forma_obucheniya'] 
		obj.nazvanie_meropriyatie=unique_forms[-1].cleaned_data['nazvanie_meropriyatie'] 
		obj.kompensaciya=unique_forms[-1].cleaned_data['kompensaciya'] 
		obj.dolzn_podrazd=unique_forms[-1].cleaned_data['dolzn_podrazd'] 
		obj.osnova_obucheniya=unique_forms[-1].cleaned_data['osnova_obucheniya'] 
		obj.daystart=unique_forms[-1].cleaned_data['daystart'] 
		obj.dayend=unique_forms[-1].cleaned_data['dayend'] 
		obj.iofglavnyi=unique_forms[-1].cleaned_data['iofglavnyi'] 
		obj.save()
		return redirect('/stage3')
	else:
		unique_forms.append(PrikazForm())
		return render(request,"profile/stage2.html",{"forms": unique_forms})

@login_required
def stage3(request):
	unique_forms=[]
	if request.method == 'POST':
		obj=osnovnye.objects.order_by('-id')[0]
		unique_forms.append(NapravlenieStudentaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		obj.naselennyj_punkt=unique_forms[-1].cleaned_data['naselennyj_punkt'] 
		obj.mesto_naznacheniya=unique_forms[-1].cleaned_data['mesto_naznacheniya'] 
		obj.save()
		return redirect('/stage4')
	else:
		unique_forms.append(NapravlenieStudentaForm())
		return render(request,"profile/stage3.html",{"forms": unique_forms})

@login_required
def stage4(request):
	unique_forms=[]
	if request.method == 'POST':
		obj=osnovnye.objects.order_by('-id')[0]
		unique_forms.append(OtchetStudentaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		obj.save()
		return redirect('/settings')
	else:
		unique_forms.append(OtchetStudentaForm())
		return render(request,"profile/stage4.html",{"forms": unique_forms})

