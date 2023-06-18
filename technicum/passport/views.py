from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def passport(request: HttpRequest) -> HttpResponse:
    template = 'passport.html'
    return render(request, template)


def passport_get_data(request):
    fields_dict = {}
    fields_dict['doc_type'] = 'passport'
    response = transform_data(fields_dict, request)
    return response
