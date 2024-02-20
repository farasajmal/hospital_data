from django.shortcuts import render
from doctor.models import submit 

# Create your views here.
def docter(request):
    if request.method=='POST':
        obj=submit()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.place=request.POST.get('place')
        obj.qaulification=request.POST.get('QUALIFICATION')


        obj.save()
        

    return render(request,"doctor.html")
def docterview(request):
    obj=submit.objects.all()
    return render(request,"doctorview.html",{'data':obj})
def updatedocter(request,pk):
    obj=submit.objects.get(id=pk)
    if request.method=='POST':
        obj=submit.objects.get(id=pk)
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.place=request.POST.get('place')
        obj.qaulification=request.POST.get('QUALIFICATION')
        obj.save()
        return docterview(request)

    return render(request,"docterupdate.html",{'data':obj})
def delete(request,pk):
    obj=submit.objects.get(id=pk)
    obj.delete()
    return docterview(request)
