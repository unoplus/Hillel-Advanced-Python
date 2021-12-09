# FLASK SITE BUSINESS CARD
### In this project I tried to create site business card based on Flask and Bootstrap technologies.
### The site has the following architecture:
* `@app.route('/')` - Main Page. Contains information about Futurama.
  * Function `about()` sends list with information about Futurama.
* `@app.route('/index/')` - index page. Contains some information about Futurama`s lessons.
  * Function `index()` read information about Futurama`s timetable from CSV file and send it to the index page.
* `@app.route('/contact/', methods=['GET', 'POST'])` - contact page. Contains contact form to contact with Futurama.
* Function `contact()` receives messages from users who have visited the site and writes them to a text file.
* `@app.errorhandler(HTTPException)` - custom errors pages.
* Function `http_errors(e)` gives the user 404 and 500 error pages when they occur.
### What can you do for run this all stuff
First download all files. Then reading the "requirements.txt" and install all needed libraries. Execute the command `flask run`. Open your browser, type "http://127.0.0.1:5000" and press the "Enter" button.\
_Good Luck!_ :metal: