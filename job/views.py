from django.shortcuts import render
from .models import Job

def job_list(request):
    queryset=Job.objects.all()
    context={'jobs':queryset}
    return render(request,'job_list.html',context)

def job_detail(request,id):
    queryset=Job.objects.get(id=id)
    context={'jobs':queryset}
    return render(request,'job_detail.html',context)