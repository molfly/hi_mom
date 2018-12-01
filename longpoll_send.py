# -*- coding: utf-8 -*-
import vk_api
#import requests
#import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
#from datetime import datetime

def main():
    """ Пример использования longpoll

        https://vk.com/dev/using_longpoll
        https://vk.com/dev/using_longpoll_2
    """

    login, password = 'Логин или номер телефона', 'пароль'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
             vars = ['Первая фраза', 'вторая фраза', 'Третья фраза']		
             if ( str(event.text).lower() ) in vars:
                 if event.from_user: #Если написали в ЛС
                    #now = datetime.now()
                    vk.messages.send( #Отправляем сообщение
                         user_id=event.user_id, 
                         # random_id - доступен начиная с версии 5.45, обязателен к использованию
                         random_id=event.random_id,
                         message='Ответ'
                         )



if __name__ == '__main__':
    main()