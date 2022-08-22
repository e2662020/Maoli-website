from flask import *
app = Flask(__name__)#设置app为主函数


#设置主页
@app.route("/")
def  index():
    return render_template("index.html")

#设置提交页面
@app.route("/dcxm.html")
def dcxm():
    return render_template("dcxm.html")

#设置返回页面
@app.route("/privatepic")
def input():
    this = request.values.get("who")
    this1 = this+'\n'
    open("1.txt","a").write(str(this1))
    return render_template("OK.html")
app.run()