from .dynamic_forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def docs(request):
	unique_forms=[]
	if request.method == 'POST':
		unique_forms.append(NapravlenieStudentaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		unique_forms.append(SluzhebnajaZapiskaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		unique_forms.append(SmetaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		unique_forms.append(OtchetStudentaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		unique_forms.append(osnovnyeForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
	else:
		unique_forms.append(NapravlenieStudentaForm())
		unique_forms.append(SluzhebnajaZapiskaForm())
		unique_forms.append(SmetaForm())
		unique_forms.append(OtchetStudentaForm())
		unique_forms.append(osnovnyeForm())
	return render(request,"profile/documents.html",{"forms": unique_forms})