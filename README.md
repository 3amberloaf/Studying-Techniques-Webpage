# Studying Techniques

This is a simple webpage design that was initially created to help improve my coding skills. There are no classes to 'teach' someone how to study, but it is a skill everyone will build upon the rest of their lives. Learning how to optimize time and efficieny handle complex topics is key to long-term success. 

# Skills Used

* Docker
* Python
* Bootsrap
* Javascript
* HTML/CSS
* Jinja

# Flask Route

Creating a Flask route allows Flask to execute a specific function at a specified URL.

1. Create a Python file and import the necessary modules

```
    from flask import Flask
    app = Flask(__name__)
```

2. Create a route using the path root of the application, `app` is a common example of a root name. 

```
    @app.route('/')
    def study():
        return 'I enjoy eating cake as I study'
```

3. You can also utilize HTTP methods ['GET', 'POST'] in the flask route to give more details on the data. 
    - GET is helpful in retrieved or reading information. In our casem accessing a web page
    - POST is best in submitting changes, such as updating the registration form in our homepage. 
    - If using both methods, remember to import `request` from Flask 

```
    @app.route('/', methods=['GET', 'POST'])
```

4.  Run the flask application.

```
    if __name__ == '__main__':
        app.run(debug=True)
```

# Update CSS 

1. Update CSS to customize templates but have CSS extend from base.html so it applied to all pages
```
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

# Improvements to be made

1. Add more timer functions
2. Add sound effects
3. Make the menu bar a drop down
4. add pop up messages for encouoragement

# Hide the minutes input once timer began

1. Added an identificator to the input field in the html file
```
<div id="countdown" class="timer-display">00:00</div>
```

2. Update the startTimer() and stopTimer() functions so they hide it once it starts

```
function startTimer() {
    let durationInput = document.getElementById('duration');
    durationInput.style.display = 'none'; // Hide the input field
}
```