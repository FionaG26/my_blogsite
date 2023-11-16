# Blogsite Project

This project is a simple Django-based blogging platform. It allows users to create, view, and manage blog posts.

## Prerequisites

- Python 3.10.12
- [Virtual Environment](https://docs.python.org/3/library/venv.html) (Optional but recommended)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/FionaG26/blogsite.git
    cd blogsite
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Unix systems
    .\myenv\Scripts\Activate  # On Windows
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Visit http://127.0.0.1:8000/ in your web browser to access the blog.

## Project Structure

```
blogsite/
│
├── blogsite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── post_detail.html
│
├── media/
│
├── venv/  (Optional: Virtual Environment)
│
├── manage.py
├── .gitignore
├── requirements.txt
├── README.md
```

## Development Workflow

1. Make changes in `models.py`, create views, templates, and URLs for database schema designing.
2. Run the server and check if it works fine or not.
3. Migrate the changes using:

    ```bash
    python manage.py makemigrations
    ```

4. Apply these migration changes by running:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

6. Start developing your application.

## Version Control

```bash
git init
git add .
git commit -m "Initial Commit"
```

## Deploying to Production

1. Update `ALLOWED_HOSTS` in `blogsite/settings.py` to include your production domain or IP.
2. Collect static files for deployment:

    ```bash
    python manage.py collectstatic
    ```

3. Configure your web server (e.g., Nginx, Apache) to serve the Django application.
4. Set up a production database (e.g., PostgreSQL) and update the database settings in `blogsite/settings.py`.
5. Follow best practices for securing your production environment.

```

### requirements.txt

```
Django==3.2.9
```
