from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_ord_ymd = serializers.SerializerMethodField()
    order_ord_no = serializers.SerializerMethodField()
    
    def get_ord_ymd(self, obj):
        return obj.order.ord_ymd

    def get_ord_no(self, obj):
        return obj.order.ord_no

    class Meta:
        model = Order
        fields = '__all__'