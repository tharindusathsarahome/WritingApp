from flask import render_template, redirect, request, url_for,session, abort,request
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import datetime
from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.dbModel.models import Users,Tokn,Pool,Admintb
from apps.authentication.util import verify_pass,hash_pass
from apps.authentication.google import *
from apps.authentication.emailVerification import email_otp_send,email_otp_verify
from apps.authentication.forgetPassword import send_link_,decode,dataEN



now = datetime.datetime.now()
today = now.date()
formatted_date = str(today.strftime("%Y-%m-%d"))

@blueprint.route("/Google")
def Google():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    session["google"] = request.args.get('name')
    return redirect(authorization_url)





@blueprint.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    print(id_info)
    
    password = id_info.get("sub")
    email = id_info.get("email")
    username = id_info.get("email")
    if session["google"]=='login':
        if id_info.get("email"):
            login_form = LoginForm(request.form)
            # Locate user
            user = Users.query.filter_by(username=username).first()
            userEmail = Users.query.filter_by(email=email).first()
    
            # Check the password
            if user or userEmail and verify_pass(password, user.password):

                login_user(user)
                return redirect(url_for('authentication_blueprint.route_default'))

            # Something (user or pass) is not ok
            return redirect('register')

        if not current_user.is_authenticated:
            return render_template('accounts/login.html',
                                form=login_form)
        return redirect(url_for('home_blueprint.index'))
    
    
    if session["google"]=='register':
        create_account_form = CreateAccountForm(request.form)
            # read form data

        # Check usename exists
        ToknViwe = Tokn.query.filter_by(userID=email).first()
        user = Users.query.filter_by(username=username).first()
        if user or ToknViwe :
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)


        tokn = Tokn(tokn='3000',payment='0',userID=username,Date=formatted_date)
        db.session.add(tokn)
        db.session.commit()

        # else we can create the user
        user = Users(username=username,email=email,password=password,Date=formatted_date)
        db.session.add(user)
        db.session.commit()
        RegistrationData.clear
        user = Users.query.filter_by(username=username).first()
        if user and verify_pass(password, user.password):
                login_user(user)
                return redirect(url_for('authentication_blueprint.route_default'))
  
    return redirect(url_for('home_blueprint.index'))
    


@blueprint.route('/')
def route_default():
    now = datetime.datetime.now()
    today = now.date()
    formatted_date = str(today.strftime("%Y-%m-%d"))
    IP = request.remote_addr
    try:
        pool = Pool(ip =IP ,Date=formatted_date)
        db.session.add(pool)
        db.session.commit()
        return redirect(url_for('authentication_blueprint.login'))
    except:
        return redirect(url_for('authentication_blueprint.login'))




@blueprint.route('/forgePassword', methods=['GET', 'POST'])
def forgePassword():
    if request.form:
        user = Users.query.filter_by(username=request.form['emali_forget']).first()
        if user :
            send_link_(request.form['emali_forget'],request.root_url)
            return render_template('accounts/emailview.html',email=request.form['emali_forget'])
            
        else:
             return redirect(url_for('authentication_blueprint.register'))

    return render_template('accounts/link_sendEmali.html')

@blueprint.route('/newPassword', methods=['GET', 'POST'])
def newPassword():
    if request.args:
        key = request.args['en']
        try:
            if decode(key):
                return render_template('accounts/forgetPassword.html')
            else:
                return render_template('accounts/link_sendEmali.html')
        except:
            return render_template('accounts/link_sendEmali.html')     
    if request.form:
        pwd = request.form['pass']
        hash_pass(pwd)
        try:
            user = Users.query.filter_by(username=dataEN['user']).first()
            user.password = hash_pass(pwd)
            db.session.commit()
        except:
            return render_template('accounts/register.html')
        return redirect(url_for('authentication_blueprint.login'))
    
    
    


# Login & Registration


@blueprint.route('/login', methods=['GET', 'POST'])
def login(): 
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(username=username).first()
       
   
        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))
        
        
        user = Users.query.filter_by(email=username).first()
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))
        
        
        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    
    
    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))

    
RegistrationData = []

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    print(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form :
        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        ToknViwe = Tokn.query.filter_by(userID=email).first()
        user = Users.query.filter_by(username=username).first()
        if user or ToknViwe :
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)
    
        email_otp_send(email)
        RegistrationData.append(request.form)
        return render_template('accounts/otp.html',success=False)
        
    elif RegistrationData:
        print(RegistrationData)
        if request.args['otp']:  
            if email_otp_verify(request.args['otp']): 
                from1 = RegistrationData[0]
                print(from1['username'])
                tokn = Tokn(tokn='3000',payment='0',userID=from1['username'],Date=formatted_date)
                db.session.add(tokn)
                db.session.commit()

                # else we can create the user
                user = Users(**from1,Date=formatted_date)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('authentication_blueprint.route_default'))
            else:
                return render_template('accounts/otp.html',success=False)
                
    else:
        return render_template('accounts/register.html', form=create_account_form)
    



@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
