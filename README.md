This simple Django web app solves a problem for storing and downloading files.
</br>When you upload a file on the internet for storage and later when you want to donwload them you need to go ot the website and click some buttons. You must navigate to download button and press it.
</br>with this app you can upload your files and when you want to download them just go to  http://127.0.0.1:8000/download/[FILE_NAME] and you can see your file.
</br>If you use a terminal in Linux you can download it from there using wget.
</br>If you are using Windows, open a Powershell and enter  Invoke-WebRequest -OutFile [FILE_NAME] -Uri http://127.0.0.1:8000/download/[FILE_NAME] and file will be downloaded to your current directory.
