from django.shortcuts import render,redirect
from patiend.models import submit

# Create your views here.
def paitend(request):
    if request.method=='POST':
        obj=submit()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.place=request.POST.get('place')
        obj.disease=request.POST.get('disease')
        obj.save()
    return render(request,"patiend.html")
def paitendview(request):
    obj=submit.objects.all()
    return render(request,"patiendview.html",{'data':obj})
def updatepatient(request,pk):
    obj=submit.objects.get(id=pk)
    if request.method=='POST':
        obj=submit.objects.get(id=pk)
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.place=request.POST.get('place')
        obj.disease=request.POST.get('disease')
        obj.save()
        return redirect("viewpt")
    return render(request,"update.html",{'data':obj})
def delete(request,pk):
    obj=submit.objects.get(id=pk)
    obj.delete()
    return paitendview(request)