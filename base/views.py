from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Counter
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        count = Counter.objects.get(user=request.user)
        context = {
            'count':count
        }
        return render(request, 'base/home.html', context)
    
class UpdateCount(LoginRequiredMixin, View):
    def post(self, request):
        count = Counter.objects.get(user=request.user)
        data = json.loads(request.body)
        action = data['action']
        if action == 'add':
            count.count += 1
            count.save()
            res = 'add action has been made...'
        elif action  == 'remove':
            count.count -=1
            count.save()
            res = 'remove action has been made...'    
        return JsonResponse(res,safe=False)   
