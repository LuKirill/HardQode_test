from django.http import HttpResponse


def index(request):
    return HttpResponse("Тестовое задание от Hard_Qode.")
