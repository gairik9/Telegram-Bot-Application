import time
from django.shortcuts import render,HttpResponse
from Bot.final import run  
import asyncio


def index(request):
    # context = {'name': 'Gairik'}
    # search_input = request.POST.get('name')
    # print(search_input)
    search_input = request.POST.get('group')
    print(search_input)
    run(search_input)
    time.sleep(500)

    return render(request,'index.html')


