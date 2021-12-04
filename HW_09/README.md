# FLASK FIRST STEPS
### In this project I tried to create some basics site based on Flask technology.
### The site has the following architecture:
* `@app.route('/')` - Main Page. Contains information about web-site.
  * Function `main()` sends some list to main page.
* `@app.route('/requirements/')` - requirements page. Contains my "requirements.txt".
  * Function `requirements():` reads data from file "requirements.txt" and generates a list, which is then passed to page "requirements"
* `@app.route('/generate-users/<int:number>')` - user-info page. Contains some full names and emails.
  * Function `generate_users(number)` accepts a default number or a user-supplied number. Generates multiple fake full names and email addresses. The number of fake records is equal to the received number.
* `@app.route('/mean/')` - mean page. Contains some information calculated from CSV file/
  * Function `mean()` reads data from file "hw05.csv". Calculates "average_height" in inches, "average_weight" in pounds and count how many rows contains CSV file. Then transfer "average_height" in cm and transfer "average_weight" in kg. Then sends this information to the "mean" web page.
* `@app.route('/space/')` - space page. Contains information about how many astronauts in space right now.
  * Function `space()` using api "http://api.open-notify.org/astros.json" gets information about astronauts in space. Then, from the received data, it selects only the quantity and sends this quantity to the "space" web page.
* `@app.route('/base58encode/<string:string>')` - base58encode page. Contains some string which encode by using base58 algorithm.
  * Function `base58encode(string):` accepts a default string or a user-supplied string and encoded to base58 algorithm.
* `@app.route('/base58decode/<string:string_in_base58>')` - base58decode page. Contains some string which decode by using base58 algorithm.
  * Function `base58decode(string_in_base58):` accepts a default string or a user-supplied string and decoded to base58 algorithm.
### What can you do for run this all stuff
First download all files. Then reading the "requirements.txt" and install all needed libraries. Execute the command `flask run`. Open your browser, type "http://127.0.0.1:5000" and press the "Enter" button.\
_Good Luck!_ :metal: