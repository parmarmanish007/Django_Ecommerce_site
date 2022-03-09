def upload(f):
    with open('user/static/images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
