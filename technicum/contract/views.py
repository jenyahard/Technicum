from scripts.scripts import transform_data

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def contract(request: HttpRequest) -> HttpResponse:
    template = 'contract.html'
    return render(request, template)


def contract_get_data(request: HttpRequest) -> HttpResponse:
    fields_dict = {}
    fields_dict['doc_type'] = 'contract'
    fields_dict['ru_name'] = 'Контракт и инвойс'
    response = transform_data(fields_dict, request)
    return response
