from django.shortcuts import render, get_object_or_404
from .models import Page
# Create your views here.
# '<int:page_id>/<slug:page_slug>/'
def page(request, page_id, page_slug):
    page =get_object_or_404(Page,id=page_id)
    return render(request, 'pages/sample.html',{'page': page})


 