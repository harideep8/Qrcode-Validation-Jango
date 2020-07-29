from django.shortcuts import render
import random
import qrcode
# Create your views here.
otp=0
def openloginpage(request):
    return render(request,'testapp/login.html')

def validateuser(request):
    username=request.POST.get('t1')
    password=request.POST.get('t2')
    if username=="Harideep" and password=="Harideep8@":
        rno=random.randint(1000,9999)
        global otp
        otp=rno
        im=qrcode.make("OTP: "+str(rno))
        im.save('testapp/static/qrimages/hari.jpg')
        return render(request,'testapp/qrcode.html')
    else:
        return render(request,'testapp/login.html',{'message':"Invalid Username or Password"})

def validateotp(request):
    user=request.POST.get('otp')
    if int(user)==otp:
        name="harideep"
        age="25"
        im1=qrcode.make("Name: "+name+"\n"+"Age:"+age)
        im1.save('testapp/static/qrimages/hari1.jpg')
        return render(request,'testapp/welcome.html')
    else:
        return render(request,'testapp/login.html',{'message':"Invalid OTP"})
