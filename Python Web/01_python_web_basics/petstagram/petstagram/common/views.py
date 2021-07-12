from django.shortcuts import render


def index(req):
    context = {
        'page_name': 'landing',
    }
    return render(req, 'landing_page.html', context)
