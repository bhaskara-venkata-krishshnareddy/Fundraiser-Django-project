from django.shortcuts import render, redirect, get_object_or_404
from fundraiser.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from userapp.models import *

# Create your views here.

def adminhome(request):
    adminhome=FundRaiserModel.objects.all().order_by('-fund_id')
    count=FundRaiserModel.objects.filter(cause='Health').count()
    Livelihood=FundRaiserModel.objects.filter(cause='Livelihood').count()
    Education=FundRaiserModel.objects.filter(cause='Education').count()
    Total=count+Livelihood+Education
    return render(request,'admin/admin-index.html',{'adminhome':adminhome,'count':count,'Livelihood':Livelihood,'Education':Education,'Total':Total})

def raiser(request):
    raiser=FundRaiserModel.objects.all().order_by('-pk')
    return render(request,'admin/admin-view-raiser.html',{'raiser':raiser})

def funds(request):
    funds=FundRaiserModel.objects.all().order_by('-fund_id')
    return render(request,'admin/admin-view-funds.html',{'funds':funds})
    


def feedbacks(request):
    feedback=FeedbackModel.objects.all().order_by('-feedback_id')
    return render(request,'admin/admin-view-feedbacks.html',{'feedback': feedback})

def fundraiserprofile(request,id):
    data = get_object_or_404(FundRaiserModel,fund_id=id)  
    return render(request,'admin/raiserprofile.html',{'data':data})



#STATUS UPDATE

def fundraiserprofileaccept(request,id):
    data = get_object_or_404(FundRaiserModel,fund_id=id)
    data.status = 'Accepted'
    data.save(update_fields=['status'])
    data.save()
    print("this is accept")
    
    #email message
    html_content = "<br/> <p> fundraiser application has been successfully accepted</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.gmail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("fundraiser Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
        print("sent")
    
    
    
    return redirect('view_fundraisers')
    
def fundraiserprofilereject(request,id):
    accept = get_object_or_404(FundRaiserModel,fund_id=id)
    accept.status = 'Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    
     #email message
    html_content = "<br/> <p> fundraiser application has been Rejected so please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.gmail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("fundraiser Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
        print("sent")
    
    return redirect('view_fundraisers')


def adminlogin(request):
    if request.method=='POST':
        name=request.POST.get('username') 
        password=request.POST.get('password') 
        if name=='admin' and password=='admin':
            return redirect('admin_home')
    return render(request,'admin/login2.html')
