# app.py
from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        client_id = request.form.get('client_id')
        email = request.form.get('email')
        if client_id and email:
            # Check if email is valid
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return 'Error: Invalid email format'
            return 'Form submitted successfully'
    return render_template_string('''
        <style>
            body { background-color: #fafafa; font-family: Arial, sans-serif; }
            form { border: 1px solid #ccc; padding: 20px; margin: 0 auto; width: 300px; }
            input[type="text"] { width: 100%; padding: 10px; margin-bottom: 10px; }
            input[type="submit"] { width: 100%; padding: 10px; background-color: #007BFF; color: white; border: none; }
            input[type="submit"]:hover { background-color: #0056b3; }
        </style>
        <form method="POST">
            Client ID: <input type="text" name="client_id" placeholder="Enter Client ID"><br>
            Email: <input type="text" name="email" placeholder="Enter Email"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True,port =5000, host='0.0.0.0')