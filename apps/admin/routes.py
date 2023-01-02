
from flask import render_template, redirect, request, url_for,session,jsonify
from apps.admin import blueprint
import os
from flask import render_template, request
from flask_login import login_required,current_user
from apps.dbModel.models import Pool,Users,Tokn
import datetime
from apps.config import Config

from datetime import date, timedelta

def generate_dates(num_days):
    today = date.today()
    dates = []
    for i in range(num_days):
        dates.append(today + timedelta(days=i))
    return dates




data_dic = {}
now = datetime.datetime.now()
today = now.date()
formatted_date = str(today.strftime("%Y-%m-%d"))

def poolCheck(date):
    poolData = Pool.query.filter_by(Date=date).all()
    ip_count = 0
    for ip_a in poolData:
        ip_count+=1
    return ip_count

def usercheck(date):
    UserData = Users.query.filter_by(Date=date).all()
    User_count = 0
    for UserData_a in UserData:
        User_count+=1
    return User_count
def pay_cus(date):
    cus = Tokn.query.filter_by(Date=date).all()
    cus_count = 0
    for cusData_a in cus:
        if cusData_a.payment == '1':
            cus_count+=1
    return cus_count

def comb_Loop(date):
    for m in date:
        m = str(m)
        data_dic[m]=[usercheck(m),poolCheck(m),pay_cus(m)]
    

@blueprint.route('/admin',methods=['POST','GET'])
@login_required
def adminPanl():
    if Config.ADMIN_USER == str(current_user):
        num_days = 30  # Generate dates for the next 30 days
        dates = generate_dates(num_days)
        comb_Loop(dates)
        return render_template("admin/index.html",data_=data_dic)
    else:
        return redirect(url_for("home_blueprint.index"))        
        
