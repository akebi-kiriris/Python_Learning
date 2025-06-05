from flask import Flask
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

#Column常用參數
#1.db.String(n)    字串
#2.db.Integer      整數
#3.db.Text         長字串
#4.db.Boolean      布林值
#5.db.DateTime     日期時間
#6.db.Float        浮點數
#7.db.ForeignKey('table.column')  外鍵
#8.nullable=False  不可為空
#9.unique=True     值必須為唯一
#10.default=n      預設值
#11.index=True     建立索引，加快查詢


#常用指令
#db.create_all()   建立所有尚未存在的資料表
#db.drop_all()     刪除所有資料表

#新增資料
# user1 = User(username='alice', email='alice@example.com')
# db.session.add(user1)  加入 session
# db.session.commit()    提交變更

#查詢資料
# users = User.query.all()               # 查詢所有
# user = User.query.get(1)               # 根據主鍵查詢
# user = User.query.filter_by(username='alice').first()  # 條件查詢

#修改資料
#user = User.query.get(1)
# user.email = 'new@example.com'
# db.session.commit()

#刪除資料
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()


#關聯設定(一對多)
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text)
#     #設定外鍵
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     user = db.relationship('User', back_populates='posts')

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20))
#     posts = db.relationship('Post', back_populates='user', cascade="all, delete-orphan")
    
    
if __name__=="__main__":
    app.run(debug=True)