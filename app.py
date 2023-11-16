from flask import Flask,render_template, request, jsonify
import pickle,joblib
import numpy as np

app = Flask(__name__)
#model = pickle.load(open('./model.pkl', 'rb')) 
model = joblib.load(open('./churnmodel.joblib', 'rb'))

@app.route("/")
def predict():
    return render_template("index.html")


@app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        features = [int(x) for x in request.form.values()]
        features = [np.array(features)]
        final = model.predict(features)
        final = round(final[0],0)
        if final == 1:
            finalout ="Customer likely to churn"
        else:
            finalout ="Customer unlikely to churn"
        return render_template("sub.html", fini = finalout)


if __name__ =="__main__":
    app.run() 