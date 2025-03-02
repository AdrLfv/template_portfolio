# Template Portfolio

A personal portfolio website built with Flask showcasing your projects and professional information.

## Features

- Dark mode design
- Responsive layout optimized for all devices
- Project showcase with preview images/GIFs
- Dedicated project detail pages
- "About Me" section
- Downloadable CV
- Contact information

## Project Structure

```
template_portfolio/
├── app.py              # Main Flask application
├── static/             # Static assets (CSS, JS, images)
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Website images and project previews
├── templates/          # HTML templates
│   ├── base.html       # Base template with common elements
│   ├── index.html      # Main portfolio page
│   ├── about.html      # About Me page
│   ├── cv.html         # CV page
│   ├── contact.html    # Contact page
│   └── project.html    # Project detail page template
└── requirements.txt    # Python dependencies
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python app.py
   ```
6. Access the website at `http://localhost:5000`

## Adding Projects

To add a new project:
1. Add project images to `static/images/projects/`
2. Update the projects data in `app.py`

## Customization

The site can be customized by:
- Editing the template files in `/templates`
- Modifying the CSS in `/static/css`
- Updating personal information in `app.py`
