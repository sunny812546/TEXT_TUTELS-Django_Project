from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,"index.html")
def output(request):
    inputtext=request.POST.get("text","default")
    titel=request.POST.get("a","off")
    uppercase=request.POST.get("b","off")
    lowercase=request.POST.get("c","off")
    extraspace=request.POST.get("d","off")
    RemovePunc=request.POST.get("e","off")
    if titel=="on":

        ans=inputtext.title()
        params = {"ans":ans}
        inputtext = ans
    if uppercase=="on":
        ans=inputtext.upper()
        params = {"ans":ans}
        inputtext = ans
    if lowercase=="on":
        ans=inputtext.lower()
        params = {"ans":ans}
        inputtext = ans
    if extraspace=="on":
        analyzed = ""
        for index, char in enumerate(inputtext):
            # It is for if a extraspace is in the last of the string
            if char == inputtext[-1]:
                    if not(inputtext[index] == " "):
                        analyzed = analyzed + char

            elif not(inputtext[index] == " " and inputtext[index+1]==" "):                        
                analyzed = analyzed + char
        ans=analyzed
        params = {"ans":ans}
        inputtext=ans
    if RemovePunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for c in inputtext:
            if c not in punctuations:
                analyzed=analyzed+c
        ans=analyzed
        params={"ans":ans}
        inputtext=ans
    if(titel!= "on" and uppercase!="on" and lowercase!="on" and extraspace!="on" and RemovePunc!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request,"output.html",params)
