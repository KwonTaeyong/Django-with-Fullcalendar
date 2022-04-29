from django.shortcuts import redirect
from ..models import Order_list, Work_list, Category, Product, Factory
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from B2C.serializers.B2C_serializer import OrderlistSerializer, ProductSerializer, CategorySerializer, FactorySerializer
from datetime import datetime, timedelta
from django.db.models import Q


class Table(APIView):
    def get(self, request):
        req = request.GET

        x = {
            "result": 'false',
            "data": {
            }
        }

        ## action 값에 따라 api 작동
        if req.get('action') == 'getorderlisttable':  ## 검색 시
            order_list = Order_list.objects.order_by('-REG_DATE')
            serializer = OrderlistSerializer(order_list, many=True)
            x = {
                "result": 'true',
                "data": {
                    "contents": serializer.data,
                }
            }

        if req.get('action') == 'getorderlisttablebtn':
            order_list = Order_list.objects.order_by('-REG_DATE')
            today = datetime.now().date()

            ## 출고일 지정
            if req.get('state') == '21':
                order_list = order_list.filter(
                    Q(HOPE_DELV_DATE__gt=today.strftime('%Y%m%d')) &
                    Q(scm_status='주문수집') &
                    ~Q(RECEIVE_ADDR__icontains='제주') &
                    Q(RECEIVE_ADDR__regex='[가-힣]+')
                )

            ## 제주, 소스
            if req.get('state') == '22':
                order_list = order_list.filter(
                    Q(HOPE_DELV_DATE__lte=today.strftime('%Y%m%d')) &
                    Q(scm_status='주문수집') &
                    ~Q(RECEIVE_ADDR__icontains='제주') &
                    Q(RECEIVE_ADDR__regex='[가-힣]+')
                )

            if req.get('state') == '23':
                order_list = order_list.filter(scm_status='작업지시')


            if req.get('state') == '11':
                order_list = order_list.filter(~Q(RECEIVE_ADDR__regex='[가-힣]+'))

            if req.get('state') == '12':
                order_list = order_list.filter(Q(RECEIVE_ADDR__icontains='제주') & Q(scm_status='주문수집'))

            if req.get('state') == '13':
                order_list = []


            serializer = OrderlistSerializer(order_list, many=True)
            x = {
                "result": 'true',
                "data": {
                    "contents": serializer.data,
                }
            }

        if req.get('action') == 'searchdata':
            if req.get('statelist[]'):
                order_list = Order_list.objects.order_by('-REG_DATE')
                order_list = order_list.filter(
                    Q(scm_status__in=req.getlist('statelist[]')) &
                    ~Q(RECEIVE_ADDR__icontains='제주') &
                    Q(RECEIVE_ADDR__regex='[가-힣]+')
                )
                ## 주문 기간
                if req.get('date1') and req.get('date2'):
                    date2 = datetime.strptime(req.get('date2'), '%Y-%m-%d') + timedelta(hours=23, minutes=59,
                                                                                        seconds=59.9, milliseconds=99)
                    order_list = order_list.filter(REG_DATE__range=[req.get('date1'), date2])

                if req.get('date1'):
                    order_list = order_list.filter(REG_DATE__gte=req.get('date1'))

                if req.get('date2'):
                    date2 = datetime.strptime(req.get('date2'), '%Y-%m-%d') + timedelta(hours=23, minutes=59,
                                                                                        seconds=59.9, milliseconds=99)
                    order_list = order_list.filter(REG_DATE__lte=date2)


                ## 검색어
                if req.get('kw'):
                    KW = req.get('kw')
                    order_list = order_list.filter(Q(IDX__icontains=KW) |
                                                   Q(MALL_ID__icontains=KW) |
                                                   Q(PRODUCT_NAME__icontains=KW) |
                                                   Q(SKU_VALUE__icontains=KW) |
                                                   Q(RECEIVE_NAME__icontains=KW) |
                                                   Q(USER_NAME__icontains=KW)
                                                   ).distinct()

            else:
                order_list = []

            serializer = OrderlistSerializer(order_list, many=True)
            x = {
                "result": 'true',
                "data": {
                    "contents": serializer.data,
                }
            }

        if req.get('action') == 'getmodalajax':  ## orderlist의 모달 데이터
            data = Order_list.objects.get(IDX=req.get('data'))
            serializer = OrderlistSerializer(data)
            return JsonResponse(serializer.data)

        return Response(x)

    def post(self, request):
        req = request.POST
        if req.get('action') == 'updateorder':
            tdata = Order_list.objects.get(id=req.get('id'))
            self.update_dict(tdata, save_update=True, **req)

        ## 상태 변셩
        if req.get('action') =='postdata':
            result = {'result': 'false'}

            if req.get('state') == '작업지시':
                workform = Work_list(checker=req.get('user'))
                workform.save()
                for iloc in req.getlist('idlist[]'):
                    tdata = Order_list.objects.get(id=iloc)
                    tdata.scm_status = req.get('state')
                    tdata.save()
                    workform.order.add(iloc)


                result = {'result': 'true'}

            if req.get('state') == '주문수집':
                for iloc in req.getlist('idlist[]'):
                    tdata = Order_list.objects.get(id=iloc)
                    tdata.scm_status = req.get('state')
                    tdata.save()

                result = {'result': 'true'}

            return JsonResponse(result)

        return redirect('B2C:orderlist')

    def update_dict(self, model, save_update=True, **kwargs):
        for attr, val in kwargs.items():
            if val[0]:
                setattr(model, attr, val[0])
                if attr == "HOPE_DELV_DATE":
                    setattr(model, attr, val[0].replace('-', ''))
        if save_update:
            model.save()



class gridTable(APIView):
    def get(self, request):

        req = request.GET
        print(req)
        result = {
            "result": 'false',
            "data": {
                "contents": []
            }
        }

        ## 작업 관리 메인
        if req.get('action') == 'getworklisttable':
            idlist = req.getlist('idlist[]')
            data = Work_list.objects.filter(id__in=idlist)
            datalist = []
            for iloc in data:
                for iloc2 in iloc.order.all():
                    datalist.append(iloc2)

            serializer = OrderlistSerializer(datalist, many=True)

            result = {
                "result": 'true',
                "data": {
                    "contents": serializer.data,
                }
            }

        ## 목록형
        if req.get('action') == 'getgridlistdata':
            result = {
                "result": 'true',
                "data": {
                    "contents": []
                }
            }

        if req.get('action') == 'categorygrid':
            data = Category.objects.order_by('rank')
            serializer = CategorySerializer(data, many=True)
            result = {
                "result": 'true',
                "data": {
                    "contents": serializer.data,
                }
            }

        if req.get('action') == 'productgrid':
            if req.get('catid'):
                data = Product.objects.order_by('rank').filter(category=req.get('catid'))
                serializer = ProductSerializer(data, many=True)
                result = {
                    "result": 'true',
                    "data": {
                        "contents": serializer.data,
                    }
                }

        if req.get('action') == 'factorygrid':
            data = Factory.objects.all()
            serializer = FactorySerializer(data, many=True)
            result = {
                "result": 'true',
                "data": {
                    "contents": serializer.data,
                }
            }




        return Response(result)

    def post(self, request):


        return redirect('B2C:worklist')
