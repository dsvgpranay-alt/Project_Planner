# DevPath — AI-Augmented Project Planner

![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Mermaid](https://img.shields.io/badge/Mermaid-FF3670?style=flat-square&logo=mermaid&logoColor=white)

DevPath is a Flask-based web application that uses the Google Gemini API to transform a project idea into a structured development plan.

Describe your idea, and DevPath generates a practical roadmap to help you move from concept to implementation.

## Features

- 💡 Enter and describe a project idea
- 🤖 Generate a structured project plan using Gemini
- 📝 Dynamically display AI-generated results
- 🎨 Responsive interface using Bootstrap
- 🔄 Server-side rendering with Jinja2
- 📊 Generate project diagrams using Mermaid
- 🔐 Secure API key configuration using environment variables

## Tech Stack

- **Python**
- **Flask**
- **Jinja2**
- **Google Gemini API**
- **HTML**
- **CSS**
- **Bootstrap**
- **Mermaid**

## How It Works

```text
User enters project idea
        ↓
HTML form sends POST request
        ↓
Flask receives the input
        ↓
Prompt is constructed
        ↓
Gemini API generates the project plan
        ↓
Flask receives the response
        ↓
Jinja2 renders the result
        ↓
Generated plan is displayed
```
## Project Structure
```text
DevPath/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── nav_image.png
│
└── templates/
    ├── index.html
    └── plan.html
```
## Future Improvements

- Add user authentication
- Save and manage generated project plans
- Add technology and difficulty preferences
- Allow users to customize generated plans
- Export project plans as PDF
- Add project progress tracking
- Improve input validation and error handling
