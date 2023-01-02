
from flask import render_template, redirect, request, url_for,session,jsonify
from apps.payment import blueprint
from apps.payment.forms import LoginForm
import os
import stripe
from flask import render_template, request
from flask_login import login_required,current_user
from apps.dbModel.models import Tokn
from apps import db
from apps.payment.paymentData import formData,ToknData
from apps import config
from apps.payment.data import yearChek,AddPayment

stripe.api_key = config.Config.PAYMENT_API_KEY


def priceData(data):
    return formData[data]

            

@blueprint.route('/payment',methods=['POST','GET'])
@login_required
def tool():
    login_form = LoginForm(request.form)
    userName=str(current_user)
    if request.args:
        tokn = Tokn.query.filter_by(userID=userName).first()
        Tokntot = ToknData[request.args.get('data')]
        toknVal=int(tokn.tokn)+Tokntot[0]
        tokn.tokn = toknVal
        tokn.payment=1
        db.session.commit()
        if Tokntot[1] == 'Yearly':
            AddPayment(userName,tokn.tokn)
    tokn = Tokn.query.filter_by(userID=userName).first()
    try:
        yearChek(userName)
        return render_template("payment/payment.html",form=login_form,ToknData=tokn.tokn)
    except:
        return render_template("payment/payment.html",form=login_form,ToknData=tokn.tokn)
        
@blueprint.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    root=request.url_root
    try:
        pr_= request.form.get('hideData')
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact PriceID (for example, pr_1234) of the product you want to sell
                    'price':priceData(pr_),
                    'quantity': 1,
                }
                
            ],
            mode='subscription',
            success_url=root+f'payment?data={priceData(pr_)}',
            cancel_url=root+'payment',
        
        )
    except Exception as e:
        return str(e)
  
    print(checkout_session)
    return redirect(checkout_session.url,code=303)


