from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

# Initialize the Flask app
app = Flask(__name__)

# --- Database Connection ---
# Connect to your local MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db'] # Create a database named 'survey_db'
collection = db['users']   # Create a collection (like a table) named 'users'

# This is the main page of your website
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the user is submitting the form (POST request)
    if request.method == 'POST':
        # Get the data from the form fields
        user_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'age': int(request.form.get('age')),
            'gender': request.form.get('gender'),
            'occupation': request.form.get('occupation'),
            'total_income': float(request.form.get('total_income'))
        }

        # Loop through possible expenses to see which ones were checked
        expense_categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        for category in expense_categories:
            # If the checkbox for an expense is ticked...
            if request.form.get(f'expense_{category}'):
                # ...get the amount from the corresponding text box
                amount = request.form.get(f'amount_{category}', 0)
                user_data[category] = float(amount) if amount else 0

        # Insert the final data dictionary into the MongoDB collection
        collection.insert_one(user_data)

        # Redirect the user to a "Thank You" page
        return redirect(url_for('success'))

    # If the user is just visiting the page (GET request), show them the form
    return render_template('index.html')

# This is the "Thank You" page
@app.route('/success')
def success():
    return render_template('success.html')