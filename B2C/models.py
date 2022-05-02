from django.db import models
from django.contrib.auth.models import User


class Order_list(models.Model):
    IDX = models.CharField(max_length=100, null=True, blank=True)  # 사방넷 주문번호
    ORDER_ID = models.CharField(max_length=100, null=True, blank=True)  # 몰 주문번호
    MALL_ID = models.CharField(max_length=100, null=True, blank=True)  # 몰이름
    ORDER_STATUS = models.CharField(max_length=100)  # 주문상태
    scm_status = models.CharField(max_length=100, null=True, blank=True)  # scm 주문상태
    PAY_COST = models.IntegerField()  # 결제액
    ORDER_DATE = models.DateTimeField(null=True, blank=True)  # 몰 주문일자
    MALL_PRODUCT_ID = models.CharField(max_length=100, null=True, blank=True)  # 몰 상품코드
    PRODUCT_NAME = models.CharField(max_length=100, null=True, blank=True)  # 상품명
    SKU_VALUE = models.CharField(max_length=100, null=True, blank=True)  # 옵션명
    DELIVERY_METHOD_STR = models.CharField(max_length=100, null=True, blank=True)  # 배송방법
    DELV_COST = models.IntegerField(null=True, blank=True)  # 배송비
    P_EA = models.IntegerField(null=True, blank=True)  # 총 수량
    REG_DATE = models.DateTimeField(null=True, blank=True)  # 사방 수집일자
    ORD_CONFIRM_DATE = models.DateTimeField(null=True, blank=True)  # 주문 확인 일자
    RTN_DT = models.DateTimeField(null=True, blank=True)  # 반품 완료일자
    CHNG_DT = models.DateTimeField(null=True, blank=True)  # 교환 완료일자
    DELIVERY_CONFIRM_DATE = models.DateTimeField(null=True, blank=True)  # 출고 완료일자
    CANCEL_DT = models.DateTimeField(null=True, blank=True)  # 취소 완료일자
    DELIVERY_ID = models.CharField(max_length=100, null=True, blank=True)  # 택배사 코드
    INVOICE_NO = models.BigIntegerField(null=True, blank=True)  # 송장번호
    INV_SEND_MSG = models.CharField(max_length=100, null=True, blank=True)  # 송장 전송 결과
    INV_SEND_DM = models.DateTimeField(null=True, blank=True)  # 송장 전송일
    USER_ID = models.CharField(max_length=100, null=True, blank=True)  # 주문자 ID
    USER_NAME = models.CharField(max_length=100, null=True, blank=True)  # 주문자 이름
    USER_TEL = models.CharField(max_length=100, null=True, blank=True)  # 주문자 전화
    USER_CEL = models.CharField(max_length=100, null=True, blank=True)  # 주문자 폰
    RECEIVE_NAME = models.CharField(max_length=100, null=True, blank=True)  # 수취인 이름
    RECEIVE_TEL = models.CharField(max_length=100, null=True, blank=True)  # 수취인 전화
    RECEIVE_CEL = models.CharField(max_length=100, null=True, blank=True)  # 수취인 폰
    RECEIVE_ZIPCODE = models.CharField(max_length=10, null=True, blank=True)  # 우편번호
    RECEIVE_ADDR = models.CharField(max_length=100, null=True, blank=True)  # 주소
    DELV_MSG = models.CharField(max_length=100, null=True, blank=True)  # 배송메세지
    HOPE_DELV_DATE = models.CharField(max_length=10, null=True, blank=True)  # 배송희망일
    memo = models.CharField(max_length=10, null=True, blank=True)  # 메모

    # 카테고리
    item_id = models.CharField(max_length=100, null=True, blank=True)  # 품번
    item_name = models.CharField(max_length=100, null=True, blank=True)  # 품목
    item_quan = models.IntegerField(null=True, blank=True)  # 품목수량
    # 추가구성


class Work_list(models.Model):
    checker = models.CharField(max_length=100, null=True, blank=True)
    check_time = models.DateTimeField(auto_now_add=True)
    order = models.ManyToManyField(Order_list, related_name='order')


class Category(models.Model):
    name = models.CharField(max_length=100) ## 카테고리
    create_date = models.DateTimeField(auto_now_add=True)
    modify_user = models.CharField(max_length=100, null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    rank = models.IntegerField()

class Packing(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_user = models.CharField(max_length=100, null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)

class Factory(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_user = models.CharField(max_length=100, null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100) ## 품목
    category = models.ForeignKey(Category, on_delete=models.SET('해당 카테고리는 삭제 되었습니다.'), related_name='category')
    packing = models.ForeignKey(Packing, on_delete=models.SET('해당 포장상태가 삭제되었습니다.'), related_name='boxing')
    pdfactory = models.ForeignKey(Factory, on_delete=models.SET('해당 공장이 삭제되었습니다.'), related_name='pdfactory') ## produce
    smfactory = models.ForeignKey(Factory, on_delete=models.SET('해당 공장이 삭제되었습니다.'), related_name='smfactory')## shipment
    create_date = models.DateTimeField(auto_now_add=True)
    modify_user = models.CharField(max_length=100, null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    sumpacking = models.BooleanField()
    rank = models.IntegerField(null=True, blank=True)


class Calendar(models.Model):
     title = models.CharField(max_length=50, null=True)
     start_data = models.DateTimeField(unique=True, null=True)
     end_data = models.DateTimeField(unique=True, null=True)
     allday = models.BooleanField()



class User(models.Model):
    user_id = models.CharField(max_length=45),
    name = models.CharField(max_length=45),
    password = models.CharField(max_length=400),
    password2 = models.CharField(max_length=400),

