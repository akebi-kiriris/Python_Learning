from flask import Flask
from flask import url_for
from markupsafe import escape


#創建程序對象
app = Flask(__name__)

#註冊處理函數，以處理某個請求。
#使用app.route()這個裝飾器為函數綁定url
#當訪問這個url就會觸發以下函數(視圖函數)
@app.route("/")
def hello():
    return "Hello, World"


#一個視圖函數可綁定多個url。
@app.route("/clapping")
@app.route("/greeting")
def greeting():
    return "<b>%%%<b>"

#可在回傳值中使用HTML標籤，因回傳值會被瀏覽器當作html格式解析
@app.route("/dodoro")
def dodoro():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# URL 中的變數會被傳入視圖函數作為參數
#為防止輸入的值包含惡意代碼，使用escape函數轉義，
#如把<轉為&lt，返回值時瀏覽器不會將其作為程式碼執行
@app.route('/user/name/<name>')
def user_page(name):
    return f'User: {escape(name)}'

#int:age 是 Flask 的 路由轉換器，它限定 age 必須是整數，否則不會匹配這個路由。
#只有值為整數時才會執行這個視圖函數。
@app.route('/user/age/<int:age>')
def user_age(age):
    return f"User's age : {age}"

@app.route("/test")
def test_url_for():
    #url_for會生成該視圖函數對應的url
    #print會印在終端機
    # /
    print(url_for('hello'))
    # /user/greyli
    print(url_for('user_page', name='greyli')) 
    # /user/peter
    print(url_for('user_page', name='peter'))  
    # /test
    print(url_for('test_url_for'))  
    # /test?num=2
    print(url_for('test_url_for', num=2))  
    
    urls = [
        url_for('hello'),
        url_for('user_page', name='greyli'),
        url_for('user_page', name='peter'),
        url_for('test_url_for'),
        url_for('test_url_for', num=2),
    ]
    #不可這樣，'Test page'會被當為內容，'<br>'.join(urls)會被當作http狀態碼
    #return 'Test page' ,'<br>'.join(urls)   
    return 'Test page<br>' + '<br>'.join(urls)

# 直接執行此檔案時，啟動 Flask 伺服器（開啟 debug 模式）
if __name__=="__main__":
    app.run(debug=True)