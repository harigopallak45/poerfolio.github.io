from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

#Database connection details
hostname = '<hostname>'
username = '<username>'
password = '<password>'
database = '<database>'

#Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host=127.0.0.1,
    user=root,
    password=,
    database=
)

# Create a cursor to execute database queries
cursor = conn.cursor()

# Route for the form page
@app.route('/')
def form():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    email = request.form['email']
    message = request.form['Message']

    # Prepare the SQL query to insert the form data into the database
    sql = "INSERT INTO form_data (Name, Email, Message) VALUES (%s, %s, %s)"
    values = (name, email, message)

    # Execute the query
    cursor.execute(sql, values)
    conn.commit()

    return 'Data stored successfully'

# Close the database connection when the app is shut down
@app.teardown_appcontext
def close_connection(exception):
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run()

