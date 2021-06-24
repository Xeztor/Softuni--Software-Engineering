from django.shortcuts import render


def index(req):
    return render(req, 'landing_page.html')