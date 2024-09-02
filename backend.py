from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Define the HTML template with placeholder for text
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Text Output</title>
    </head>
    <body>
        <h1>Welcome to the Text Output Page</h1>
        <p>{{ text }}</p>
    </body>
    </html>
    '''
    
    # Define the text to be output on the webpage
    text = "Hello, this is your text output from the Flask backend!"

    # Render the HTML template with the text
    return render_template_string(html_template, text=text)

if __name__ == '__main__':
    # Run the Flask app on localhost
    app.run(host='127.0.0.1', port=5000, debug=True)
