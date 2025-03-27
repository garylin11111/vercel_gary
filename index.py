from flask import Flask,render_template, request
from datetime import datetime, timezone, timedelta



app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>林政彥Python網頁(時間+8)</h1>"
	homepage +="<a href=/mis>MIS</a><br>"
	homepage +="<a href=/today>顯示日期時間</a><br>"
	homepage +="<a href=/welcome?nick=政彥>傳送使用者暱稱</a><br>"
	homepage +="<a href=/account>網頁表單傳值</a><br>"
	homepage +="<a href=/rwd>政彥簡介網頁</a><br>"
	return homepage

@app.route("/mis")
def mis():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
	tz = timezone(timedelta(hours=+8))
	now = datetime.now(tz) 
	return render_template("today.html", datetime = str(now))

@app.route("/rwd")
def me():
	return render_template("rwd.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

if __name__ == "__main__":
	app.run()
