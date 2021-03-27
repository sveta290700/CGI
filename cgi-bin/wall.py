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
  avatar = form.getfirst("avatar", "")
  avatar = html.escape(avatar)
  if len(login) > 0 and len(avatar) > 0:
    wall.register(login, avatar)
    cookie = wall.set_cookie(login)
    print('Set-cookie: session={}'.format(cookie))
  elif wall.find(login):
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
    <main style="width: 70%;transform: translate(20%, 1rem)">
    <form class="mew-form" action="/cgi-bin/wall.py">
      
      {login}
      
      {publish}
      <input type="submit" class="button-primary" value="{form}">
    </form>
    
    <div class="mews">
    
        {posts}
    
    </div>
  </main>
</body>
<script src="/client.js">
</html>
'''

if len(cookie) > 1: # just a piece of shit statement,
  # because there is no way to write it otherwise classes in python suck
  user = wall.find_cookie(cookie)

if user is not None:
  form = 'Send'
  avatar = '<div class="one column">' + wall.get_html_avatar(user) + '</div>'
  login = '''
  <div class="row">
  <div class="ten columns">
  <label for="name">Logged in as:</label>
  </div>
  <div class="two columns">
  <button class="button" onclick="logout()" style="color: #FFF;background-color:#ff6060;border-color:#ff6060;transform: translateX(10%)">Log out</button>
  </div>
  </div>
  <div class="row" style="display: flex;align-items: center">''' + avatar + '''
  <div class="one-half column">
      <h5 style="transform: translateX(0rem)" class="u-full-width">''' + user + '''</h5></div></div>'''
  pub = '''
    <script>
        function logout() {
          document.cookie = "session= ; expires = Thu, 01 Jan 1970 00:00:00 GMT";
          return false;
        }
    
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
  form = 'Sign In'
  avatar_field = '''
  <div class="one-half column">
  <label for="avatar">Avatar</label>
      <input class="u-full-width" type="text" id="avatar" name="avatar">
      </div>
  '''
  login = '''
  <div class="row" style="display: flex;align-items: center">
  <div class="one-half column">
      <label for="name">Name</label>
      <input class="u-full-width" type="text" id="login" name="login"></div>
  ''' + avatar_field + '''</div>'''
  pub = '''
     <input type="hidden" name="action" value="login">
    '''

print('Content-type: text/html\n')

posts = wall.html_list()
res = pattern.format(posts=posts,
                     publish=pub,
                     form=form,
                     login=login,
                     )
print(res)