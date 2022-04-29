from django.shortcuts import render, redirect, HttpResponse
from ..models import Order_list
import requests
import xmltodict
import json
from django.db.models import Q
from datetime import datetime


def orderlist(request):
    today = datetime.today()
    aboxcount = Aboxcount()
    context = {
        'today': today,
        'aboxcount': aboxcount
    }
    return render(request, 'B2C/orderlist.html', context)


def Aboxcount():
    datadict = dict()
    today = datetime.now().date()
    order_list = Order_list.objects.all()

    datadict['11'] = len(order_list.filter(~Q(RECEIVE_ADDR__regex='[가-힣]+')))
    datadict['12'] = len(order_list.filter(Q(RECEIVE_ADDR__icontains='제주') & Q(scm_status='주문수집')))
    datadict['13'] = ''

    datadict['21'] = len(order_list.filter(
        Q(HOPE_DELV_DATE__gt=today.strftime('%Y%m%d')) &
        Q(scm_status='주문수집') &
        ~Q(RECEIVE_ADDR__icontains='제주') &
        Q(RECEIVE_ADDR__regex='[가-힣]+')
    ))

    datadict['22'] = len(order_list.filter(
        Q(HOPE_DELV_DATE__lte=today.strftime('%Y%m%d')) &
        Q(scm_status='주문수집') &
        ~Q(RECEIVE_ADDR__icontains='제주') &
        Q(RECEIVE_ADDR__regex='[가-힣]+')
    ))

    datadict['23'] = len(order_list.filter(scm_status='작업지시'))
    return datadict


def date_trans(date):
    result = None
    if date:
        result = datetime.strptime(date, '%Y%m%d%H%M%S')
    return result


def update_order(request):
    order_db = Order_list.objects.all()
    order_list = get_order()
    for order in order_list:
        if not order_db.filter(IDX=order['IDX']):
            Order_list(
                IDX=order['IDX'],
                ORDER_ID=order['ORDER_ID'],
                MALL_ID=order['MALL_ID'],
                ORDER_STATUS=order['ORDER_STATUS'],
                scm_status="주문수집",
                PAY_COST=order['PAY_COST'],
                ORDER_DATE=date_trans(order['ORDER_DATE']),
                MALL_PRODUCT_ID=order['MALL_PRODUCT_ID'],
                PRODUCT_NAME=order['PRODUCT_NAME'],
                SKU_VALUE=order['SKU_VALUE'],
                item_id=None,
                item_name=None,
                item_quan=None,
                DELIVERY_METHOD_STR=order['DELIVERY_METHOD_STR'],
                DELV_COST=order['DELV_COST'],
                P_EA=order['P_EA'],
                REG_DATE=date_trans(order['REG_DATE']),
                ORD_CONFIRM_DATE=date_trans(order['ORD_CONFIRM_DATE']),
                RTN_DT=date_trans(order['RTN_DT']),
                CHNG_DT=date_trans(order['CHNG_DT']),
                DELIVERY_CONFIRM_DATE=date_trans(order['DELIVERY_CONFIRM_DATE']),
                CANCEL_DT=date_trans(order['CANCEL_DT']),
                DELIVERY_ID=order['DELIVERY_ID'],
                INVOICE_NO=order['INVOICE_NO'],
                INV_SEND_MSG=order['INV_SEND_MSG'],
                INV_SEND_DM=date_trans(order['INV_SEND_DM']),
                USER_ID=order['USER_ID'],
                USER_NAME=order['USER_NAME'],
                USER_TEL=order['USER_TEL'],
                USER_CEL=order['USER_CEL'],
                RECEIVE_NAME=order['RECEIVE_NAME'],
                RECEIVE_TEL=order['RECEIVE_TEL'],
                RECEIVE_CEL=order['RECEIVE_CEL'],
                RECEIVE_ZIPCODE=order['RECEIVE_ZIPCODE'],
                RECEIVE_ADDR=order['RECEIVE_ADDR'],
                DELV_MSG=order['DELV_MSG'],
                HOPE_DELV_DATE=order['HOPE_DELV_DATE'],
            ).save()

    return redirect('B2C:orderlist')


def order_xml(request):
    today = datetime.today().strftime("%Y%m%d")
    stat = '002'
    context = {
        '<SABANG_ORDER_LIST>'
        '<HEADER>'
        '<SEND_COMPAYNY_ID>eunha</SEND_COMPAYNY_ID>'
        '<SEND_AUTH_KEY>3ZSRNyAuE2C39SS65XAW82HTE3rb5GrGGy</SEND_AUTH_KEY>'
        '</HEADER>'
        '<DATA>'
        f'<ORD_ST_DATE>{today}</ORD_ST_DATE>'
        f'<ORD_ED_DATE>{today}</ORD_ED_DATE>'
        '<ORD_FIELD>'
        f'<![CDATA[ IDX|ORDER_ID|MALL_ID|ORDER_STATUS|PAY_COST|ORDER_DATE|MALL_PRODUCT_ID|PRODUCT_NAME|SKU_VALUE|DELIVERY_METHOD_STR|DELV_COST|P_EA|REG_DATE|ORD_CONFIRM_DATE|RTN_DT|CHNG_DT|DELIVERY_CONFIRM_DATE|CANCEL_DT|DELIVERY_ID|INVOICE_NO|INV_SEND_MSG|INV_SEND_DM|USER_ID|USER_NAME|USER_TEL|USER_CEL|RECEIVE_NAME|RECEIVE_TEL|RECEIVE_CEL|RECEIVE_ZIPCODE|RECEIVE_ADDR|DELV_MSG|HOPE_DELV_DATE ]]>'
        '</ORD_FIELD>'
        f'<ORDER_STATUS>{stat}</ORDER_STATUS>'
        '</DATA>'
        '</SABANG_ORDER_LIST>'
    }
    return HttpResponse(context, content_type="text/xml")


def get_order():
    url = 'https://r.sabangnet.co.kr/RTL_API/xml_order_info.html?xml_url=http://eunha.nowonlab.com/api/order.xml'
    res_xml = requests.get(url).content.decode('euc-kr')
    res_dict = xmltodict.parse(res_xml)
    res_json = json.loads(json.dumps(res_dict))
    order_list = res_json['SABANG_ORDER_LIST']['DATA']
    return order_list
