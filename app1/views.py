from django.shortcuts import render

from django.core.paginator import Paginator
from  .models import StudentModel





def showlist(request,pgno1):
    data=StudentModel.objects.all()
    pages=Paginator(data,2)
    no=pgno1
    print(type(no))
    obj=pages.get_page(int(no))
    pgno=range(1,pages.num_pages+1)
    return render(request,"html.html",{"objec":obj,"pages":pgno})
