# from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to the database
            ContactMessage.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return JsonResponse({'message': 'Success'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})

# def index(request):
#     return render(request,'index.html')
