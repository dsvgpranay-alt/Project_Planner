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
        techstack=[tech.strip() for tech in request.form.get('technologies').split(',')]
        time=request.form.get('time')
        goal=request.form.get('goal')
        prompt = f"""
            You are DevPath, an AI project planning assistant.
            Create a practical, detailed, and realistic development plan for the following project:

            Project Name: {title}
            Project Idea: {description}
            Project Type: {project_type}
            Technologies Known: {techstack}
            Available Time: {time}
            Main Goal: {goal}

            Return ONLY one valid JSON object.

            The JSON must contain EXACTLY these 9 top-level keys:

            project_overview
            core_features
            recommended_tech_stack
            system_architecture
            database_design
            development_roadmap
            concepts_to_learn
            future_improvements
            architecture_diagram

            Requirements:

            project_overview:
            Give a clear explanation of the project, its purpose, the problem it solves, and how it will work.

            core_features:
            List the important features that should be implemented. Choose the number of features based on the project's complexity. Do not artificially limit the number of features.

            recommended_tech_stack:
            Recommend suitable technologies for:
            - frontend
            - backend
            - database
            - APIs
            - deployment

            Prioritize technologies the developer already knows. Recommend new technologies only when they provide a meaningful benefit.

            system_architecture:
            Explain the major components of the system, their responsibilities, and how they communicate with each other. Describe the overall data flow between the frontend, backend, database, and external APIs when applicable.

            database_design:
            Describe the main database entities or tables and their important fields. Only include database entities that are actually relevant to the project. If persistent database storage is not required, return an empty array.

            development_roadmap:
            Create a practical step-by-step implementation roadmap based on the available timeframe. Break the development into logical phases and include the important tasks that should be completed in each phase.

            concepts_to_learn:
            List the important technical concepts the developer should understand to successfully build the project.

            future_improvements:
            Suggest useful features, scalability improvements, security improvements, performance improvements, or advanced functionality that could be added after the initial version.
            architecture_diagram:
            Generate a concise Mermaid diagram showing the main components of the system and how data flows between them.

            Rules:
            - Return ONLY valid Mermaid syntax.
            - Start with "graph TD".
            - Do not use Markdown code fences.
            - Do not include explanations.
            - Do not use ```mermaid.
            - Keep the diagram concise and readable.
            - Use simple node labels.
            - Show the main flow between frontend, backend, database, and external APIs when applicable.
            - Adapt the diagram to the actual project.
            Use this JSON structure:

            {{
                "project_overview": "string",
                "core_features": ["string"],
                "recommended_tech_stack": {{
                    "frontend": ["string"],
                    "backend": ["string"],
                    "database": ["string"],
                    "apis": ["string"],
                    "deployment": ["string"]
                }},
                "system_architecture": ["string"],
                "database_design": [
                    {{
                        "entity": "string",
                        "fields": ["string"]
                    }}
                ],
                "development_roadmap": [
                    {{
                        "phase": "string",
                        "tasks": ["string"]
                    }}
                ],
                "concepts_to_learn": ["string"],
                "future_improvements": ["string"]
            }}

            Important:
            - Adapt the number and depth of items to the complexity of the project.
            - Do not artificially limit the response.
            - Keep the recommendations practical and achievable within the specified timeframe.
            - Prioritize the developer's existing technologies and skills.
            - Do not recommend unnecessary technologies.
            - Do not use Markdown.
            - Do not use code fences.
            - Do not add explanations outside the JSON object.
            - Do not add any keys other than the 8 specified top-level keys.
            - Return valid JSON only.
            """
        try:
            response=client.models.generate_content( model="gemini-3.7-flash",contents=prompt,config=types.GenerateContentConfig(response_mime_type="application/json",temperature=0.3))
            data=json.loads(response.text)
            return render_template("plan.html",data=data)
        
        except Exception as e:
            return {"ERROR":str(e)} , 500

    
if __name__=="__main__":
    app.run(debug=True)

 