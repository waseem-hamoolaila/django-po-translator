# django-po-translator

Django package allows you to translate PO files automatically and fix all the fuzziness in your files ... with only one command
The package will detect all your PO files and translate or fix them based on the file language ... without any interaction by you.

You can check [pypi](https://pypi.org/project/django-po-translator/) for more information.


# Installation

### Install the package

```
pip install django-po-translator

```

### Add the package to your installed apps

```
INSTALLED_APPS = [
    ..., 
    'django_po_translator',
    ...
]
```

### Important steps

Make sure your app is ready to support localization ... you should have *locale* folder in the root of your project and **all related settings** are added.


# How to use the package?

- After installing the package and making sure that all is looking fine
- Run ` python manage.py translate ` *Extra arguments will be mentioned down*
- You will need to compile messages to reflect the new translations
- Enjoy :) 

### po-translator command arguments

- **--translate-existed**: This argument will allow the command to translate the already existed translation .. use it carefully .. as it will override all your existing translations
- **--resolve-fuzzy**: This argument will resolve all fuzzy translations in your po file

Ex: ` python manage.py translate --translate-existed --resolve-fuzzy `


### Tests

To run tests ` python manage.py test django_po_translator `

### Note

If you have any issue while using the package ... don't hesitate to report it and it will be fixed ASAP. Thank you.