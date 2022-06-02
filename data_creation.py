#create several random emails on a csv file
import csv
import random as rd
import string as st
from torch import randint
nome = ['Joao','Gabriel','Gustavo','Augusto','Pedro','Rafael','Amanda','Ana','Paula','Maria','Gabriella','Vanessa','Claudia','Alessandra','Gilmar','Thiago','Mariana','Julia','Alan','James','Rodolfo','Luciana']
#nome do meio = qualquer letra uppercase
sobrenome= ['Oliveira','Alves','Silva','Santos','Costa','Braga','Mendonça','Ribeiro','Aragao','Moreira','Mendes','Peres']

def produce_email():
    nome_rand = rd.choice(nome)
    sobrenome_rand = rd.choice(sobrenome)
    valid = rd.randint(0,3)
    randstr = ''.join(rd.choice(st.ascii_uppercase) for i in range(5))
    if valid == 0:
        return nome_rand + rd.choice(st.ascii_uppercase) + sobrenome_rand + '@gmail.com'
    elif valid == 1:
        return nome_rand + rd.choice(st.ascii_uppercase) + sobrenome_rand + '@outlook.com'
    elif valid == 2:
        return nome_rand + rd.choice(st.ascii_uppercase) + sobrenome_rand + '@hotmail.com'
    else:
        return nome_rand + rd.choice(st.ascii_uppercase) + sobrenome_rand + randstr

f = open('.\email_raw.csv', 'w')
# create the csv writer
writer = csv.writer(f)
# write a row to the csv file
writer.writerow(['email'])
for i in range(2000):
    writer.writerow([produce_email()])
# close the file
f.close()