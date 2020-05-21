import os
import re
import subprocess
from transliterate import translit
from slugify import slugify
import docx
import docx2txt
from docx import Document
import openpyxl
doc_directory = ['.\students\primaryTemplates',
                 '.\students\secondaryTemplates',]

settings_path='.\doc_settings\prompt_and_types.txt'

primaryTemplates=[]

strtype_to_ormtype_dict = {
    'date': 'DateTimeField()',
    'string': 'CharField(max_length=100)',
    'text': 'TextField()',
    'int': 'IntegerField()',
    'float': 'FloatField()',

}

class variable:
    def __init__(self,param):
        self.name=param[0]
        self.type=param[1]
        self.title=param[2]
        self.prompt='Подсказка:'+str.strip(param[3])

def getTextFromDocx(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def get_template_params():
    #TODO:сделать деление на первичные и вторичные
    template_params = dict()
    template_params_counts = dict()
    for dir in doc_directory:
        for full_filename in os.listdir(dir):
            full_path=os.path.join(dir, full_filename)
            if os.path.isfile(full_path):
                filename, extension = os.path.splitext(full_filename)
                if extension == '.docx' and filename[0]!='~':
                    if (doc_directory.index(dir)==0):
                        primaryTemplates.append(filename)
                    template_params[filename] = set()
                    template_file = docx2txt.process(full_path)
                    template_file = template_file.split('\n')
                    for line in template_file:
                        for param_name in re.findall(r'#([\w_]+)', line):
                            param_name=slugify(param_name,separator='_')
                            template_params[filename].add( param_name)
                            if param_name not in template_params_counts:
                                template_params_counts[param_name] = 1
                            else:
                                template_params_counts[param_name] += 1

                if extension=='.xlsx'and filename[0]!='~':
                    if (doc_directory.index(dir)==0):
                        primaryTemplates.append(filename)
                    xlsx_file =openpyxl.load_workbook(full_path)
                    sheet=xlsx_file.active
                    template_params[filename] = set()
                    for row in sheet.iter_rows():
                        for cell in row:
                            s=str(cell.value)
                            if (s[0]=='#'):
                                param_name=s.replace('#','')
                                param_name = slugify(param_name, separator='_')
                                template_params[filename].add(param_name)
                                if param_name not in template_params_counts:
                                    template_params_counts[param_name] = 1
                                else:
                                    template_params_counts[param_name] += 1

    common_template_params = list(filter(lambda param: template_params_counts[param] > 1, template_params_counts))
    for common_template_param in common_template_params:
        for param_name in template_params:
            try:
                template_params[param_name].remove(common_template_param)
            except KeyError:
                pass
    template_params['osnovnye'] = common_template_params
    return template_params

'''
def create_types_and_prompt(template_params_dict):
    with open(settings_path, 'w', encoding='utf8') as template_file:
        for template_name, template_params in template_params_dict.items():
            for param_name in template_params:
                template_file.write('{}|||\n'.format(param_name))
'''

def get_types_and_prompt_dict():
    types_and_prompt=dict()
    with open(settings_path, 'r', encoding='utf8') as template_file:
        for line in template_file:
            param=line.split('|')
            param[0]=slugify(param[0],separator='_')
            var=variable(param)
            types_and_prompt[var.name]=var

    return types_and_prompt

def generate_models_file(template_params_dict,types_and_prompt_dict):
    with open('users/dynamic_models.py', 'w',encoding='utf8') as models_file:
        models_file.write('from django.db import models\n\n\n')
        for template_name, template_params in template_params_dict.items():
            models_file.write('class {}(models.Model):\n'.format(template_name))
            for param_name in template_params:
                param_type = types_and_prompt_dict[param_name].type
                if not param_type:
                    param_type = 'string'
                if param_type not in strtype_to_ormtype_dict:
                    raise AttributeError("Unknown type: '{}'!".format(param_type))
                models_file.write('\t{} = models.{}\n'.format(param_name, strtype_to_ormtype_dict[param_type]))
            models_file.write('\n\n')

def generate_forms_file(template_params_dict,types_and_prompt_dict):
    with open('users/dynamic_forms.py', 'w',encoding='utf8') as forms_file:
        forms_file.write('from django.forms import ModelForm\n')
        forms_file.write('from django import forms\n')
        forms_file.write('from django.utils.translation import ugettext_lazy as _\n')
        forms_file.write('from .dynamic_models import {}\n\n\n'.format(', '.join(template_params_dict)))
        for template_name, template_params in template_params_dict.items():
            forms_file.write('class {}Form(ModelForm):\n'.format(template_name))
            try:
                if (primaryTemplates.index(template_name)>-1):
                    forms_file.write("\tindex='1'\n")
            except ValueError:
                if (template_name == 'osnovnye'):
                    forms_file.write("\tindex='0'\n")
                else:
                    forms_file.write("\tindex='2'\n")

            forms_file.write("\tname='{}'\n".format(translit(template_name,"ru")))
            forms_file.write('\tclass Meta:\n')
            forms_file.write('\t\tmodel = {}\n'.format(template_name))

            forms_file.write(
                '\t\tfields = ({},)\n'.format(', '.join("'{0}'".format(param) for param in template_params)))
            forms_file.write('\n\n')

            forms_file.write("\t\tlabels = {\n")
            for param in template_params:
                var=types_and_prompt_dict[param]
                forms_file.write("\t\t\t'{}':_('{}'),\n".format(var.name, var.title))
            forms_file.write("\t\t}\n")

            forms_file.write("\t\thelp_texts = {\n")
            for param in template_params:
                var = types_and_prompt_dict[param]
                forms_file.write("\t\t\t'{}':_('{}'),\n".format(var.name, var.prompt))
            forms_file.write("\t\t}\n")


def generate_admin_file(template_params_dict):
    with open('users/admin.py', 'w') as admin_file:
        admin_file.write('from django.contrib import admin\n')
        admin_file.write('from .dynamic_models import {}\n\n\n'.format(', '.join(template_params_dict)))
        for template_name in template_params_dict:
            admin_file.write('admin.site.register({})\n'.format(template_name))

def generate_views_file(template_params_dict):
    with open('users/dynamic_views.py', 'w') as admin_file:
        admin_file.write('from .dynamic_forms import *\n')
        admin_file.write('from django.contrib.auth.decorators import login_required\n'
                         'from django.shortcuts import render\n')
        admin_file.write('@login_required\n')
        admin_file.write('def docs(request):\n')
        admin_file.write('\tunique_forms=[]\n')
        admin_file.write("\tif request.method == 'POST':\n")
        for template_name in template_params_dict:
            admin_file.write('\t\tunique_forms.append({0}Form(data=request.POST))\n'.format(template_name))
            admin_file.write('\t\tif unique_forms[-1].is_valid():\n')
            admin_file.write('\t\t\tunique_forms[-1].save()\n')
        admin_file.write('\telse:\n')
        for template_name in template_params_dict:
            admin_file.write('\t\tunique_forms.append({0}Form())\n'.format(template_name))
        #admin_file.write('\traise Exception(repr(unique_forms))\n')
        admin_file.write('\treturn render(request,"profile/documents.html",{"forms": unique_forms})')

fetched_template_params = get_template_params()

#create_types_and_prompt(fetched_template_params)

types_and_prompt_dict=get_types_and_prompt_dict()
generate_models_file(fetched_template_params,types_and_prompt_dict)
generate_forms_file(fetched_template_params,types_and_prompt_dict)
generate_admin_file(fetched_template_params)
generate_views_file(fetched_template_params)
make_migrations_retcode = subprocess.run(["python", "manage.py", "makemigrations","--noinput"], capture_output=True).returncode
migrate_retcode = -1
if make_migrations_retcode == 0:
    migrate_retcode = subprocess.run(["python", "manage.py", "migrate"], capture_output=True).returncode
"""
if migrate_retcode == 0:
    result = subprocess.run(["python", "manage.py", "runserver"], capture_output=True)
    print(result)
"""