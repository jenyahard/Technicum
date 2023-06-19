import os
import zipfile

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
        return give_me_file(ready_doc_file_path, doc_type, fields_dict)


def give_me_file(ready_doc_file_path: str, doc_type: str, fields_dict: dict):
    '''Отправляет пользователю готовый файл из папки для загрузки'''
    doc_name_for_user = fields_dict['ru_name']
    with open(ready_doc_file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{quote(doc_name_for_user + ".docx")}"'
        return response


def smk_transform_data(fields_dict: dict, request: HttpRequest):
    smk_base_files_list = fields_dict['smk_base_files_list']
    print('smk_base_files_list =====', smk_base_files_list)
    if request.method == 'POST':
        for i in range(1, 6):
            field_i = request.POST.get(f'field{i}')
            if field_i is not None and field_i != '':
                fields_dict[f"pf{i}"] = field_i
        fields_dict['pf6'] = request.POST.get('field3')[:4]
    for i in range(0, 13):
        fields_dict['doc_type'] = f'smk{i}'
        fields_dict['base_file_name'] = f'smk_base{i}.docx'
        main_func(fields_dict)
    return download_files(request)


def download_files(request):
    # Список файлов, которые необходимо скачать
    files_to_download = []
    for i in range(0, 13):
        files_to_download.append(f'new_smk{i}.docx')
    # Создание временного архива
    zip_filename = 'Документы СМК.zip'
    zip_file_path = os.path.join(settings.MEDIA_ROOT, zip_filename)
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for file in files_to_download:
            file_path = os.path.join(settings.MEDIA_ROOT, 'new_smk_files',file)
            zip_file.write(file_path, os.path.basename(file_path))
    # Открытие и чтение архива
    with open(zip_file_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{quote(zip_filename)}"'
    # Удаление временного архива
    os.remove(zip_file_path)
    return response
