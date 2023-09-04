from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'list.html')

def got_data(request):
    return HttpResponse("<h1>성공적으로 업데이트 되었습니다.</h1>")