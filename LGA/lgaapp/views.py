from django.shortcuts import render
from lgaapp.models import Art

q = [1,2,3]
# Create your views here.
def search(request):
	arts = Art.objects.filter(name='Графіка')

	return render(request, 'search/index.html', {'arts':arts, 'q':q})


