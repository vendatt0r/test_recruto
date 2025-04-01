from django.http import HttpResponse

def hello(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить!')
    return HttpResponse(f"Hello {name}! {message}")
