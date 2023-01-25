from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .paginations import OrderLargePagination


class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.all().order_by('-id')
        
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)