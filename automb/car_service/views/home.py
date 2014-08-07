from django.shortcuts import render

# Create your views here.
def index(request):
    #import pdb;pdb.set_trace()
    return render(request,'car_service/siteadmin/index.html')
