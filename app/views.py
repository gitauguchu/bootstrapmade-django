from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details_pl(request):
    return render(request, 'portfolio-details-pl.html')

def portfolio_details_st(request):
    return render(request, 'portfolio-details-st.html')

def portfolio_details_hpp(request):
    return render(request, 'portfolio-details-hpp.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')