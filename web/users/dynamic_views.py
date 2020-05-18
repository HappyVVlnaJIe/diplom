from .dynamic_forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def docs(request):
	unique_forms=[]
	if request.method == 'POST':
		unique_forms.append(dvaForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		unique_forms.append(odinForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
		unique_forms.append(commonForm(data=request.POST))
		if unique_forms[-1].is_valid():
			unique_forms[-1].save()
	else:
		unique_forms.append(dvaForm())
		unique_forms.append(odinForm())
		unique_forms.append(commonForm())
	return render(request,"profile/documents.html",{"forms": unique_forms})