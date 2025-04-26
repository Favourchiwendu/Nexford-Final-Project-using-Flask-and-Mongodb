from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (local or cloud)
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["user_data"]

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']

    # Handle expense categories
    categories = request.form.getlist('categories')
    expenses = {}
    for category in categories:
        amount = request.form.get(category)
        if amount:
            expenses[category] = float(amount)

    user_data = {
        "age": int(age),
        "gender": gender,
        "income": float(income),
        "expenses": expenses
    }

    collection.insert_one(user_data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
