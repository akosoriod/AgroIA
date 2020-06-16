from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from zipfile import ZipFile, BadZipfile
from django.conf import settings, os
class CreateUserForm(UserCreationForm):
    rol = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','rol','email','password1','password2']

class UserChangeForm(UserChangeForm):
    rol = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','rol','email']

class ItemForm(forms.ModelForm):
    title = forms.CharField(max_length=99)
    detail = forms.CharField(max_length=499)
    met = forms.IntegerField()
    class Meta:
        model = Item
        fields = ['title','detail','image','met']

class MethodForm(forms.ModelForm):
    title = forms.CharField(max_length=99)
    detail = forms.CharField(max_length=499)
    file  = forms.FileField()
    class Meta:
        model = Method
        fields = ['title','detail','file','command']


    def process_file(self,title):
        # Ruta donde se encuentra el fichero
        zip_filename = self.cleaned_data['file']
        # Lugar donde se alojarán los ficheros descomprimidos
        dirname=settings.MEDIA_ROOT+"/methods/"
        dir= os.path.join(dirname,title+"_Folder")
        os.mkdir(dir)
        #dirname2 = str(dir)
        zip = ZipFile(zip_filename)
        lista_ficheros = []
		# Recorremos todos los ficheros que contiene el zip
        for filename in zip.namelist():
            ruta_total = os.path.join(dir , filename)
            # Si es un directorio, lo creamos
            if filename.endswith('/'):
                try: # Don't try to create a directory if exists
                    os.mkdir(ruta_total)
                except:
                    pass
			# Si es un fichero, lo escribimos
            else:
                outfile = open(ruta_total, 'wb')
                outfile.write(zip.read(filename))
                outfile.close()
                lista_ficheros.append(ruta_total)
        zip.close()
