import os
from flask import Flask,request,redirect,url_for,render_template
from google import genai
from google.genai import types
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

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
        prompt = f"""
                You are DevPath, an AI project planning assistant.

                The user wants to build a project with the following details:

                Project name: {title}
                Project idea: {description}
                Project type: {project_type}
                Technologies they already know: {techstack}
                Available timeframe: {time}
                Main goal: {goal}

                Analyze the project and create a practical development plan.

                The response must be valid JSON.
                Include these fields:
                1. project_overview
                2. core_features
                3. recommended_tech_stack
                4. system_architecture
                5. architecture_diagram
                6. database_design
                7. development_roadmap
                8. concepts_to_learn
                9. future_improvements

                For architecture_diagram:
                - Return a Mermaid flowchart.
                - Show the main components of the system and how they interact.
                - Keep it simple and easy to understand.
                - Use Mermaid flowchart syntax.
                - Do not use Markdown code fences.
                - Do not include explanations outside the JSON.

                Example:

                "architecture_diagram": "flowchart TD
                    A[User] --> B[Frontend]
                    B --> C[Backend]
                    C --> D[Database]"
                """
        try:
            response=client.models.generate_content( model="gemini-3.6-flash",contents=prompt,config=types.GenerateContentConfig(response_mime_type="application/json"))
            data=json.loads(response.text)
            return render_template("plan.html",data=data)
        except Exception as e:
            return {"ERROR":str(e)} , 500

    
if __name__=="__main__":
    app.run(debug=True)

 