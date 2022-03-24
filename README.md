# group8

Lab #4 - Flask & Data Science
Web development is divided into two aspects, frontend development and backend development. Frontend development is creating the parts of the website that a user will interact with and ensuring that everything looks nice. Backend development is working with an underlying programming language to run the application and interact with any
databases. Frontend development is normally done using HTML, CSS, and Javascript while backend development is normally done using Python, C#, or Java.
For this lab you’ll be using HTML, CSS and Javascript for the website frontend and the Flask Python library for the website backend.

HTML
HTML stands for Hyper Text Markup Language, its purpose is to tell a web browser what content goes where.
Resources for help with HTML can be found here:
● https://htmlcheatsheet.com/
● FreeCodeCamp.com
● https://web.stanford.edu/group/csp/cs21/htmlcheatsheet.pdf

CSS
CSS is what adds styles (colors, borders, text sizing) to a website
● https://htmlcheatsheet.com/css/

Javascript
Javascript is what’ll generate the data visualization (Chart.JS) and adds interactivity to a website
● https://www.codecademy.com/learn/introduction-to-javascript
● https://www.learn-js.org/

Flask
Flask is a web application library for Python with many optional libraries that give it additional
functionality. Flask is commonly referred to as a microframework because of how extensible it is,
which also makes it great for quick development.
Flask Resources:
● Official Flask Documentation
● Flask Mega Tutorial
● Corey Schaffer’s Flask Tutorial Series


Lab Assignment
For this assignment, you’ll be working as a group to create a website that displays
visualizations about various data sets.

Requirements
One Flask-based website that meets the following requirements:
● One Database with Two Tables:
1. Users Table - User ID, Account Type, User Name, Password Hash, email, Date
Created, & Last Login
2. DataSets - Data Set Name, Data Set File
● One Content Page
1. Displays visualizations using Chart.JS based on selected datasets
2. Allows users to select a data set to visualize
3. Allows users to log out
● One Login Page
1. Allows users to login
2. Allows new users to create an account
● One Admin Page
1. Allows Administrators to remove data sets & ban users
2. Non admin users can’t access this page
● Secure coding practices should be considered and used for all aspects of the application.
StandardUser Cyber Security
100 N Locust St #2
Denton, TX 76201
Optional Requirements
● Allow users to upload custom data sets on the content page
● Allow users to comment on specific visualizations
○ Store these comments in their own table on the database
● Add a user profile page
○ Requires its own database table & links to the users table
○ Should display all of the user’s posts in chronological order
○ Users can customize basic content on the page
■ Username
■ Profile Description
■ Background Image
■ Profile Image