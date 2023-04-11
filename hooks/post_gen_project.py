import subprocess

print("started post gen project!")
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# 1) conda env 생성
# conda create -n 가상환경이름 python=버전
# ---------------------------------------------------------------------------------------------------------------------------------------------------
print("crate conda env...")
subprocess.call(['conda', 'create', '-n', '{{cookiecutter.project_name}}', 'python={{cookiecutter.python_version}}'])
subprocess.call(['conda', 'activate', '{{cookiecutter.project_name}}'])

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# 3) conda install
# pip install -r requirements.txt
# uvicorn==0.21.1
# fastapi==0.95.0
# requests==2.28.2
# xmltodict==0.13.0
# sqlalchemy==2.0.9
# celery==5.2.7
# alembic==1.10.3
# ---------------------------------------------------------------------------------------------------------------------------------------------------
print("install packages...")
subprocess.call(['conda', 'install', 'uvicorn==0.21.1'])
subprocess.call(['conda', 'install', 'fastapi==0.95.0'])
subprocess.call(['conda', 'install', 'requests==2.28.2'])
subprocess.call(['conda', 'install', 'xmltodict==0.13.0'])
subprocess.call(['conda', 'install', 'sqlalchemy==2.0.9'])
subprocess.call(['conda', 'install', 'celery==5.2.7'])
subprocess.call(['conda', 'install', 'alembic==1.10.3'])

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# 3) git 초기화
# conda create -n 가상환경이름 python=버전
# ---------------------------------------------------------------------------------------------------------------------------------------------------
print("initialize git repo...")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
print("finished post gen project!")
