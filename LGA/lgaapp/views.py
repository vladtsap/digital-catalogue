from django.shortcuts import render
from lgaapp.models import Art

# Create your views here.
def search(request):
	arts = Art.objects.filter(name='Графіка')

	return render(request, 'search/index.html', {'arts':arts})