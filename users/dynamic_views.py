from .dynamic_forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def stage2(request):
	unique_forms=[]
	if request.method == 'POST':
		unique_forms.append(PrikazForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		return redirect('/stage3')
	else:
		unique_forms.append(PrikazForm())
		return render(request,"profile/stage2.html",{"forms": unique_forms})

@login_required
def stage3(request):
	unique_forms=[]
	if request.method == 'POST':
		unique_forms.append(NapravlenieStudentaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		return redirect('/stage4')
	else:
		unique_forms.append(NapravlenieStudentaForm())
		return render(request,"profile/stage3.html",{"forms": unique_forms})

@login_required
def stage4(request):
	unique_forms=[]
	if request.method == 'POST':
		unique_forms.append(OtchetStudentaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		return redirect('/settings')
	else:
		unique_forms.append(OtchetStudentaForm())
		return render(request,"profile/stage4.html",{"forms": unique_forms})

