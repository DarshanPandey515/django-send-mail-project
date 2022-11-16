from django.shortcuts import render,redirect
from app.helpers import send_contact_mail
# Create your views here.



def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        facebook = request.POST.get('facebook')
        income = request.POST.get('income')
        message = request.POST.get('message')
        send_contact_mail(username=username,email=email,facebook=facebook,income=income,message=message)
        return redirect('success')
    return render(request,'index.html')


def success(request):
    return render(request,'success.html')