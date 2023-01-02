

from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,IntegerRangeField
from wtforms.validators import  DataRequired

# login and registration

class ToolForm(FlaskForm):
    selectCreativity = SelectField(u'creativity', choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'),])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    selectGremar = SelectField(u'Gremar', choices=[('Active voice', 'Active voice'), ('Passive voice', 'Passive voice')])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    selectToneOfVoice = SelectField(u'Tone-Of-Voice', choices=[('Professional', 'Professional'), ('Childish', 'Childish'), ('Luxurious', 'Luxurious'), ('Confident', 'Confident'), ('Exciting', 'Exciting')])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    selectEmail = SelectField(u'Email', choices=[('Newsletter ', 'Newsletter '), ('Lead nurturing ', 'Lead nurturing '), ('Promotional ', 'Promotional '), ('Milestone ', 'Milestone '), ('Survey ', 'Survey ')])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    selectEcommerce = SelectField(u'Ecommerce', choices=[('Points ', 'Bullet Points '), ('Description ', 'Description ')])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    selectStyle = SelectField(u'Style', choices=[('formal', 'Formal'), ('motivated', 'Motivated'), ('concerned', 'Concerned'), ('disappointed', 'Disappointed')])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    txtA1 = TextAreaField('txta1',validators=[DataRequired()])
    txtA2 = TextAreaField('txta2',validators=[DataRequired()])
    txtA3 = TextAreaField('txta3',validators=[DataRequired()])
    txtA4 = TextAreaField('txta4',validators=[DataRequired()])
    txtA5 = TextAreaField('txta5',validators=[DataRequired()])
    rang1=IntegerRangeField('range',validators=[DataRequired()])
    txt1 = StringField('txt1',validators=[DataRequired()])
    txt2 = StringField('txt2',validators=[DataRequired()])
    txt3 = StringField('txt3',validators=[DataRequired()])
    txt4 = StringField('txt4',validators=[DataRequired()])
    txt5 = StringField('txt5',validators=[DataRequired()])
    txt6 = StringField('txt6',validators=[DataRequired()])
    txt7 = StringField('txt7',validators=[DataRequired()])
    txt8 = StringField('txt8',validators=[DataRequired()])
    txt9 = StringField('txt9',validators=[DataRequired()])
    txt10 = StringField('txt10',validators=[DataRequired()])
 


