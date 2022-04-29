from django.shortcuts import render
from ..models import Order_list, Work_list
import json


def worklist(request):
    order_db = Order_list.objects.values()
    x = ref(order_db)
    work_list = Work_list.objects.all()
    order_list = Order_list.objects.order_by('-REG_DATE')
    order_list = order_list.filter(scm_status='작업지시')
    context = {
        'orderlist': x,
        'work_list': work_list,
        'order_list':order_list
    }

    return render(request, 'B2C/worklist.html', context)


def ref(orderlist):
    with open('ref.json', encoding='utf-8') as json_file:
        ref = json.load(json_file)
    res = []
    for order in orderlist:
        if order['SKU_VALUE'] == None:
            try:
                x = ref[order['PRODUCT_NAME']]
            except:
                continue
        else:
            try:
                x = ref[f"{order['PRODUCT_NAME']} /{order['SKU_VALUE']}"]
            except:
                try:
                    x = ref[f"{order['PRODUCT_NAME']}/ {order['SKU_VALUE']}"]
                except:
                    try:
                        x = ref[f"{order['PRODUCT_NAME']} / {order['SKU_VALUE']}"]
                    except:
                        continue
        order['카테고리'] = x['카테고리']
        order['품목'] = x['품목']
        order['구성품'] = x['구성품']
        order['증정'] = x['증정']

        res.append(order)
    return res


