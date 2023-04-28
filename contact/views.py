from django.shortcuts import render

from django.shortcuts import render

def post_list(request):
    return render(request, 'contact/contact.html', {})
