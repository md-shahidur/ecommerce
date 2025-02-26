from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
# Create your views here.


def order_summery(request):
    if request.method == "POST":
        # ids = json.load(request)['ids']
        # qty = json.load(request)['ids']
        data = request.POST['data']
        j_data = json.loads(data)
        # print(j_data['qty'], type(j_data))
        id_list = []
        qty_list = []
        subtotal = float(j_data['subtotal'])
        grand_total = float(j_data['total'])

        for data in j_data['qty']:
            qty_list.append(int(data))
        for data in j_data['ids']:
            id_list.append(int(data))
        # for data in j_data['total']:
        #     print(data, type(data))
        new_dict = {k: v for k, v in zip(id_list, qty_list)}

        print(new_dict, subtotal, grand_total, type(grand_total))
        msg = {'result': 'Ajax Success'}
        return JsonResponse(msg)
