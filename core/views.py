from django.shortcuts import render, redirect
import os
import datetime
from django.http import FileResponse


#   Invoke-WebRequest -OutFile Decoder.py -Uri http://127.0.0.1:8000/download/Decoder.py

def index(request):
    #files_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Files')
    files_folder_path = '\\Files'    # Modify this part
    # Get the list of files in the "Files" folder
    files_list = os.listdir(files_folder_path)

    # Pass the list of files to the template
    return render(request, 'index.html', {'files_list': files_list})

def uploadPage(request):
    return render(request, 'upload.html')

def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        
        # Specify the path where you want to save the uploaded files
        upload_folder = '\\Files'    # Modify this part

        # Save the file to the specified path
        with open(os.path.join(upload_folder, uploaded_file.name), 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return redirect('index')  # Redirect to the same page after successful upload
    return redirect('uploadPage')

def download(request, Filename=''):
    os.chdir('\\Files')    # Modify this part
    request_file= open(Filename, 'rb')
    return FileResponse(request_file)
