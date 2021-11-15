from flask import Flask, render_template
import numpy as np
import pickle
from form import SoilParameters


filename = 'crop_recommender_model.sav'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)
app.config["SECRET_KEY"] = '571eujdfashlwehfshdafkuolih'

@app.route('/', methods=['GET', 'POST'])
def home():
    # pass the wtf form to the html template
    form = SoilParameters()
    if form.validate_on_submit():
       nitrogen = form.nitrogen.data
       phosphorous = form.phosphorous.data
       potassium = form.potassium.data
       temperature = form.temperature.data
       humidity = form.humidity.data
       pH = form.pH.data
       rainfall = form.rainfall.data

       # Get the output from the classification model
       data = np.array([[nitrogen, phosphorous, potassium, temperature, humidity, pH, rainfall]])
       best_crop_array = model.predict(data)
       print(best_crop_array)


       # dictionary containing the crop mapping
       crop_mapping = {0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea',
                       4: 'coconut', 5: 'coffee', 6: 'cotton', 7: 'grapes',
                       8: 'jute', 9: 'kidneybeans', 10: 'lentil', 11: 'maize',
                       12: 'mango', 13: 'mothbeans', 14: 'mungbean', 15: 'muskmelon',
                       16: 'orange', 17: 'papaya', 18: 'pigeonpeas', 19: 'pomegranate',
                       20: 'rice', 21: 'watermelon'}

       # Render the output in new HTML page
       # best_crop_num is a python array
       return render_template('result.html', recommended_crop=crop_mapping.get(best_crop_array[0]))
    # Render the form if it is a GET request   
    return render_template('layout.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
