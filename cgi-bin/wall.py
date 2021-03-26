#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os

from _wall import Wall
wall = Wall()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
if session is not None:
    session = session.value
user = wall.find_cookie(session)  # Ищем пользователя по переданной куке

form = cgi.FieldStorage()
action = form.getfirst("action", "")

if action == "publish":
    text = form.getfirst("text", "")
    text = html.escape(text)
    if len(text) > 0:
        if text and user is not None:
            wall.publish(user, text, wall.get_avatar(user))
    else:
        action = "login"
if action == "login":
    login = form.getfirst("login", "")
    login = html.escape(login)
    password = form.getfirst("password", "")
    password = html.escape(password)
    avatar = form.getfirst("avatar", "")
    avatar = html.escape(avatar)
    if wall.find(login, password):
        cookie = wall.set_cookie(login)
        print('Set-cookie: session={}'.format(cookie))
    elif wall.find(login):
        pass  # А надо бы предупреждение выдать
    elif len(login) > 0 and len(password) > 0 and len(avatar) > 0:
        wall.register(login, password, avatar)
        cookie = wall.set_cookie(login)
        print('Set-cookie: session={}'.format(cookie))

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Twitter</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Форма логина и регистрации. При вводе несуществующего имени зарегистрируется новый пользователь.
    <form class="mew-form" action="/cgi-bin/wall.py">
        Логин: <input type="text" name="login">
        Пароль: <input type="password" name="password">
        Аватар: <input type="text" name="avatar">
        <input type="hidden" name="action" value="login">
        <input type="submit">
    </form>
    //-->
    
    <main>
    <form class="mew-form" action="/cgi-bin/wall.py">
      <div class="error-message">
      </div>
      <label for="name">Name</label>
      <input class="u-full-width" type="text" id="login" name="login", value={val}>
      <label for="name">Password</label>
      <input class="u-full-width" type="password" id="password" name="password">
      <label for="name">Avatar</label>
      <input class="u-full-width" type="text" id="avatar" name="avatar">
      {publish}
      <input type="submit" class="button-primary">
    </form>
    
    <div class="mews">
    
        {posts}
    
    </div>
  </main>
</body>
<script src="/client.js">
</html>
'''

if user is not None:
    pub = '''
    <script>
        function add(str) {
            document.getElementById("content").value += str
        }
    </script>
    <label for="content">Post</label>
    <textarea class="u-full-width for-emoji" type="text" id="content" name="text"></textarea>
    <div>
    <input type="button" value="😄" onclick="add(\'😄\')">
    <input type="button" value="😉" onclick="add(\'😉\')">
    <input type="button" value="😏" onclick="add(\'😏\')">
    <input type="button" value="🤣" onclick="add(\'🤣\')">
    <input type="button" value="😎" onclick="add(\'😎\')">
    <input type="button" value="😭" onclick="add(\'😭\')">
    <input type="button" value="😈" onclick="add(\'😈\')">
    <input type="button" value="🙅‍♀️" onclick="add(\'🙅‍♀️\')">
    <input type="button" value="😼" onclick="add(\'😼\')">
    </div>
    <input type="hidden" name="action" value="publish">
    '''
else:
    pub = '''
     <input type="hidden" name="action" value="login">
    '''

print('Content-type: text/html\n')

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
if session is not None:
    session = session.value
user = wall.find_cookie(session)
posts = wall.html_list()
print(pattern.format(posts=posts, publish=pub, val=user))