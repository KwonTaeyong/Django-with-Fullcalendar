from django.shortcuts import render, HttpResponse
from ..models import Category, Packing, Factory, Product
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm




def datalist(request):
    product_list = Product.objects.all()
    packing_list = Packing.objects.all()
    factory_list = Factory.objects.all()

    productlist = []
    for i in product_list:
        product = i.name
        productlist.append(product)

    print(list(productlist))
    context = {
        'packing_list': packing_list,
        'factory_list': factory_list,
        'product_list': product_list,
    }



    return render(request, 'B2C/datalist.html', context)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('B2C/datalist.html')
    else:
        form = UserForm()
    return render(request, 'B2C/datalist.html', {'form': form})

