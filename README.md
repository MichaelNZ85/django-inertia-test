# Django / Inertia / Vite / Vue

This is a boilerplate project for a Django backend serving a Vue frontend using [Inertia.js](https://inertiajs.com/) and Vite. 

Inertia is like "glue" that joins your frontend and backend together. With Inertia, you can serve Vue components right from your backend! (Inertia also works with React and Svelte).

The Inertia website currently only mentions Laravel and React, but they did create [a package for Django](https://github.com/inertiajs/inertia-django), which is what this project uses.

## How to use

1. Clone the project

```git clone git@github.com:MichaelNZ85/django-inertia-vue.git```

2. Install the backend requirements form the requirements.txt file

```pip install -r requirements.txt```
 
3.   install the frontend requirements with NPM

```npm install```

4. Start the backend

```python manage.py runserver```

5. Start the frontend

```npm run dev```

6. Go to http://localhost:8000 in your browser.

### Many thanks to [mercuryseries](https://github.com/mercuryseries) for his help on setting up this project. Here is [his original project](https://github.com/mercuryseries/django-inertia-vue).
