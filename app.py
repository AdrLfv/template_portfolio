from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Project data
projects = [
    {
        'id': 1,
        'title': 'Project 1',
        'description': 'Description of project 1',
        'image': 'project1.jpg',
        'long_description': 'Detailed description of project 1 including technologies, challenges, and solutions.',
        'technologies': ['Python', 'Flask', 'JavaScript'],
        'github_link': 'https://github.com/AdrienLefevre/project1',
        'live_demo': 'https://project1.example.com',
    },
    {
        'id': 2,
        'title': 'Project 2',
        'description': 'Description of project 2',
        'image': 'project2.jpg',
        'long_description': 'Detailed description of project 2 including technologies, challenges, and solutions.',
        'technologies': ['React', 'Node.js', 'MongoDB'],
        'github_link': 'https://github.com/AdrienLefevre/project2',
        'live_demo': 'https://project2.example.com',
    },
    {
        'id': 3,
        'title': 'Project 3',
        'description': 'Description of project 3',
        'image': 'project3.jpg',
        'long_description': 'Detailed description of project 3 including technologies, challenges, and solutions.',
        'technologies': ['Vue.js', 'Express', 'PostgreSQL'],
        'github_link': 'https://github.com/AdrienLefevre/project3',
        'live_demo': 'https://project3.example.com',
    },
    {
        'id': 4,
        'title': 'Project 4',
        'description': 'Description of project 4',
        'image': 'project4.jpg',
        'long_description': 'Detailed description of project 4 including technologies, challenges, and solutions.',
        'technologies': ['Angular', 'Django', 'SQLite'],
        'github_link': 'https://github.com/AdrienLefevre/project4',
        'live_demo': 'https://project4.example.com',
    },
    {
        'id': 5,
        'title': 'Project 5',
        'description': 'Description of project 5',
        'image': 'project5.jpg',
        'long_description': 'Detailed description of project 5 including technologies, challenges, and solutions.',
        'technologies': ['TypeScript', 'NestJS', 'MySQL'],
        'github_link': 'https://github.com/AdrienLefevre/project5',
        'live_demo': 'https://project5.example.com',
    },
    {
        'id': 6,
        'title': 'Project 6',
        'description': 'Description of project 6',
        'image': 'project6.jpg',
        'long_description': 'Detailed description of project 6 including technologies, challenges, and solutions.',
        'technologies': ['PHP', 'Laravel', 'MySQL'],
        'github_link': 'https://github.com/AdrienLefevre/project6',
        'live_demo': 'https://project6.example.com',
    },
]

# Context processor to make current year available in all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Routes
@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project/<int:project_id>')
def project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project.html', project=project)
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
