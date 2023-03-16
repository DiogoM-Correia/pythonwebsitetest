from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from json import JSONDecodeError
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response

from .api.serializers import UserSerializer
import users.scripts.load_file as ld
from users.models import User


# Create your views here.
def home_view(request, *args, **kwargs):
    print (request)
    print(*args, **kwargs)
    
    return render (request, "home.html", {})

def upload_view (request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        if (fs.exists(uploaded_file.name)):
            fs.delete(uploaded_file.name)

        fs.save(uploaded_file.name, uploaded_file)
 
        if uploaded_file.name[-3:] == 'csv':
            print('csv file')
            ld.import_csv(uploaded_file.name)
        elif uploaded_file.name[-4:] == 'json':
            print('json file')
            ld.import_json(uploaded_file.name)
        else:
            # Not a valide file
            return False

    return render (request, "upload.html", {})

# def export(request):
#     person_resource = UserResource()
#     dataset = person_resource.export()
#     response = HttpResponse(dataset.json, content_type='application/json')
#     response['Content-Disposition'] = 'attachment; filename="persons.json"'
#     return response


# # obtém parâmetros de paginação
# page_number = int(request.GET.get('pageNumber', 1))
# page_size = int(request.GET.get('pageSize', 100))

# # filtra usuários elegíveis com base na região e classificação do usuário
# regiao = request.GET.get('regiao')
# classificacao = request.GET.get('classificacao')
# elegiveis = [u for u in usuarios if u.regiao == regiao and u.classificacao == classificacao]

# # aplica a paginação aos resultados
# total_count = len(elegiveis)
# start_index = (page_number - 1) * page_size
# end_index = start_index + page_size
# elegiveis_paginados = elegiveis[start_index:end_index]

# # retorna os resultados como uma resposta JSON
# response = {
#     'pageNumber': page_number,
#     'pageSize': page_size,
#     'totalCount': total_count,
#     'users': [u.to_dict() for u in elegiveis_paginados]
# }
# return JsonResponse(response)