from flask import Flask,render_template,request
import sqlite3
from web_scraper import get_content


app=Flask(__name__,template_folder='Template') 

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/get_url/",methods=["POST"])
def get_url():  
    url = request.json.get("url")
    content = get_content(url)
    
    # data=con.execute("SELECT * from contents")
    # print(data)
    # con.commit()
    # con.close()
    return {"content":content}

@app.route("/save_content/",methods=["POST"])
def save_data():
    content = request.json.get("content")
    
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()  
        cur.execute("SELECT * from contents")
        n = len(cur.fetchall()) 
        cur.execute('''INSERT INTO contents VALUES(?,?)''',(n+1,"str(content)"))
        con.commit() 
        con.close()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"
    

@app.route("/get_content/",methods=["GET"])
def get_data():
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        data = cur.execute("SELECT * from contents")
        saved_data={"dt":[]}
        for i in data:
            d={}
            d["content"]=i
            saved_data["dt"].append(d)
        con.commit() 
        con.close() 
        return {"response":saved_data}
    except Exception as e:
        print(e)
        return "FAILED"


if __name__=="__main__":
    app.run(debug=True)