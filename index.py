from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import MethodNotAllowed
app = Flask (__name__)
secret_key =secrets.token_hex(32)
app.secret_key = secret_key
id_list = []
@app.route ("/")
def home():
    return render_template ("home.html")
@app.route ("/VisionandMission")
def VisionandMission():
    return render_template ("VisionAndMission.html")


@app.route ("/WhoCanCant")
def WhoCanCant():
    return render_template ("can and cant.html")

@app.route("/homepage")
def home1():
    return render_template("home1.html")

@app.route ("/need")
def need():
    return render_template ("needofblood.html")


@app.route ("/precaution")
def precaution():
    return render_template ("precautions.html")


@app.route ("/feedback", methods=["GET", "POST"])
def feedback():
    return render_template("feedback.html")

@app.route("/postfeedback",methods=["GET","POST"])
def post():
    msg=" "
    feedback = request.form['feedbackText']
    rating = request.form.get('rating')
    print(feedback)
    if feedback:
        try:
            conn = sqlite3.connect ('feedback.db')
            cursor = conn.cursor ()
            cursor.execute ('INSERT INTO feedback(content,rating) VALUES(?,?)', (feedback, rating))
            conn.commit ()
            conn.close ()
            msg = "Thanks For your Feedback"
        except Exception as e:
            print("Error:",str(e))
    return render_template("thank_you_feedback.html",msg=msg)
@app.route ("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']
        conn=sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?',(email,password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]
            flash('login successful','success')
            return redirect(url_for('home1'))
        else:
            flash('login failed. please check your email and password.','error')
    return render_template ("login.html")

@app.route('/logout')
def logout():
    return redirect(url_for('home'))
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return redirect(url_for("home1"))
    else:
        flash('you need to login first.','error' )
        return  redirect(url_for('login'))
@app.route ("/signup",methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        phone = request.form['phoneno']
        password = request.form['pass']
        confirm_password = request.form['pass1']
        if password != confirm_password:
            flash('Passwords do not match.Please try again.','danger')
            return  render_template('signup.html')
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(firstname,lastname,email,phone,password) VALUES(?,?,?,?,?)",
                       (firstname,lastname,email,phone,password))
        conn.commit()
        conn.close()
        flash('Account created successfully!','success')
        return  redirect(url_for('login'))
    return render_template('signup.html')
@app.route ("/findblood")
def findblood():
    return render_template ("findblood.html")

@app.route("/search",methods = ['POST'])
def searchdonar():
    location = request.form['location1'].strip()
    blood_group = request.form['blood_group1'].strip()
    print(repr(location))
    print(repr(blood_group))
    conn = sqlite3.connect('volunteer.db')
    cursor = conn.cursor()
    cursor.execute ('SELECT * FROM Donor WHERE LOWER(loc)=LOWER(?) AND LOWER(blood_group) =LOWER(?)',
                    (location, blood_group))
    matching_donors = cursor.fetchall()
    if matching_donors:
        conn.close ()
        return render_template("SearchDonar.html",donors=matching_donors)
    else:
        message = "Sorry,No matching donors found."
        return render_template('nomatch.html',message=message)
@app.route ("/donate")
def donate():
    return render_template ("Donate.html")
@app.route ("/addrec", methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            firstName = request.form['fn']
            lastName = request.form['ln']
            email = request.form['ei']
            phoneNumber = request.form['pn']
            DOB = request.form['dob']
            location = request.form['loc']
            bloodGroup = request.form['bg']
            with sqlite3.connect ('volunteer.db') as con:
                cur = con.cursor()
                cur.execute(
                    """INSERT INTO Donor (first_name,last_name, email,phone_No,dob,loc,blood_group) VALUES (?,?,?,?,?,?,?)""",
                    (firstName, lastName, email, phoneNumber, DOB, location, bloodGroup))
                con.commit()
                msg = "Your Donor Registration Successfully completed"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            con.close()
            return render_template ("result.html", msg=msg)

if __name__ == "__main__":
    app.run (debug=True, port=5003)
