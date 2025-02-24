from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
# Create your views here.


def order_summery(request):
    if request.method == "POST":
        # ids = request.POST['ids']
        qty = json.load(qty)
        print(qty)
        msg = {'result': 'Ajax Success'}
        return JsonResponse(msg)
