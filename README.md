# Web-App

# Overview

It seems that most websites today are dynamically generated. Since this is the case, I found it important for me to learn how to work with web servers that generate a full web application. Since they are so widely used, I believe that learning more about creating web applications through useful tools such as, Django or Node.js, will best prepare me for my career in software development. 

To start a test server on my computer, I need to access my __manage.py__ file in the root of my project folder so that I can run the server. To do that, I type into a terminal:

```python
python myproject/manage.py runserver
```
After I hit ENTER, the terminal should bring up a link that looks something like this: __http://127.0.0.1:8000/__ . I open the link by hitting CTRL, and then clicking on the link. The link should take me to a new tab in my primary search engine. Initially, the link will pull up an Error 4040 (Page Not Found), but this is okay because this is not where my project is at. To reach my project, I need to add __my_app__ onto the end of the link in the search bar so that it reads, __http://127.0.0.1:8000/my_app__ . After I hit ENTER, I should see the home page of my web application. 

My purpose for writing this software is to expand my professional software portfolio, and to learn how web applications are generated, with something as simple and fun as a pretend dog rescue. 

[Software Demo Video](https://www.youtube.com/watch?v=7tBij_IXgtI)

# Web Pages

## Home Page

On the home page is a brief welcome message, welcoming the user to the fictional dog rescue, "Homes for Hounds". Below the welcome message, the user will be prompted to choose whether they would like to view a list of dogs that are classified as small, or a list of dogs that are classified as large. Each selection is a link to one of the other two pages in my web app (http://127.0.0.1:8000/my_app/smallDogs for the list of small dogs, and http://127.0.0.1:8000/my_app/largeDogs for the list of large dogs). The content on the homepage is generated from an html template in my project folder.

## Small Dogs Page

The web page for the small dogs contains a list containing each of the small dogs that are available to adopt at the rescue. Each dog has an image, their name listed, and a brief bit of information specifying their breed, gender, and age. Each dog was dynamically generated from a smallDogs database on the server's admin page http://127.0.0.1:8000/admin. At the bottom of the web page, there is a link that takes the user back to the home page.

## Large Dogs Page

The web page for the large dogs contains a list containing each of the large dogs that are available to adopt at the rescue. Like the small dogs, each of the large dogs also have an image, their name, and information specifying their breed, gender, and age. The dogs on the large page were dynamically generated from a largeDogs database on the server's admin page. At the bottom of this web page, there is also a link that takes the user back to the home page. 

# Development Environment

The tool that I used to write and edit the code was VSCode. I used GitHub to upload my code to the internet, and Django to dynamically create my webpages. Lastly, I used the admin page that was provided by the server I created, to add items to my databases.

The programming language I used for this software was python. The libraries I used were libraries that were imported from Django, such as admin, or include, and other general libraries such as os and sys. 

# Useful Websites

* [Codemy.com on YouTube](https://www.youtube.com/watch?v=O5YkEFLXcRg)
* [Official Django site](https://docs.djangoproject.com/en/3.0/contents/)
* [tutorialspoint](https://www.tutorialspoint.com/django/index.htm)

# Future Work

* I could make individual pages for each dog.
* I could add more categories to sort the dogs by, besides just large or small.
* I could always add some more dogs!
