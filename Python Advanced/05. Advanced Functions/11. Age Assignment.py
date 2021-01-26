def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        if name[0] in kwargs:
            result[name] = kwargs[name[0]]
    return result

