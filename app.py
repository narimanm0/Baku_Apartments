from flask import Flask, render_template, request
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # Get values from form
    data = {
        'Location': request.form['location'],
        'Area': float(request.form['area']),
        'Number_of_rooms': int(request.form['rooms']),
        'Frontage': int(request.form['frontage']),
        'Mortgage': int(request.form['mortgage']),
        'Condition': int(request.form['condition']),
        'Current_floor': int(request.form['current_floor']),
        'Total_floors': int(request.form['total_floors'])
    }

    # Create DataFrame with correct column names
    input_df = pd.DataFrame([data])

    # Predict
    pred = model.predict(input_df)

    return render_template("index.html", prediction=round(pred[0], 2))

if __name__ == "__main__":
    app.run(port=3000, debug = True)