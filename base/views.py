from django.shortcuts import render
from django.views.generic import View
from .models import Counter
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        count = Counter.objects.get(user=request.user)
        context = {
            'count':count
        }
        return render(request, 'base/home.html', context)
