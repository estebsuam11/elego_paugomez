from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Reserve

from .forms import ReserveCreateForm


class ServicesListView(View):
    def get(self, request, *args, **kwargs):
        context={

        }

        return render(request, 'services-responsive.html', context)
    
class ReserveCreateView(View):
    def get(self, request, *args, **kwargs):
        form=ReserveCreateForm()
        context={
            'form':form
        }
        return render(request, 'reserve-responsive.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = ReserveCreateForm(request.POST)
            if form.is_valid():

                fullname = form.changed_data.get('fullname')
                address = form.cleaned_data.get('address')
                phone = form.cleaned_data.get('phone')
                email = form.cleaned_data.get('email')
                zip_code = form.cleaned_data.get('zip_code')
                service = form.cleaned_data.get('service')
                date = form.cleaned_data.get('date')
                number_hour = form.cleaned_data.get('number_hour')
                start_time = form.cleaned_data.get('start_time')
                pets = form.cleaned_data.get('pets')
                pet_number = form.cleaned_data.get('pet_number')
                
                r, created = Reserve.objects.get_or_create(address=address, phone=phone, email=email, zip_code=zip_code, service=service, date=date, number_hour=number_hour, start_time=start_time, pets=pets, pet_number=pet_number)
                r.save()
                
                

            
        context={

        }
        return render(request, 'reserve-responsive.html', context)