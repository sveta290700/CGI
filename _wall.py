#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import time
from markdown2 import Markdown

md = Markdown()


class Wall:
    USERS = 'cgi-bin/users.json'
    WALL = 'cgi-bin/wall.json'
    COOKIES = 'cgi-bin/cookies.json'

    def __init__(self):
        """Создаём начальные файлы, если они не созданы"""
        try:
            with open(self.USERS, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.USERS, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        try:
            with open(self.WALL, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.WALL, 'w', encoding='utf-8') as f:
                json.dump({"posts": []}, f)

        try:
            with open(self.COOKIES, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.COOKIES, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def register(self, user, password, avatar):
        """Регистриует пользователя. Возвращает True при успешной регистрации"""
        if self.find(user):
            return False  # Такой пользователь существует
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        users[user] = {'password': password, 'avat': avatar}
        with open(self.USERS, 'w', encoding='utf-8') as f:
            json.dump(users, f)
        return True

    def set_cookie(self, user):
        """Записывает куку в файл. Возвращает созданную куку."""
        with open(self.COOKIES, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        cookie = str(time.time()) + str(random.randrange(10**14))  # Генерируем уникальную куку для пользователя
        cookies[cookie] = user
        with open(self.COOKIES, 'w', encoding='utf-8') as f:
            json.dump(cookies, f)
        return cookie

    def find_cookie(self, cookie):
        """По куке находит имя пользователя"""
        with open(self.COOKIES, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        return cookies.get(cookie)

    def find(self, user, password=None):
        """Ищет пользователя по имени или по имени и паролю"""
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if user in users and (password is None or password == users[user]):
            return True
        return False

    def get_avatar(self, user):
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if user in users:
            test = users[user]
            return users[user]['avat']
        else:
            return ""

    def publish(self, user, text, avatar):
        """Публикует текст"""
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        wall['posts'].append({'user': user, 'text': text, 'avatar': avatar})
        with open(self.WALL, 'w', encoding='utf-8') as f:
            json.dump(wall, f)

    def html_list(self):
        """Список постов для отображения на странице"""
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        posts = []
        for post in wall['posts']:
            if 'avatar' in post:
                content = md.convert('![avatar](' + post['avatar'] + ')**' + post['user'] + '**: ') + md.convert(
                    post['text'])
            else:
                content = md.convert('**' + post['user'] + '**: ') + md.convert(post['text'])
            posts.append(content)
        return ''.join(posts)