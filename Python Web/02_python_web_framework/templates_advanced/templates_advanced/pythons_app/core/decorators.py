from django.http import HttpResponse
from django.shortcuts import render


def only_allow_groups(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            def unauthorised_response():
                return render(request, "exit_codes/401.html")

            user = request.user
            if user.is_superuser:
                return view_func(request, *args, **kwargs)
            if not user.is_authenticated:
                return unauthorised_response()
                # return HttpResponse('You must be signed in!') # Homework Only
            if not user.groups.exists():
                return unauthorised_response()
                # return HttpResponse(f'You must be in one of the following groups: {", ".join(groups)}') # Homework Only

            user_groups = [g.name for g in user.groups.all()]
            result = set(user_groups).intersection(groups)
            if groups and not result:
                return unauthorised_response()
                # return HttpResponse(f'You must be in one of the following groups: {", ".join(groups)}') # Homework Only

            return view_func(request, *args, **kwargs)


        return wrapper
    return decorator
