from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import Product, OrderTiles
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    # T_type= Product.objects.filter('kitchen')
    # params= {'tiles':T_type}
    # return redirect(request, 'TilesTypes.html', params)
    a=""
    if request.method == 'POST':
        if request.POST.get("room"):
            # print('room')
            a = 'room'
        elif request.POST.get("kitchen"):
            # print('kitchen')
            a= 'kitchen'
        elif request.POST.get("bathroom"):
            # print('bathroom')
            a= 'bathroom'
        T_type= Product.objects.filter(Tiles_type= a)
        params= {'tiles':T_type} 
        return render(request, 'tilestypes.html', params)
    else:
        return render(request, 'home.html')

def tiles_type(request, typetile):
    print(typetile)
    a= typetile
    T_type= Product.objects.filter(Tiles_type= a)
    params= {'tiles':T_type} 
    return render(request, 'tilestypes.html', params)

    



def Tiles(request):
    allProd = []
    pro= Product.objects.values('Tiles_type', 'id')
    types= {item['Tiles_type'] for item in pro}
    for type in types:
        prod= Product.objects.filter(Tiles_type= type)
        n= len(prod)
        allProd.append([prod, range(1, n)])

    params = {'product': allProd}
    return render(request, 'tiles.html', params)

def TilesDetails(request,my_id):
    photoDetails= Product.objects.get(id= my_id)
    
    T_name= photoDetails.Tiles_name
    T_type= photoDetails.Tiles_type
    T_size= photoDetails.Tiles_size
    T_rate= photoDetails.Tiles_rate
    T_image= photoDetails.image
    # print(T_image)
    if request.method=='POST':
        try:
            Order_Tiles = OrderTiles.objects.get(Person_name=request.user.username,Person= request.user,Order_Tiles_name= T_name, 
                Order_Tiles_rate= T_rate , Order_Tiles_type= T_type,
                Order_Tiles_size= T_size, 
                Order_image= T_image
                )
            messages.error(request,"Order Already Exists!")
            return redirect('home')
        except:
            quantity= request.POST.get('quantity')
            mobile_number= request.POST.get('mobile_number')
            address = request.POST.get('address')
            if(len(mobile_number)!=10):
                messages.error(request, "enter valid mobile number")
                return redirect('home')
            Order_Tiles = OrderTiles.objects.create(Person_name=request.user.username,Person= request.user,Order_Tiles_name= T_name, 
            Order_Tiles_rate= T_rate , Order_Tiles_type= T_type,
            Order_Tiles_size= T_size, 
            Order_image= T_image,
            Order_Tiles_Quantity= quantity,
            Person_mobile_number= mobile_number,
            Person_address= address
            )
            messages.success(request, "your order submitted sucessfully")
        return redirect('home')
    params = {'photo' :photoDetails}
    return render(request, 'TilesDetails.html', params)


def YourOrder(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    Your_Order= OrderTiles.objects.filter(Person=request.user)
    params ={'photo':Your_Order}
    if request.method == "POST":
        remove= OrderTiles.objects.filter(Person=request.user)
        # x= OrderTiles.objects.get(id=remove.id)
        # remove.delete()
        # print(remove)
    return render(request, 'order.html', params)


def MyOrder(request):
    T_Order= OrderTiles.objects.all()
    params = {'order': T_Order}
    # print(T_Order)
    return render(request, 'MyOrder.html', params)


def userdeleteform(request, my_id):
    try:
        O_delete = OrderTiles.objects.get(id= my_id)
    except:
        raise Http404
    params= {'order': O_delete}
    if request.method=='POST':
        x = OrderTiles.objects.get(id= my_id)
        x.delete()
        # print(x)
        messages.success(request ,"Your order deleted successfully")
        return redirect('home')
    return render(request,'UserOrderDelete.html', params)


def aboutus(request):
    return render(request, 'about.html')