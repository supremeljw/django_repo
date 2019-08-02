from django.shortcuts import render, HttpResponse, render_to_response
from django.views.generic import ListView,DetailView
import random
from forms_base.models import UserInfo
# Create your views here.

def test(request):
    html='<h1>我的天哪</h1>'
    return HttpResponse(html)
def error_404(req):
    return render(req,'404.html',{'msg':random.randint(1,100)})

class IndexView(ListView):
    template_name = 'index.html'
    model = UserInfo

class myDetailView(DetailView):
    model = UserInfo
    template_name = 'detail_view.html'
    pk_url_kwarg = 'user_id'
