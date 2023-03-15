from django.shortcuts import render
from django.http import HttpResponse
import users.scripts.load_file as ld
from django.core.files.storage import FileSystemStorage
from users.resources import UserResource

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
        else:
            # Not a valide file
            return False

    return render (request, "upload.html", {})

def export(request):
    person_resource = UserResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response