from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth 
from .models import Customer,Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm , ExtendedCreateUserForm ,OrderForm ,paymentForm ,OrderUpdateForm
from .decorators import unauthenticated_user, allowed_user , admin_only
from django.contrib.auth.models import Group
from .filters import OrderFilter



# Create your views here.
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        form = CreateUserForm()
        extendedregister_form = ExtendedCreateUserForm(request.POST)

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                password= form.cleaned_data.get('password1')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    profile = ExtendedUser.objects.create(user=request.user)


                    return redirect('profile')

    context = {'form':form}

    return render(request,'register.html', context)


@unauthenticated_user
def singin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.info(request, 'User name or Password incorrect ')
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')



@login_required(login_url ='singin')

def dashboard(request):
    
    payment_taka = 0
    order = Order.objects.filter(user=request.user.id)

    my_filter = OrderFilter(request.GET, queryset=order)
    order= my_filter.qs


    pay = payment.objects.filter(user=request.user.id)
    # my_pay = OrderFilter(request.GET, queryset=pay)
    # pay= my_pay.qs
 
    
    for p in pay:
        payment_taka = p.payment

    number_order = order.exclude(status='new order').count()
    sell = 0
    cost = 0
    
    
    INTRANSIT = order.filter(status='Out for delivery').count()
    delivered = order.filter(status='Delivered').count()
    new_order = order.filter(status='new order').count()
    hold = order.filter(status='hold').count()
    Return = order.filter(status='Return').count()

    all_order = order.filter(status='Delivered')
    for ord in all_order:

        sell = sell+ ord.condition
        cost = cost + ord.delivery_cost
    balance = sell-cost-payment_taka


    if request.method == 'POST':
        balance = 0
        payment_taka = 0
        print('get')



    context = {'number_order':number_order, 'delivered':delivered,'INTRANSIT':INTRANSIT, 'new_order':new_order,'hold':hold,'Return':Return ,'sell':sell, 'cost':cost ,'balance':balance, 'payment_taka':payment_taka}
    return render (request, 'dashboard.html',context)



@login_required(login_url ='singin')
@admin_only
@allowed_user(allowed_roles='admin')
def admin(request):
    new_order = Order.objects.filter(status='new order').count()
    hold = Order.objects.filter(status='hold').count()
    INTRANSIT = Order.objects.filter(status='Out for delivery').count()
    delivered = Order.objects.filter(status='Delivered').count()

    all_order = Order.objects.exclude(status='new order').order_by('-order_date1')

    header_name = 'All Collected Order'

    context={'new_order':new_order,'delivered':delivered,'INTRANSIT':INTRANSIT,'hold':hold,'all_order':all_order,'header_name':header_name }

    return render(request,'admin.html',context)


@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def new_order_admin(request):
    new_order = Order.objects.filter(status='new order').count()
    hold = Order.objects.filter(status='hold').count()
    INTRANSIT = Order.objects.filter(status='Out for delivery').count()
    delivered = Order.objects.filter(status='Delivered').count()

    all_order = Order.objects.filter(status='new order')
    header_name = 'All New Order'

    context={'new_order':new_order,'delivered':delivered,'INTRANSIT':INTRANSIT,'hold':hold,'all_order':all_order,'header_name':header_name }

    return render(request,'admin.html',context)


@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def deliver(request):
    new_order = Order.objects.filter(status='new order').count()
    hold = Order.objects.filter(status='hold').count()
    INTRANSIT = Order.objects.filter(status='Out for delivery').count()
    delivered = Order.objects.filter(status='Delivered').count()

    all_order = Order.objects.filter(status='Delivered')
    header_name = 'All Delivery'

    context={'new_order':new_order,'delivered':delivered,'INTRANSIT':INTRANSIT,'hold':hold,'all_order':all_order,'header_name':header_name }

    return render(request,'admin.html',context)


@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def hold(request):
    new_order = Order.objects.filter(status='new order').count()
    hold = Order.objects.filter(status='hold').count()
    INTRANSIT = Order.objects.filter(status='Out for delivery').count()
    delivered = Order.objects.filter(status='Delivered').count()

    all_order = Order.objects.filter(status='hold')
    header_name = 'All Hold'

    context={'new_order':new_order,'delivered':delivered,'INTRANSIT':INTRANSIT,'hold':hold,'all_order':all_order,'header_name':header_name }

    return render(request,'admin.html',context)

@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def in_transit(request):
    new_order = Order.objects.filter(status='new order').count()
    hold = Order.objects.filter(status='hold').count()
    INTRANSIT = Order.objects.filter(status='Out for delivery').count()
    delivered = Order.objects.filter(status='Delivered').count()

    all_order = Order.objects.filter(status='Out for delivery')
    header_name = 'Out for delivery'

    context={'new_order':new_order,'delivered':delivered,'INTRANSIT':INTRANSIT,'hold':hold,'all_order':all_order,'header_name':header_name }

    return render(request,'admin.html',context)



@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderUpdateForm(instance=order)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin')

    context ={
        'form': form
    }
    return render (request,'updatepage.html' ,context)


@login_required(login_url ='singin')
def send_parcel(request):
    task_form = OrderForm
    if request.method == "POST":
        task_form=OrderForm(data=request.POST)
        if task_form.is_valid():

            task=task_form.save(commit=False)
            task.user= request.user
            task.save()
            return redirect('order_confirm')


    
    context ={
        'task_form':task_form
    }
    return render(request,'send.html',context)


@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def active_user(request):
    all_user = ExtendedUser.objects.all()


    context= {'all_user':all_user}
    return render (request,'all_user.html', context)

@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def payments(request,pk):
    sell = 0
    cost = 0
    pay = 0
    name= ''
    # taka = get_object_or_404(payment, user=pk)
    try:
            taka = payment.objects.get(user=pk)
            pay = taka.payment  
    except:
        pass

    order = Order.objects.filter(user=pk)
    
           
    all_order = order.filter(status='Delivered')
    
    for ord in all_order:
        sell = sell+ ord.condition
        cost = cost + ord.delivery_cost
        name = ord.user

    balance = sell-cost-pay

    context={'all_order':all_order,'balance':balance,'sell':sell,'cost':cost,'pay':pay,'name':name}
    

    return render (request, 'payment.html', context)



 
@login_required(login_url ='singin')
@allowed_user(allowed_roles='admin')
def make_payment(request,pk):

    if request.method == "POST":
        new = int(request.POST['new'])
        print(new)

        task= payment.objects.get_or_create(user_id=pk)

        if request.method == "POST":
            new = int(request.POST['new'])
            print(new)
    
            task= payment.objects.get(user=pk)
            task.payment = task.payment + new
            task.save()
            return redirect('active_user')
    
    # context ={'form':form }

    return render(request, 'make_payment.html')

 

# hoy nai  akhono   
def make_order(request):

    form = OrderForm
    
    if request.method == 'POST':
        form = OrderForm
        if form.is_valid():
            form.save()
            return redirect('make_parcel')
    context ={'form':form}
    return render (request,'make_order.html', context)




@login_required(login_url ='singin')
def new_order(request): 
    name = request.user
    header_name = '\'s all New Order s'
    order = Order.objects.filter(user=request.user.id)


    all_order = order.filter(status='new order').order_by('-date_created')

           
    # all_order = order.filter(status='new order').order_by('-order_date1')
        
    context={'all_order':all_order,'header_name':header_name, 'name':name}
    
    return render (request,'delevered_parcel_list.html',context)

@login_required(login_url ='singin')
def all_order_user(request):
    name = request.user
    header_name = '\'s all times Orders'
    order = Order.objects.filter(user=request.user.id)
           
    all_order = order.exclude(status='new order').order_by('-order_date1')
        
    context={'all_order':all_order,'header_name':header_name, 'name':name}
    
    return render (request,'old_percel_user.html',context)



@login_required(login_url ='singin')
def profile(request):
    old= ExtendedUser.objects.get(user_id=request.user.id)
    form = ExtendedCreateUserForm(instance=old)

    if request.method == 'POST':
        form = ExtendedCreateUserForm(request.POST, request.FILES, instance=old)
        if form.is_valid():
            task = form.save(commit=False)
            task.user= request.user
            task.save()
            return redirect('dashboard')

    pic = old.profile_pic
    context ={'form':form, 'pic' : pic}
    return render(request, 'profile.html' , context)


def track(request):
    not_Found = False
    number = request.POST.get('order')
    try:
        track_product = Order.objects.get(order_id=number)
        shop_name = ExtendedUser.objects.get(user=track_product.user.id)
        

    except:
        track_product =[]
        shop_name = ''
        not_Found = True

    context = {
        'shop_name' :shop_name,
       'track_product' : track_product,
        'not_Found' : not_Found
    }
    return render(request,'track.html', context)


# user page user new order delete
@login_required(login_url ='singin')

def delete_order(request,pk):
    print(pk)
    order = Order.objects.get(id = pk)
    print(order.receiver_name)
    order.delete()
    return redirect('dashboard')

@login_required(login_url ='singin')
def Update_order_user(request,pk):
    update=True
    order = Order.objects.get(id = pk)
    task_form= OrderForm(instance=order)
    if request.method == "POST":
        task_form=OrderForm(data=request.POST , instance=order)
        if task_form.is_valid():

            task=task_form.save(commit=False)
            task.user= request.user
            task.save()
            return redirect('order_confirm')

    context = {
        'task_form':task_form,
        'update':update
    }
    return render(request, 'send.html', context)



@login_required(login_url ='singin')
def order_confirm(request):
    all_order = Order.objects.filter(user=request.user).last()
    av = Order.objects.filter(user=request.user).last()
    print(all_order.order_id)
    print(av.order_id)


    number = all_order.order_id
    context ={
        'number': number
    }
    return render(request, 'order_confirm.html' , context)



def test(request):
    return render(request, 'test.html')


