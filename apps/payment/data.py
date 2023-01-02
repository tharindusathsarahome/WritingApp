import datetime
from apps.dbModel.models import Payment,Tokn
from apps import db

def yearChek(user):
    now = datetime.datetime.now()
    today = now.date()
    formatted_date = today.strftime("%Y-%m-%d")
    Data = Payment.query.filter_by(userID=user).first()  
    start_date = datetime.datetime.strptime(Data.stat, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(Data.end, "%Y-%m-%d")
    date_to_check = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")
    if start_date <= date_to_check <= end_date:
        currant_date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")
        print(currant_date.month)
        if str(currant_date.month) == Data.month:
            return True
        else:
            tokn = Tokn.query.filter_by(userID=user).first()
            tokn.tokn = Data.tokn
            Data.val = str(int(Data.val)+1)
            Data.month = currant_date.month
            db.session.commit()
            return False
    else:
        return 'over'
def AddPayment(user,Tokn):
    now = datetime.datetime.now()
    today = now.date()
    formatted_date = today.strftime("%Y-%m-%d")
    month = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")
    today = datetime.date.today()
    next_year = str(today.replace(year=today.year + 1))
    PAY = Payment(tokn=Tokn,month=month.month,val='1',stat =formatted_date ,end =next_year,userID=user)
    db.session.add(PAY)
    db.session.commit()
 
    
    
