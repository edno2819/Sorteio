import subprocess

# pyinstaller --name=mysite manage.py
# mysite.exe runserver localhost:8000 --noreload

p = subprocess.run("cp", "dirA/file", "dirB")