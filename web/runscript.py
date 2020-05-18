import os
import re
import subprocess

directory = '.\students'

strtype_to_ormtype_dict = {
    'date': 'DateTimeField()',
    'string': 'CharField(max_length=200)',
    'text': 'TextField()',
    'int': 'IntegerField()',
    'float': 'FloatField()'
}


def get_template_params():
    template_params = dict()
    template_params_counts = dict()
    for full_filename in os.listdir(directory):
        full_path=os.path.join(directory, full_filename)
        if os.path.isfile(full_path):
            filename, extension = os.path.splitext(full_filename)
            if extension == '.txt':
                template_params[filename] = set()
                with open(full_path, 'r',encoding='utf8') as template_file:
                    for line in template_file:
                        for param_tuple in re.findall(r'#([\w_]+)(?:\[(\w+)\])?', line):
                            template_params[filename].add(param_tuple)
                            if param_tuple not in template_params_counts:
                                template_params_counts[param_tuple] = 1
                            else:
                                template_params_counts[param_tuple] += 1

    common_template_params = list(filter(lambda param: template_params_counts[param] > 1, template_params_counts))
    for common_template_param in common_template_params:
        for param_name in template_params:
            try:
                template_params[param_name].remove(common_template_param)
            except KeyError:
                pass
    template_params['common'] = common_template_params
    return template_params


def generate_models_file(template_params_dict):
    with open('users/dynamic_models.py', 'w') as models_file:
        models_file.write('from django.db import models\n\n\n')
        for template_name, template_params in template_params_dict.items():
            models_file.write('class {}(models.Model):\n'.format(template_name))
            for param_name, param_type in template_params:
                if not param_type:
                    param_type = 'string'
                if param_type not in strtype_to_ormtype_dict:
                    raise AttributeError("Unknown type: '{}'!".format(param_type))
                models_file.write('\t{} = models.{}\n'.format(param_name, strtype_to_ormtype_dict[param_type]))
            models_file.write('\n\n')


def generate_forms_file(template_params_dict):
    with open('users/dynamic_forms.py', 'w') as forms_file:
        forms_file.write('from django.forms import ModelForm\n')
        forms_file.write('from .dynamic_models import {}\n\n\n'.format(', '.join(template_params_dict)))
        for template_name, template_params in template_params_dict.items():
            forms_file.write('class {}Form(ModelForm):\n'.format(template_name))
            forms_file.write('\tclass Meta:\n')
            forms_file.write('\t\tmodel = {}\n'.format(template_name))
            forms_file.write(
                '\t\tfields = ({})\n'.format(', '.join("'{0}'".format(param[0]) for param in template_params)))
            forms_file.write('\n\n')


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
generate_models_file(fetched_template_params)
generate_forms_file(fetched_template_params)
generate_admin_file(fetched_template_params)
generate_views_file(fetched_template_params)
make_migrations_retcode = subprocess.run(["python", "manage.py", "makemigrations"], capture_output=True).returncode
migrate_retcode = -1
if make_migrations_retcode == 0:
    migrate_retcode = subprocess.run(["python", "manage.py", "migrate"], capture_output=True).returncode
if migrate_retcode == 0:
    result = subprocess.run(["python", "manage.py", "runserver"], capture_output=True)
    print(result)
