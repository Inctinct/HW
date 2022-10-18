import os
import shutil
import re
print(os.name)
direct=input('Введите название папки в которую хотите войти:')
path=os.getcwd()+'\\'+direct
os.chdir(path)
try:
    os.mkdir('python_files')
    os.mkdir('json_files')
    os.mkdir('txt_files')
except OSError:
    print('Не удалось создать директории')
else:
    print('Директории созданы')
files=os.listdir(path)
python_count=0
json_count=0
txt_count=0
for i in files:
    if re.search('\.json',i):
        shutil.move(i,'json_files')
        json_count+=1
    if re.search('\.py',i):
        shutil.move(i,'python_files')
        python_count+=1
    if re.search('\.txt',i):
        shutil.move(i,'txt_files')
        txt_count+=1
print(f'В папку с питонскими файлами закинуто {python_count} файла/ов, '
      f'их суммарный размер равен {os.path.getsize("python_files")}»')
print(f'В папку с тхт файлами закинуто {txt_count} файла/ов, '
      f'их суммарный размер равен {os.path.getsize("txt_files")}»')
print(f'В папку с джейсон файлами закинуто {json_count} файла/ов, '
      f'их суммарный размер равен {os.path.getsize("json_files")}»')

print(f'Файл test01.txt успешно переименован в rename_test01.txt')
def start_python():
    os.chdir('python_files')
    files = os.listdir(os.getcwd())
    print(files)
    st_python=input('Введите пайтон файл для запуска')
    try:
        os.startfile(os.getcwd()+"\\"+st_python)
    except Exception:
        print('Что-то пошло не так:(')
    else:
        print(f'Файл {st_python} успешно запущен')

def rename_file(path):
    typ=int(input('Выберите тип файла для переименования:\n1.txt\n2.python\n3.json'))
    if typ == 1:
        path+='\\txt_files'
    if typ == 2:
        path+='\\python_files'
    if typ == 3:
        path+='\\json_files'
    files=os.listdir(path)
    print(files)
    file=input('Выберите файл для переименования: ')
    rename=input('Введите новое название файла: ')
    os.chdir(path)
    try:
        os.rename(file,rename)
    except Exception:
        print('Что-то пошло не так:(')
    else:
        print(f'Файл {file} переименован в {rename}')
start_python()
rename_file(path)