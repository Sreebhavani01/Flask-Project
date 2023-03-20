from flask import Flask,render_template,request,flash,redirect,url_for,session
import sqlite3
app=Flask(__name__)
app.secret_key="123" 

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/login')    
def login():
    return render_template('signin.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('signout.html')

@app.route('/signup', methods = ["POST", "GET"])
def signup():
  
    if request.method == "POST":
        Username = request.form["Username"]
        EmailId = request.form["EmailId"]
        Password = request.form["Password"]
        try:
            with sqlite3.connect('user.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT into Users (Username, EmailId, Password) values (?, ?, ?)",(Username, EmailId, Password))
                flash('Registered successfully!', 'success')
                
                return render_template('signin.html')        
        except sqlite3.IntegrityError:
            flash("Username/EmailId already exist...", 'warning')
            return render_template('signup.html')
    return render_template('signin.html')

@app.route('/signin', methods = ["POST", "GET"])
def signin():
    
    if request.method == "POST":
        Username = request.form["Username"]
        Password = request.form["Password"]
        with sqlite3.connect('user.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * from Users where Username = ? and Password = ?", (Username, Password))
            data = cur.fetchone()
            if data:
                session['logged_in'] = True
                for data in cur:
                    session[Username] = data['Username']
                    session[Password] = data['Password']
                return render_template('index.html')
            else:
                session['logged_in'] = False
                flash("Invalid Username / Password...", 'warning')
                return render_template('signin.html')
    return render_template('signin.html')

                    
@app.route('/signout', methods = ["POST"])
def signout():
    Username = request.form['Username']
    EmailId = request.form['EmailId']
    Password = request.form['Password']
    with sqlite3.connect('user.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * from Users where Username = ? and Password = ?", (Username, Password))
            data = cur.fetchone()            
            if data:
                session['logged_in'] = False
                cur.execute("DELETE from Users where Username = ? and EmailId = ? and Password = ?", (Username, EmailId, Password))
                flash('You logged out!!', 'warning')
                return render_template('index.html')
            else:
                flash("Invalid Username / Password...", 'warning')
                return render_template('signout.html')
    return render_template('signout.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sub', methods=['POST','GET'])
def subdetails():
    if request.method=="POST":
        try:
            name=request.form["name"]
            phone=request.form["phone"]
            address=request.form["address"]
            query=request.form["query"]
            c=sqlite3.connect("query.db")
            cur=c.cursor()
            cur.execute("insert into queries(Name,Phone,Address,Queries) values (?,?,?,?)",(name,phone,address,query))
            c.commit()
        except:
            c.rollback()
        finally:
            return render_template("contact.html")

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/ordersave', methods=['POST','GET'])
def ordersave():
    if request.method=="POST":
        try:
            name=request.form["name"]
            phone=request.form["phone"]
            address=request.form["address"]
            email=request.form["email"]
            dish=request.form["dish"]
            date=request.form["date"]
            amount=request.form["amount"]
            c=sqlite3.connect("order.db")
            cur=c.cursor()
            cur.execute("insert into orders(Name,Phone,Address,Email,DishName,Date,Amount) values (?,?,?,?,?,?,?)",(name,phone,address,email,dish,date,amount))
            c.commit()
        except:
            c.rollback()
        finally:
            return render_template("order.html")

@app.route('/yourorder')
def yourorder():
    c=sqlite3.connect("order.db")
    c.row_factory=sqlite3.Row
    cur=c.cursor()
    cur.execute("select * from orders")
    r=cur.fetchall()
    return render_template("yourorder.html",row=r)

@app.route('/veg')
def veg():
    return render_template("veg.html")

@app.route('/breakfast')
def breakfast():
    return render_template("breakfast.html")

@app.route('/ice')
def ice():
    return render_template("ice.html")

@app.route('/juice')
def juice():
    return render_template("juice.html") 

@app.route('/coffee')
def coffee():
    return render_template("coffee.html")   

@app.route('/cooldrinks')
def cooldrinks():
    return render_template("cooldrinks.html")

@app.route('/dessert')
def dessert():
    return render_template("dessert.html")    

@app.route('/noodles')
def noodles():
    return render_template("noodles.html")  

@app.route('/soup')
def soup():
    return render_template("soup.html")

@app.route('/grain')
def grain():
    return render_template("grain.html")  

@app.route('/pizza')
def pizza():
    return render_template("pizza.html")  

if __name__=='__main__':
    app.run(debug=True)