from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

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

def chaiStore(request):
    stores = None
    form = None
    if request.method == 'POST':
        # form after the submission
        # passing post data received through post to form
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            # chai_variety is the field we gave in forms.py
            chai_variety = form.cleaned_data['chai_variety']
            # ChaiVarieties is the field in Store model
            stores = Store.objects.filter(ChaiVarieties = chai_variety)
    else:
        # render form before the submission
        form = ChaiVarietyForm()
    return render(request, 'app1/chai_stores.html', {'stores':stores, 'form': form})