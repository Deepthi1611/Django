from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def app1(request):
    return render(request, 'app1/all_app1.html')

# def test(request):
#     return print("test function in vews of app1")

def allChai(request):
    chaiVarities = ChaiVariety.objects.all()
    # all() returns an array of elements
    return render(request, 'app1/all_app1.html', {'chais':chaiVarities})

def chaiDetail(request, chaiId):
    # it takes two args- model and primary key
    chai = get_object_or_404(ChaiVariety, pk = chaiId)
    return render(request, 'app1/chaiDetail.html', {'chai':chai})