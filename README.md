# crop-recommender

This is a crop recommendation system that predicts the best crop to plant in a farm based on the soil parameters.

The `crop_recommender.ipynb` file is the Jupyter notebook for training several machine learning algorithms to perform crop recommendation.
It can be opened using Jupyter Notebook IDE or Visual Studio Code. 
Running the last cells after running previous cells will create the `crop_recommender_model.sav` file.
This file is the machine learning model created from the Random Forest classifier.

The `app.py` file contains code for the Flask web application for the project. The `templates` folder contains the HTML files.
The  `static` folder contains the CSS file and background images.


To run the app locally, you'll have to first clone this repo.
After cloning the repo, open the code using Visual Studio Code or any code editor of your choice.
You will need to create a virtual environment. First, install a `virtualenv`. It is an environment manager in Python. It will let you create virtual environments.
In your terminal, run the code below.

```bash
pip install virtualenv
```

To create a virtual environment `venv`, run the code below in your terminal.

```bash
virtualenv venv
```

After creating the virtual environment, you need to activate it.
To activate the virtual environment on Windows, run the command below.

```bash
venv\Scripts\activate.bat 
```

The `requirements.txt` file contains all the libraries you need to install to run the web application successfully.
In your terminal, run the code below to install all the necessary libraries:

```bash
pip install -r requirements.txt
```

Now you can run the web application locally by running the code below in your terminal:

```bash
python app.py
```

Once the code runs, you'll have to open your web browser and go to the URL shown in your terminal. 
For example, the URL could be `http://127.0.0.1`

