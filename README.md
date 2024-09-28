#to set projet location as Python path
set PYTHONPATH=%PYTHONPATH%;D:\MLModelPackaging\pack-ml-model

## Virtual Environment
Install virtual environment

'''
python -m pip install virtualenv
'''

Check the version
'''
virtualenv --version
'''

create virtual environmet
'''
virtualenv ml_package
'''

Activate your virtual environment
'''
ml_package\Scripts\activate
'''

pip install -r requirements.txt

#Manifest.in used in Python projects to specify files to be included or excluded 
#when creating source distribution with 'setuptools'