from django.shortcuts import render
from django.shortcuts import HttpResponse
from myapp.models import Product



# Create your views here.
def home(request):
    # return HttpResponse("ban dang xay dung ung  dung truy xuat du lieu den sqllite...")
    # rs = Student.objects.all()
    # s=""
    # for item in rs:
    #     s=s+"ID:"+ str(item.id)+",ho ten:"  + str(item.fullname)+",tuoi" +str(item.age)+"</br>"
    #
    # # for item in rs:
    # #     s = s + str(item)+"</br>"
    #     return HttpResponse(s)
    #
    #
    #
    #
    # # return  render(request,'pages/table_page01.html',(s))
        Data = {'Products': Product.objects.all()}
        return render(request, 'pages/table_page01.html', Data)

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'pages/detail.html', {'Products':product})



