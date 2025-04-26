# Nexford-Final-Project-using-Flask-and-Mongodb

## Project structure

Survey APP/


│

├── app.py                 # Flask backend

├── templates/

│   └── form.html          # Frontend HTML form

├── user.py          # Python class for User data processing

├── export_data.csv        # Exported user data (generated)

├── analysis.ipynb         # Jupyter notebook for data visualization

├── requirements.txt       # Python dependencies

└── README.md              # Project documentation


## Project Description
This project is a complete pipeline built to collect, store, process, and visualize survey data regarding income and spending habits, in preparation for the launch of a healthcare product.

Participants submit their age, gender, income, and expenses across various categories. The data is stored securely, processed into CSV format, and visualized to derive business insights.

## 🛠️ Technologies Used
Flask – for creating a simple web form

MongoDB – for storing user survey submissions

Python – for backend processing

Pandas, Matplotlib – for data visualization

Jupyter Notebook – for data exploration

## ✅ Completed Tasks
Web Development with Flask

A simple webpage (form.html) was created.

The form collects:

Age

Gender

Total Income

Expense details (Utilities, Entertainment, School Fees, Shopping, Healthcare).

Expense entries use checkboxes and input fields for amount entry.

## Data Storage with MongoDB

The submitted data is stored in a MongoDB database named survey_db under a collection user_data.

## Data Processing with Python

A User class was created in Python.

The data collected from MongoDB was looped through and saved into a CSV file.

## Data Analysis and Visualization

A Jupyter Notebook (analysis.ipynb) was created.

The CSV file is loaded for analysis.

Two major visualizations were created:

Top Ages with the Highest Income (Bar Chart)

Gender Distribution across Spending Categories (Grouped Bar Chart)

## Export

All charts are prepared for export to be used in a PowerPoint presentation for client reporting.


## Ensure that the form.html file is inside a template folder before executing it

## This app was not succesfully executed on AWS because of the one dollar request from my credit card before i can access the user ID and deploy the app
