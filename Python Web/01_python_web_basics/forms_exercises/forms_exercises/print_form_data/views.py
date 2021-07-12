from django.shortcuts import render

from forms_exercises.print_form_data.forms import DataForm


def form(req):
    if req.method == "POST":
        [print(field, value) for field, value in req.POST.items()]

    context = {
        'form': DataForm(),
    }

    return render(req, 'index.html', context=context)
