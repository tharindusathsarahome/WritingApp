# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for,session
from apps.tool import blueprint
from apps.tool.forms import ToolForm
from apps.tool.writingTool import dataJson
from flask_login import login_required,current_user
from apps.tool.backend import call
from apps.dbModel.models import Tokn
from apps import db



@blueprint.route('/tool',methods=['GET', 'POST'])
@login_required
def tool():
    toolName = request.args.get('name')
    data=dataJson[toolName]
    if request.form:
        Tokntot=0
        fromData=call(toolName,request.form)
        for toknArry in fromData:
            Tokntot+=int(fromData[toknArry][0])
        userName=str(current_user)
        tokn = Tokn.query.filter_by(userID=userName).first()
        if int(tokn.tokn) < Tokntot:
            return redirect('payment')
        toknVal=int(tokn.tokn)-Tokntot
        tokn.tokn = toknVal
        db.session.commit()
        tokn = Tokn.query.filter_by(userID=userName).first()
      
    else:
        fromData= False
        userName=str(current_user)
        tokn = Tokn.query.filter_by(userID=userName).first()
    tool_form = ToolForm(request.form)
    
    return render_template("tool/tool.html",form=tool_form,ToolData=data,classMarch=getattr,OutPut = fromData,ToknData=tokn.tokn)


