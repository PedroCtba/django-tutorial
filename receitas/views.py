from django.shortcuts import render

# Create your views here.
def index(request):
    # Return thr HTML file at this view
    return render(request, 'index.html')