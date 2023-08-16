from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
fai=Flask(__name__)

class Nameform(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()
@fai.route('/webforms',methods=['GET','POST'])
def webforms():
    nf=Nameform()
    if request.method=='POST':
        form_data=Nameform(request.form)
        if form_data.validate():
            return form_data.data
    return render_template('webforms.html',nf=nf)


@fai.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        fd=request.form
        return str(fd)
    return render_template('htmlforms.html')

if __name__=='__main__':
    fai.run(debug=True)