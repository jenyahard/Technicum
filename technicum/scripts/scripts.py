import os

from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import default_storage

from scripts.passport_insert_and_create_file import main_func

from urllib.parse import quote


def transform_data(fields_dict: dict, request: HttpRequest) -> HttpResponse:
    '''Трансформирует введенные пользователем на html странице
       текстовые и графические данные в word документ и
       отправляет пользователю этот документ для загрузки
    '''
    
    if fields_dict['doc_type'] == 'tu':
        fields_dict['pf35'] = request.POST.get('field6')[:4]
    doc_type = fields_dict['doc_type']
    if request.method == 'POST':
        for i in range(1, 60):
            field_i = request.POST.get(f'field{i}')
            if field_i is not None and field_i != '':
                fields_dict[f"pf{i}"] = field_i
        uploaded_file = request.FILES.get('field18')
        if uploaded_file:  # Проверка наличия загруженного файла
            file_name = uploaded_file.name
            image_file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            default_storage.save(image_file_path, uploaded_file)
            fields_dict['image_file_path'] = image_file_path
        ready_doc_file_path = os.path.join(settings.MEDIA_ROOT, f'new_{doc_type}.docx')
        main_func(fields_dict)
        return give_me_file(ready_doc_file_path, doc_type)


def give_me_file(ready_doc_file_path: str, doc_type: str):
    '''Отправляет пользователю готовый файл из папки для загрузки'''
    with open(ready_doc_file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{quote(doc_type + ".docx")}"'
        return response
