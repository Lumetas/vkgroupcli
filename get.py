import os
import vk_api
from random import randint
import json
def rFile(path):
    f = open(path)
    return f.read()
    f.close()



a = json.loads(rFile('config.json'))

contactFile = a['contactFile']
token = a['key']
messCount = a['historyCount']
groupId = a['groupFromId']
vk = vk_api.VkApi(token=token)

a = json.loads(rFile(contactFile))
i = 0
while(i < len(a)):
    print(str(i + 1) + '. ' + str(a[i]))
    i += 1

id = int(input('номер: '))
id = id - 1
userId = a[id]


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randint(0, 1000)})

    
def getHistory(id, count, groupId):
    a = vk.method('messages.getHistory', {'user_id': id, 'count': count})
    i = 0
    messArr = []
    while (i < count):
        bText = a['items'][i]['text']
        if a['items'][i]['from_id'] == groupId:
            bText = 'you: ' + bText
        else:
            bText = str(a['items'][i]['from_id']) + ': ' + bText
        messArr.append(bText)
        i += 1
    
    return messArr

def printArrayReversed(array, count):
    i = count - 1
    while (i >= 0):
        print(array[i])
        i -= 1


        

a = getHistory(userId, messCount, groupId) 


printArrayReversed(a, messCount)
os.system('python3 mes.py ' + str(userId) + ' &')
while True:
    msg = input()
    write_msg(userId, msg)

