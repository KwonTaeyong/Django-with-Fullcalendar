from django.urls import path

from .views import index, api, order, work, mdata, etc

app_name = 'B2C'

urlpatterns = [
    ## index
    path('', index.main, name='index'),

    ## api
    path('api/table/', api.Table.as_view(), name='tableapi'),
    path('api/work/', api.gridTable.as_view(), name='gridtableapi'),

    ## order
    path('order/', order.orderlist, name='orderlist'),
    path('api/order.xml', order.order_xml),
    path('updateorder/', order.update_order, name='updateorder'),

    ## work
    path('work/', work.worklist, name='worklist'),

    ## info
    path('mdata/', mdata.datalist, name='datalist'),

    ##etc
    path('etc/', etc.etclist, name='etclist')
]