# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def main():

    login, password = 'Логин или номер телефона', 'Пароль'
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
             if event.text == 'Можно с пробелом' or event.text == 'Привет' or event.text == 'привет':
                 if event.from_user: #Если написали в ЛС
                    vk.messages.send( #Отправляем сообщение
                         user_id=event.user_id, 
                         random_id=event.random_id, # random_id - доступен начиная с версии 5.45, обязателен к использованию
                         message='Текст'
                         )

if __name__ == '__main__':
    main()
