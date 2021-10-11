from django.shortcuts import render

def main(request, *args, **kwargs):
    return render(request, 'BookApp/index.html',{})