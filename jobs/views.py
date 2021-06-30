from django.shortcuts import render,get_object_or_404
from .models import Job
# Create your views here.
def rajesh(request):
    return render(request,'jobs/rajesh.html')


def home(request):
    Jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs':Jobs})

def detail(request,job_id):
    job_detail = get_object_or_404(Job,pk=job_id)

    return render(request,'jobs/detail.html',{'job': job_detail})
