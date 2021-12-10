import numpy as np
import math
import pickle
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template')

model=pickle.load(open('Loan2.pkl','rb'))
#model=pickle.load(open("Model.pkl","rb"))

@app.route("/")
def home():
    return (render_template('index.html'))

# def home():
    # return "This is Home"


@app.route('/Predict', methods=["POST"])
def predict():
    if request.method == "POST":
        ag = request.form.values


    int_feature = [x for x in request.form.values()]
# print(request.form.get(values))
    final_feature = [np.array(int_feature)]
    prediction = model.predict(final_feature)
 
# output=round(prediction[0],2)
    return render_template('index.html', prediction_text="Your Insurance Price is {}".format(math.floor(prediction)))


if __name__ == "__main__":
    app.run(debug=True)
