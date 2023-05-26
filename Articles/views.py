from django.shortcuts import render
from.import models
# Create your views here.
def Articles_list(request):
   Articles=models.Article.objects.all().order_by('date')
   
   args={'Articles':Articles}
   return render(request,'Articles/Articleslist.html',args)