
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("hello world")

def admin(request):
    return HttpResponse("hello admin")
def navigate(request):
    html_content = """
        <a href="https://www.amazon.in/" target="_blank"><button>amazon</button> </a>
        <a href="https://www.flipkart.com/" target="_blank"><button>flipkart</button> </a>
        <a href="https://www.ajio.in/" target="_blank"><button>ajio</button> </a>
        <a href="https://www.myntra.com/" target="_blank"><button>myntra</button></a>
        """
    return HttpResponse(html_content)

def calltemp(request):
    details={'name': 'vineeth', 'mail':'vineeth@mail.com'}
    return render(request, 'index.html',details)

def callform(request):
    return render(request, 'basform.html')

def showresults(request):
    resultdata=request.GET.get('textdata','default')
    removepunch=request.GET.get('removepunc', 'off')
    uc=request.GET.get('uppercase','off')
    finaldata=''
    print(resultdata,removepunch)
    if removepunch == "on":
        punclist = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in resultdata:
            if char not in punclist:
                finaldata += char
    elif(uc=="on"):
        for char in resultdata:
            finaldata += char.upper()
    else:
        finaldata = resultdata
    param = {'resultdata': finaldata}
    return render(request, 'showresult.html',param)