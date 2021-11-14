#Склеивает файлы. Кидаем в папку python. Переименовываем в 1.mp3
#И дальше скрипт множит 5 раз нашу музыку
#Еще как вариант    input1 = open ('1.mp3', 'rb'). read()
#                   input2 = open ('2.mp3', 'rb'). read()
#                   input1+=input2

input1 = open ('1.mp3', 'rb'). read()
input2 = open ('1.mp3', 'rb'). read()
input3 = open ('1.mp3', 'rb'). read()
input4 = open ('1.mp3', 'rb'). read()
input5 = open ('1.mp3', 'rb'). read()

input4+=input5
input3+=input4
input2+=input3
input1+=input2

with open ('3.mp3', 'wb') as fp:
    fp.write(input1)
    
#print (file.read())
#file.close()

input('press ENTER to exit')