

from apps.home import blueprint
from apps.home.writingTool import dataJson
from flask import render_template, request,url_for,redirect
from flask_login import login_required,current_user
from jinja2 import TemplateNotFound
from apps.dbModel.models import Tokn
from apps.authentication.emailVerification import email_send
from apps.payment.data import yearChek




@blueprint.route('/index')
@login_required
def index():
    userName=str(current_user)
    
    try:
        yearChek(userName)
        tokn = Tokn.query.filter_by(userID=userName).first()
        return render_template('home/index.html', segment='index',viewTool=dataJson,ToknData = tokn)

    except:
        
         tokn = Tokn.query.filter_by(userID=userName).first()
         return render_template('home/index.html', segment='index',viewTool=dataJson,ToknData = tokn)


@blueprint.route('/contact-us',methods=['POST','GET'] )
@login_required
def contact_us():
    if request.form:
        msg = f"""Subject: Request Tools {request.form['name']}\n\nHi there!\n{request.form['email']}\n{request.form['message']}\n\nThank you for your time,\n\n{request.form['name']}"""
        if email_send(msg):
            return redirect(url_for('home_blueprint.index')) 
    userName=str(current_user)
    tokn = Tokn.query.filter_by(userID=userName).first()
    return render_template('home/contact.html',viewTool=dataJson,ToknData = tokn)





@blueprint.route('/<template>')
@login_required
def route_template(template):
   

    try:
        
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

