# this file is created by me - Dk
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    capitalise=request.POST.get('capitalise','off')
    newlinecut=request.POST.get('newlinecut','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed

    if capitalise=="on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()

        params = {'purpose':' Maked the capital','analyzed_text':analyzed}
        djtext = analyzed

    if charcount=="on":
        word = 1
        for char in djtext:
            if char ==" ":
                word=word+1
                analyzed = word

        params = {'purpose':' numbers of letter are ','analyzed_text':analyzed}


    if newlinecut=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': ' New lines are removed ', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': ' Extra spaces are removed ', 'analyzed_text': analyzed}

    if(removepunc!="on" and capitalise!="on"  and newlinecut!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Please select the type of text which you want to modify.. ")

    return render(request, 'analyze.html', params)

