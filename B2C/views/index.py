import re

from django.shortcuts import render, HttpResponse
from datetime import datetime
from ..models import Order_list, Factory, Category, Packing, Product

def main(request):
    today0 = datetime.now().date()
    today = datetime.today()
    order_list = Order_list.objects.all()
    # order_list = order_list.filter(ORDER_DATE__range=[today0, today])
    product_list = Product.objects.all()
    factory_list = Factory.objects.all()

    factorylist = []
    for i in factory_list:
        name = i.name
        factorylist.append(name)

    createlist = []
    for i in factory_list:
        create = i.create_date
        createlist.append(create)

    j = list(createlist)

    for i in range(len(j)):
        j[i] = str(j[i])

    date_time = []
    for i in j:
        date_time.append(i[:10])

    plus = list(zip(date_time,factorylist))
    print(plus)


    namelist = []
    ranklist = []

    for i in product_list:
        name = i.name
        namelist.append(name)

    for i in product_list:
        rank = i.rank
        ranklist.append(rank)



    test_list = {}

    for i in product_list:
        if i.name not in test_list:
            test_list[i.name] = 0
        test_list[i.name] += i.rank




    malllist = []
    shoplist = []
    datelist = []

    for iloc in order_list:
        mall = iloc.MALL_ID
        malllist.append(mall)
    for shop in order_list:
        pay = shop.PAY_COST
        shoplist.append(pay)
    for date in order_list:
        check = date.ORDER_DATE
        datelist.append(check)
    for i in range(len(datelist)):
        datelist[i] = str(datelist[i])

    shoplist = list(shoplist)
    malllist = list(malllist)
    c = list(datelist)

    date_list = []
    for i in c:
        date_list.append(i[:10])


    testlist = {}

    for i in order_list:
        if i.MALL_ID not in testlist:
            testlist[i.MALL_ID] = 0
        testlist[i.MALL_ID] += i.PAY_COST

    x = testlist.keys()
    c = testlist.values()

    a = list(x)
    b = list(c)



    context = {
        'today0': today0,
        'order_list': Order_list.objects.all(),
        'product' : Product.objects.all(),
        'factory' : Factory.objects.all(),
        'labels': a,
        'data': b,
        'date': date_list,
        'rank': ranklist,
        'name': namelist,
        'factory_list': factorylist,
        'creaet_list': date_time,
    }


    return render(request, 'B2C/index.html', context)

