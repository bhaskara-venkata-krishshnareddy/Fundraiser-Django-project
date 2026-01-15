
from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import *
from django.contrib import messages
from django.db.models import Sum
from fundraiser.BlockcahinAlgo import HashDataBlock

# Create your views here.


def home2(request):
    livelihood = FundRaiserModel.objects.filter(cause="Livelihood", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    health = FundRaiserModel.objects.filter(cause="Health", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    education = FundRaiserModel.objects.filter(cause="Education", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()

    return render(request, 'user/index2.html', {'livelihood': livelihood, 'health': health, 'education': education})


def about(request):
    livelihood = FundRaiserModel.objects.filter(cause="Livelihood", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    health = FundRaiserModel.objects.filter(cause="Health", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    education = FundRaiserModel.objects.filter(cause="Education", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    return render(request, 'user/about.html', {'livelihood': livelihood, 'health': health, 'education': education})


def login(request):
    if request.method == 'POST':

        gmail = request.POST.get('email')
        password = request.POST.get('password')

        try:
            check = UserModel.objects.get(gmail=gmail, password=password)

            request.session['signup_id'] = check.signup_id
            messages.success(request, "Your Are Successfully Logged")
            return redirect('userdashboard')

        except:
            messages.error(request, "Your Email or Password Given Worng")
            return redirect('login')

    return render(request, 'user/login.html')


def contact(request):
    if request.method == 'POST':
        feedback_name = request.POST.get('feedback_name')
        feedback_cause = request.POST.get('feedback_cause')
        feedback_email = request.POST.get('feedback_email')
        feedbacks = request.POST.get('feedbacks')

        FeedbackModel.objects.create(feedback_name=feedback_name, feedback_email=feedback_email,
                                     feedback_cause=feedback_cause, feedbacks=feedbacks)

    return render(request, 'user/contact.html')


def livehood(request):

    livelihood = FundRaiserModel.objects.filter(cause="Livelihood", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    data = FundRaiserModel.objects.filter(cause="Livelihood", status="Accepted").exclude(
        price="0").order_by('-submitted_date')

    return render(request, 'user/livehood.html', {'data': data, 'cause': livelihood})


def health(request):
    health = FundRaiserModel.objects.filter(cause="Health", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    data = FundRaiserModel.objects.filter(cause="Health", status="Accepted").exclude(
        price='0').order_by('-submitted_date')

    return render(request, 'user/health.html', {'data': data, 'cause': health})


def education(request):
    education = FundRaiserModel.objects.filter(cause="Education", status="Accepted").order_by('-submitted_date').exclude(price="0").first()
    data = FundRaiserModel.objects.filter(cause="Education", status="Accepted").order_by(
        '-submitted_date').exclude(price='0')

    return render(request, 'user/education.html', {'data': data, 'cause': education})


def userdashboard(request):
    livelihood = FundRaiserModel.objects.filter(cause="Livelihood", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    health = FundRaiserModel.objects.filter(cause="Health", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()
    education = FundRaiserModel.objects.filter(cause="Education", status="Accepted").order_by('-submitted_date').values(
        "cause", "title", "upload_image", "fund_price", "fund_id", "describtion", "raisefundfor", "gmail", "phone_number", "price").exclude(price="0").first()

    return render(request, 'user/user-dashboard.html', {'livelihood': livelihood, 'health': health, 'education': education})


def userfeedback(request):
    user = request.session["signup_id"]
    try:
        obj = get_object_or_404(FundRaiserModel, fund_raiser=user)
    except:
        messages.info(request, 'You have not applied for any Fund raising')
        return redirect('fundrasing')
   

    if request.method == 'POST':
        user_cause = request.POST.get('user_cause')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_feedbacks = request.POST.get('user_feedbacks')

        FeedbackModel.objects.create(
            user_feedbacks=user_feedbacks, user_name=user_name, user_email=user_email, user_cause=user_cause)

    return render(request, 'user/user-feedback.html', {'f': obj})


def userfund(request):
    user = request.session["signup_id"]
    try:
        obj = get_object_or_404(FundRaiserModel, fund_raiser=user)
    except:
        messages.info(request, 'You have not applied for any Fund raising')
        return redirect('fundrasing')

    # data2 = FundRaiserModel.objects.filter(fund_id=obj).values('price')

    data = PaymentModel.objects.filter(fund_id=obj)
    data3 = PaymentModel.objects.filter(fund_id=obj).aggregate(payment=Sum('amount'))
    amount = data3['payment']

    

    return render(request, 'user/user-funds.html', {'data': data,'fund':obj,'payments':amount})


def userprofile(request):
    user = request.session["signup_id"]
 
    try:
        obj = get_object_or_404(FundRaiserModel, fund_raiser=user)
    except:
        messages.info(request, 'You have not applied for any Fund raising')
        return redirect('fundrasing')
    if request.method == 'POST' and request.FILES['upload_image']:

        name = request.POST['Name']
        relation = request.POST['relation']
        phone_number = request.POST['phone_number']
        gmail = request.POST['email']
        describtion = request.POST['describtion']

        title = request.POST['title']

        upload_image = request.FILES['upload_image']

        cause = request.POST['cause']
        raisefundfor = request.POST['raisefundfor']

        obj.name = name
        obj.relation = relation

        obj.phone_number = phone_number
        obj.gmail = gmail
        obj.upload_image = upload_image
        obj.describtion = describtion

        obj.title = title

        obj.cause = cause
        obj.raisefundfor = raisefundfor
        obj.save(update_fields=['name', 'relation', 'phone_number', 'gmail',
                 'describtion', 'title', 'cause', 'raisefundfor', 'upload_image'])

    return render(request, 'user/user-profile.html', {'i': obj})


def donate(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        gmail = request.POST.get('email')
        country = request.POST.get('country')
        phonenumber = request.POST.get('tel')
        # debitcard
        cardholder_name = request.POST.get('cardholder_name')
        cardnumber = request.POST.get('cardnumber')
        startmonth = request.POST.get('start')
        expiarydate = request.POST.get('expiary')
        cvv = request.POST.get('cvv')
        amount = request.POST.get('amount')
        # creditcard

        # netbanking
        selectbank = request.POST.get('selectbank')
        username = request.POST.get('username')
        password = request.POST.get('password')

        PaymentModel.objects.create(username=username, amount=amount, password=password, selectbank=selectbank, cardholder_name=cardholder_name,
                                    cardnumber=cardnumber, startmonth=startmonth, expiarydate=expiarydate, cvv=cvv, name=name, gmail=gmail, country=country, phno=phonenumber)
        
    return render(request, 'user/donate.html')


def verify_blockchain(request,id):
    obj = FundRaiserModel.objects.get(fund_id=id)
    key = "58d4y51oiwqa6s5pjn75@"

    #Creating Initial block
    initial_block = HashDataBlock(key, [obj.raisefundfor])
    print(initial_block.block_hash, 'hash')

    #Creating Second block
    second_block = HashDataBlock(initial_block.block_hash, [str(obj.fund_price)])
    print (second_block.block_hash)

    #Creating Third block
    third_block = HashDataBlock(second_block.block_hash, [str(obj.price)])
    print (third_block.block_hash)

    if obj.raisefundfor_block == initial_block.block_hash \
    and obj.fund_price_block == second_block.block_hash \
    and obj.price_block == third_block.block_hash:
        # messages.success(request, "This is a valid Image")
        return render(request, 'user/block-verify.html',{
            'status':'true',
            'data':obj,
            'block1':initial_block.block_hash,
            'block2':second_block.block_hash,
            'block3':third_block.block_hash
            })
    else:
        # messages.error(request, "This Image has been Tampered")
        return render(request, 'user/block-verify.html',{
            'status':'false',
            'data':obj,
            'block1':initial_block.block_hash,
            'block2':second_block.block_hash,
            'block3':third_block.block_hash
            })
    # return render(request, 'user/block-verify.html',{'data':obj})


def donateaction(request, id):
    data1 = FundRaiserModel.objects.get(fund_id=id)
    price_1 = int(data1.price)
    if request.method == 'POST':
        name = request.POST.get('fname')
        gmail = request.POST.get('email')
        country = request.POST.get('country')
        phonenumber = request.POST.get('tel')
        cardholder_name = request.POST.get('cardholder_name')
        cardnumber = request.POST.get('cardnumber')
        amount = request.POST.get('amount')

        price_2 = int(amount)

 
        if price_2 < price_1 or price_2 == price_1:
            data1.price = price_1 - price_2
            data1.save(update_fields=['price'])
            data1.save()
            PaymentModel.objects.create(cardholder_name=cardholder_name, cardnumber=cardnumber,
                                        amount=amount, fund_id=data1, name=name, gmail=gmail, country=country, phno=phonenumber)
            key = '58d4y51oiwqa6s5pjn75@'
            intitalblock = HashDataBlock(key,[str(data1.raisefundfor)])

            second_block = HashDataBlock(intitalblock.block_hash, [str(data1.fund_price)])

            third_block = HashDataBlock(second_block.block_hash,[str(data1.price)])

            data1.raisefundfor_block = intitalblock.block_hash
            data1.fund_price_block = second_block.block_hash
            data1.price_block = third_block.block_hash
            data1.save()
            messages.success(request, "Your Payment is successful")
            return redirect('home2')

        else:
            messages.error(request, "please enter valid amount")
        return redirect('donateaction', id=id)

    return render(request, 'user/donate.html', {'donate': data1, 'left': price_1})


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        if UserModel.objects.filter(gmail=gmail).exists():
            messages.error(request, "Email Already Existed")
            return redirect("signup")
        else:
            user = UserModel.objects.create(
                name=name, gmail=gmail, password=password)
            user.save()
            messages.success(
                request, "Your Account Is Successfully Registered")
    return render(request, 'user/signup-form-user.html')


def fundrasing(request):
    user_id = request.session["signup_id"]

    user = UserModel.objects.get(pk=user_id)
    try:
        obj = FundRaiserModel.objects.get(fund_raiser=user)
        messages.error(request, 'You have already Raised fund')
        return redirect('userfund')
    except:
        pass
    if request.method == 'POST' and request.FILES['upload_proof'] and request.FILES['upload_doc'] and request.FILES['upload_image']:
        name = request.POST['Name']
        relation = request.POST['relation']
        phone_number = request.POST['phone_number']
        gmail = request.POST['email']
        upload_image = request.FILES['upload_image']
        upload_doc = request.FILES['upload_doc']
        upload_proof = request.FILES['upload_proof']
        describtion = request.POST['describtion']
        document_verification = request.POST['document_verification']
        title = request.POST['title']
        proof = request.POST['proof']
        gender = request.POST['gender']
        price = request.POST['fund_price']
        fund_price = request.POST['fund_price']
        cause = request.POST['cause']
        raisefundfor = request.POST['raisefundfor']

        obj = FundRaiserModel.objects.create(name=name, relation=relation, phone_number=phone_number, gmail=gmail,
                                        upload_image=upload_image, upload_proof=upload_proof, upload_doc=upload_doc,
                                        describtion=describtion, document_verification=document_verification, gender=gender,
                                        title=title, proof=proof, fund_price=fund_price, cause=cause, raisefundfor=raisefundfor,
                                        price=price,fund_raiser=user)
        key = '58d4y51oiwqa6s5pjn75@'
        intitalblock = HashDataBlock(key,[obj.raisefundfor])

        second_block = HashDataBlock(intitalblock.block_hash, [obj.fund_price])

        third_block = HashDataBlock(second_block.block_hash,[obj.price])

        obj.raisefundfor_block = intitalblock.block_hash
        obj.fund_price_block = second_block.block_hash
        obj.price_block = third_block.block_hash
        obj.save()

        messages.success(request, "Your Fund Registration Is Successful")
        return redirect('userfund')

    return render(request, 'user/user-fundraiser-register.html',{'user':user})
