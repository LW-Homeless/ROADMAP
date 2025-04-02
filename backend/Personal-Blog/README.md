Sample solution for the [Personal Blog](https://roadmap.sh/projects/personal-blog) challenge from [roadmap.sh](https://roadmap.sh)

# Personal Blog
Personal Blog is a project to write and publish articles on various topics. This project will have two sections: a guest section and an admin section.

**Guest section:** A list of pages that can be accessed by anyone. 
- Home page: This page will display the list of articles published on the blog.
- Article page: This page will display the content of the article along with the date of publication.

**Admin section:** are the pages that only you can access to publish, edit, or delete articles.

- Dashboard: This page will display the list of articles published on the blog along with the option to add a new article, edit an existing article, or delete an article.
- Add Article Page: This page will contain a form to add a new article. The form will have fields like title, content, and date of publication.
- Edit Article Page: This page will contain a form to edit an existing article. The form will have fields like title, content, and date of publication.

# Requirements
Python v3.11.3  
Django v5.1.7  
django-ckeditor-5 v0.2.1.7   
pillow v11.1.0  

# Solution
- Programming language: Python 3.11.3.
- Type of programming: object-oriented programming (OOP).
- Design pattern: Model-View-Controller (MVC).

The MVC design pattern has the following structure.
![alt text](https://github.com/LW-Homeless/roadmap/blob/main/backend/Personal-Blog/IMG-README/mvc-django.png)

# How to use
`pip install -r requirements.txt`  
`python3 manage.py runserver 80`

Admin section username and password: (admin:admin)
