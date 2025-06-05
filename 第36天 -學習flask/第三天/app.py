from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import click

# 建立 Flask 應用實例
app=Flask(__name__)

# 設定資料庫連線（這裡使用 SQLite，資料庫檔案為 data.db）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy，傳入 Flask 應用實例
db = SQLAlchemy(app)

#表名為user(小寫)，對應的 ORM 類別是 User
#deepseek解釋
#ORM 全名是 Object-Relational Mapping（物件關聯對應）。
#意思是：把資料庫的「資料表（table）」對應成程式中的「類別（class）」，
# 讓你可以用寫 Python 類別的方式操作資料庫。

class User(db.Model):
    # 主鍵欄位，整數型別，自動遞增
    id= db.Column(db.Integer, primary_key=True)
    # 名稱欄位，字串型別，最大長度 20
    name = db.Column(db.String(20))
    
# 定義一個名為 movie 的資料表（預設表名會根據類別 Movie 轉為小寫）
class Movie(db.Model):  
    # 主鍵欄位，整數型別，自動遞增
    id = db.Column(db.Integer, primary_key=True) 
    # 電影標題欄位，最大長度 60 的字串
    title = db.Column(db.String(60)) 
    # 電影年份欄位，限制為 4 個字元 
    year = db.Column(db.String(4))  

# 註冊一個 Flask CLI 指令，名稱為 initdb
@app.cli.command()
# 定義一個 CLI 的選項 --drop，使用者輸入時可選擇是否要先刪除資料表

# 初始化資料庫（不刪除原有表格）
#flask initdb
# 先刪除再重新建立資料表
#flask initdb --drop

@click.option('--drop', is_flag=True, help='Create after drop.') 
def initdb(drop):
    """Initialize the database."""
    # 如果有加上 --drop 參數，就先刪除資料庫中的所有資料表
    if drop:  
        db.drop_all()
    # 建立所有定義好的資料表（根據模型類別）
    db.create_all()
    
    click.echo('Initialized database.')  
    
@app.route("/")
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)

#註冊指令加入資料
@app.cli.command()
def forge():
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')

if __name__=="__main__":
    app.run(debug=True)
