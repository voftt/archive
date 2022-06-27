from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def count(request):
    full_text = request.GET["fulltext"]
    return render(request,'count.html',{'text':full_text, 'total':len(full_text)})
