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
       crop_mapping = {0: 'Apple', 1: 'Banana', 2: 'Blackgram', 3: 'Chickpea',
                       4: 'Coconut', 5: 'Coffee', 6: 'Cotton', 7: 'Grapes',
                       8: 'Jute', 9: 'Kidneybeans', 10: 'Lentil', 11: 'Maize',
                       12: 'Mango', 13: 'Mothbeans', 14: 'Mungbean', 15: 'Muskmelon',
                       16: 'Orange', 17: 'Papaya', 18: 'Pigeonpeas', 19: 'Pomegranate',
                       20: 'Rice', 21: 'Watermelon'}

       # Render the output in new HTML page
       # best_crop_num is a python array
       return render_template('result.html', recommended_crop=crop_mapping.get(best_crop_array[0]))
    # Render the form if it is a GET request   
    return render_template('layout.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
