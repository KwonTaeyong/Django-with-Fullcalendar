from rest_framework import serializers
from B2C.models import Order_list, Product, Category, Factory, Calendar


class OrderlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_list  # product 모델 사용
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):

    start_data = serializers.SerializerMethodField()
    end_data = serializers.SerializerMethodField()

    def get_start_data(self, obj):
        print(obj.startdata)
        return obj

    def get_end_data(self, obj):
        print(obj)
        return obj

    class Meta:
        model = Calendar
        fields = (
            'title',
            'start_data',
            'end_data'
        )

