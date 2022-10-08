# Запрещенные слова

file=input('Set a name of file: ')
words=[]
filtr=''
arr=[]
count=0
new_arr=[]
with open(file,'r')as f:
    with open('forbidden_words.txt','r') as f1:
       for i in f1:
           words+=i.split(' ')

       for j in f:
           filtr+=j

       for i in filtr:
           if i.isupper():
               new_arr.append(count)
           count+=1

       for i in words:

           text=filtr.lower().replace(i,len(i)*'*')
           filtr=text

       filtr=text
       for i in new_arr:
           if text[i].isalpha():
               filtr=text[0:i]+text[i].upper()+text[i+1:]
               text=filtr
       print(text)
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов

with open('class.txt','r',encoding='utf-8') as f:
    for i in f:
        for j in i:
            if j.isdigit() and int(j)<3:
                print(i)


string=''
value=0
with open('цифры.txt','r') as f:
    for i in f:
        for j in i:
            if j.isdigit():
                string+=j
            else:
                string+='+'

    for i in string.split('+'):
        if i.isdigit():
            value+=int(i)
    print(value)

# Зашифруйте данный текстовый файл шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться на 1, второй строки — на 2, третьей строки — на три и т.д.

Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr=[]
count=0
number=0
with open('Цезарь.txt','r') as f:
    for i in f:
        count+=1
        for j in i:

            if j.isalpha():
                j=Alphabet.index(j.upper())
                arr.append(Alphabet[j+1])
            else:
                arr.append(j)
    print(''.join(arr))

# В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам.
arr=[]
partii=0
count=0
with open('ГосДума.txt','r') as f:
    for i in f:
       arr.append(i)

    partii=arr.index('VOTES:\n')-1

    for j in range(1,partii+1):
        count+=arr.count(arr[j])-1
    for j in range(1,partii+1):
        if (100/count)*(arr.count(arr[j])-1) >7:
            print(arr[j])

# Z: Гистограмма            
symbols=[]
arr=[]
matrix=[]
with open('Cipher.txt','r') as f:
    for i in f:
        for j in i:
            if j !=' ' and j !='\n':
                symbols.append(j)
    for i in set(symbols):
        arr.append(symbols.count(i))
    max_arr=arr[0]
    for i in arr:
        if i>max_arr:
            max_arr=i
    symb=set(symbols)
    count=max_arr+1
    for i in range(0,max_arr+1):
        matrix.append([])
        for j in range(len(symb)):
            if count> arr[j]:
                matrix[i].append(' ')
            else:
                matrix[i].append('#')

        count-=1

    for i in range(0,max_arr+1):
        for j in range(len(symb)):
            print(matrix[i][j], end='')
        print()
    print(''.join(symb))

# Q: Выборы Государственной Думы
arr=[]
new_arr=[]
summa=0
ost=[]
golosa=0
with open('gosDuma.txt','r') as f:
    for i in f:
        arr+=(i.split(' '))

    new_arr=arr[2::3]

    for j in range(len(new_arr)-1):
        if j !=len(new_arr):
            new_arr[j]=new_arr[j][:-1]

    for i in new_arr:
        summa+=int(i)
    first_izb=summa/450
    for i in range(len(new_arr)):
        ost.append(int(new_arr[i])/first_izb-int(new_arr[i])//first_izb)

        new_arr[i]=int(new_arr[i])//first_izb
    for i in new_arr:
        golosa+=int(i)

    while golosa<450:
        max_ost=ost[0]
        number=0
        for i in ost:
            if max_ost<i:
                max_ost=i
        number+=ost.index(max_ost)
        new_arr[number]+=1
        golosa+=1

    g=0
    k=1
    for i in range(len(new_arr)):

        print(f'{arr[g]} {arr[k]} {new_arr[i]}')
        g+=3
        k+=3

