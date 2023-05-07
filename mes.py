from random import randint
import json
import vk_api
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

def lower(str):
    return str.lower()

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randint(0, 1000)})
f = open('config.json')
a = json.loads(f.read())
# API-ключ созданный ранее
token = a['key']

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            if (sys.argv[1] == str(event.user_id)):
                request = event.text
                
                print(str(event.user_id) + ': ' + request)
