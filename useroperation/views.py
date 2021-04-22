import hashlib
import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from .forms import UserLoginForm
from . import models


# Create your views here.

def logins(request):
    return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        context = {'status': ''}
        username = request.POST.get('username')
        user = models.User.objects.filter(username=username).first()
        if user:
            password = request.POST.get('password')
            if hash_paw(password) == user.password:
                # 将用户数据保存在 session 中，即实现了登录动作
                request.session['status'] = True
                request.session['username'] = username
                request.session['id'] = user.id
                return redirect("post:home")
            else:
                return render(request, 'login.html', context=context)
        else:
            return render(request, 'login.html', context=context)

    elif request.method == 'GET':
        return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
    return redirect("post:home")


def hash_paw(pwd):
    md = hashlib.md5()
    md.update(pwd.encode('utf-8'))
    return md.hexdigest()


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # 表单验证

        user = models.User.objects.filter(username=username).first()
        e_mail = models.User.objects.filter(e_mail=email).first()
        if user:
            return render(request, 'register.html', {'status': 'username'})
        if e_mail:
            return render(request, 'register.html', {'status': 'email'})
        # 加密密码
        hash_password = hash_paw(password)
        # 写数据库
        try:
            user = models.User(username=username, password=hash_password, e_mail=email)
            user.save()
            print('保存成功')
            return render(request, 'login.html', {'status': True})
        except Exception as e:
            print('保存失败', e)
            return redirect('useroperation:register')
    return None


# 随机生成验证码
def random_str(randomlength=6):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 发送邮件找回密码
def findpwd(request):
    return render(request, 'findpwd.html', {'status': False,'error': ''})


# 点击获取验证码，得到名字
def send_email(request):
    print("*******************")
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, password)
        if password:
            try:
                new_pwd = request.POST.get("password")
                auth_code = request.POST.get("auth_code")
                print(username, new_pwd, auth_code)
                if username == request.session["user_name"]:
                    print("name相同")
                    if auth_code == request.session["auth_code"]:
                        print("验证码相同")
                        user = models.User.objects.get(username=username)
                        user.password = hash_paw(new_pwd)
                        user.save()
                        del request.session["auth_code"]  # 删除session
                        return render(request, 'login.html', {'error': ''})
                    else:
                        return render(request, 'findpwd.html', {'error': '验证码错误'})
                else:
                    return render(request, 'findpwd.html', {'error': '用户名错误'})
            except:
                return render(request, 'findpwd.html', {'error': '验证码过期，请重新获取'})

        else:
            try:
                user = models.User.objects.get(username=username)
                request.session["user_name"] = user.username
                email_title = "找回密码"
                code = random_str()  # 随机生成的验证码
                request.session["auth_code"] = code  # 将验证码保存到session
                request.session.set_expiry(300)
                email_body = "验证码为：" + code+"\n有效时间为5分钟。"
                print("////////")
                # render(request, 'findpwd.html', {'status': True})
                send_status = send_mail(subject=email_title, message=email_body, from_email="weiquan_xu@foxmail.com",
                                        recipient_list=[user.e_mail, ])
                return render(request, 'findpwd.html', {'status': True,'no_user': False,'error': ''})
            except Exception as e:
                print(e)
                return render(request, 'findpwd.html', {'status': False,'no_user': True,'error': ''})
