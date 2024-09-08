from django.shortcuts import render

# Create your views here.
def app1(request):
    return render(request, 'app1/all_app1.html')

def test(request):
    return print("test function in vews of app1")