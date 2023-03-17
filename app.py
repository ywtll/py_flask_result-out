import yaml
from flask import Flask, render_template, request, session, redirect, request
from util.xl import read_xl
from util.logtime import logs_time

app = Flask(__name__)
app.secret_key = 'skdcfvlnm'  # 对用户信息加密
log = logs_time()

# read yaml file
with open("xl/config.yaml", "r", encoding="utf8") as read_yaml_file:
    config_dict = yaml.load(read_yaml_file, Loader=yaml.FullLoader)

    # 设置变量
    id_src = config_dict["id_src"]
    score_src = config_dict["score_src"]
    subject = config_dict["subject"]
    log_src = config_dict["log_src"]


@app.route('/', methods=['GET', 'POST'])
def login():  # put application's code here
    # 获取客户端的ip
    ip = request.headers.get('X-Real-Ip') or request.remote_addr

    # 如果是get请求，访问网页
    if request.method == 'GET':
        return render_template('login.html')

    # 如果是post请求，就是登录操作

    # 日志
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    log.aw_log(dest=log_src, name=str(user), v="attempt login", ip=ip)  # 日志

    try:
        xl = read_xl()
        # 区分两种格式
        if id_src[-4:] == ".xls":
            list_dict = xl.read_xls_dict(dest=id_src, row_id=1, data="")
        else:
            list_dict = xl.read_xlsx_dict(dest=id_src, row_id=1, data="")

        list_name = list_dict[user]
        # 验证正确
        if list_name[-4:] == str(pwd)[-4:]:
            session['user_info'] = user
            log.aw_log(dest=log_src, name=str(user), v="login success!", ip=ip)  # 日志
            return redirect('/up')
        # 密码错误
        else:
            log.aw_log(dest=log_src, name=str(user), v="login passwd error!", ip=ip)  # 日志
            return render_template('login.html', msg='姓名或学号输入错误')
    except Exception as e:
        log.aw_log(dest=log_src, name=str(user), v="[pwd:" + str(pwd) + "]" + str(e), ip=ip)  # 日志
        return render_template('login.html', msg='姓名或学号输入错误')


@app.route('/up')
def index():
    # 获取客户端的ip
    ip = request.headers.get('X-Real-Ip') or request.remote_addr

    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    log.aw_log(dest=log_src, name=str(user_info), v="login success and get into!", ip=ip)  # 日志

    xl = read_xl()
    if score_src[-4:] == ".xls":
        list_dict = xl.read_xls_dict(dest=score_src, row_id=1, data="000")
    else:
        list_dict = xl.read_xlsx_dict(dest=score_src, row_id=1, data="000")
    score = list_dict[user_info]

    return render_template("up.html", subject=subject, user_info=user_info, score=score[0:len(score) - 3])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
