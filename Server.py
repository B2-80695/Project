from flask import Flask, request, render_template
import pickle

# Load the model
with open('lg.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    # Read the file contents and send them to the client
    return render_template('index.html')

@app.route("/prediction", methods=["POST"])
def prediction():
    # Get the values entered by the user
    print(request.form)

    # Validate and get form field values
    # Debugging
    print("Form Data:", request.form)
    try:
        max_temp = float(request.form.get("maxtempC"))
        min_temp = float(request.form.get("mintempC"))
        uv_index = float(request.form.get("uvIndex"))
        heat_index = float(request.form.get("HeatIndexC"))
        humidity = float(request.form.get("humidity"))
        pressure = float(request.form.get("pressure"))


        print("Values after conversion:", max_temp, min_temp, uv_index, heat_index, humidity, pressure)

        answers = model.predict([[max_temp, min_temp, uv_index, heat_index, humidity, pressure]])
        print("Model Predictions:", answers)
    except ValueError as e:
        print("ValueError:", e)
        return "Invalid input. Please enter a valid numeric value for the field."

    # Call the model to get predictions
    answers = model.predict([[max_temp, min_temp, uv_index, heat_index, humidity, pressure]])

    # Render the template with the result
    return render_template('index.html', result=answers[0].round())

# This function should be defined outside the prediction route
def perform_prediction(max_temp, min_temp, uv_index, heat_index, humidity, pressure):
    result = f'Predicted result for {max_temp}, {min_temp}, {uv_index}, {heat_index}, {humidity}, {pressure}'
    return result

# Start the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
