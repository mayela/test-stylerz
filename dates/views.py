from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from dates.models import Date
from dates.forms import DateForm

def create_date_view(request):
    if request.method == 'POST':
        date_form = DateForm(request.POST['date'])
        if date_form.is_valid():
            date = Date()
            date.treatment_type = date_form.cleaned_data.get('treatment_type')
            date.customer = date_form.cleaned_data.get('customer')
            date.specialist = date_form.cleaned_data.get('specialist')
            date.start_datetime = date_form.cleaned_data.get('start')
            date.save()
            return HttpResponseRedirect('cita/crear')
        else:
            return HttpResponseBadRequest("Debe de llenar todos los campos")
    else:
        date_form = DateForm()
        context = {'date': date_form}
        return render(request, 'create_date.html', context)



