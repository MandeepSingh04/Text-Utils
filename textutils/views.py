# I have created this file - Mandeep
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # input from textbox
    djtext = request.POST.get('text', 'Not found anything')
    # checkboxes
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # check checkboxes
    mytext = djtext
    if removepunc == 'on':
        punctuations = '''<>,./?;'":[]{}_()!`~@#$%^&\\*|-+'''
        analyzed = ""
        for char in mytext:
            if char not in punctuations:
                analyzed = analyzed + char
        mytext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in mytext:
            analyzed = analyzed + char.upper()
        mytext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in mytext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            mytext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for i, char in enumerate(mytext):
            if not (mytext[i] == " " and mytext[i + 1] == " "):
                analyzed = analyzed + char
        mytext = analyzed

    if removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off' and extraspaceremover == 'off':
        params = {'analyzed_text': mytext}
        return render(request, 'analyze2.html', params)

    params = {'purpose': 'Completed', 'analyzed_text': mytext}
    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')
