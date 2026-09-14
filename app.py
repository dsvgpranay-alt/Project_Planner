from flask import Flask,request,redirect,url_for,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project-details",methods=['GET','POST'])
def project_details():
    if request.method=="GET":
        return render_template("project.html")
    elif request.method=="POST":
        title=request.form.get('project_name')
        description=request.form.get('project_idea')
        project_type=request.form.get('project_type')
        techstack=request.form.get('technologies').split(',')
        time=request.form.get('time')
        goal=request.form.get('goal')
        

    
    
if __name__=="__main__":
    app.run(debug=True)

 