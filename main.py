#Di fatto l'import fa il copia incolla del codice presente nel modulo importato
import json
import Counter as cn

print("Ciao sono il main")
c1=cn.Counter("Counter1")
c2=cn.Counter("Counter2")
c1.print_attr()

#########   File
f=open('myfile.txt', 'w+')
f.write("Hello world")
f.close()
content=None
with open('myfile.txt', 'r') as fp:
    #faccio qualcosa con il filepointer
    content=fp.readline()
print("File:\n"+content)


#########   JSON
myJSON={'result':'Testo della canzone', 'success': 0, 'errormsg': ''}
with open("filejson.txt", 'w+') as fp:
    json.dump(myJSON, fp)


#########   Eccezioni
try:
    1/0
except Exception as e:
    print(e)

a=1
b=0
try:
    a/b
except Exception as e:
    print("la variabile b non è valida")