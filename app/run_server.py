from flask import Flask, request, jsonify, render_template, url_for, flash
import pandas as pd
import dill
from forms import TumorForm

# Обработчики и запуск Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = "7b8abeeece4cec3a07c68f1979c185e426061afbd1b1951dd1702859bc07074cd1d8dbb371ff42cf16e8"

with open('logreg_pipeline.dill', 'rb') as in_strm:
    model = dill.load(in_strm)

# run_with_ngrok(app)  # Start ngrok when app is run
list_for_render = [1, 2, 3, 4, 5]


@app.route("/", methods=["GET"])
def general():
    return render_template('index.html', name=list_for_render)


@app.route('/predict', methods=['GET', 'POST'])
def fill_predict():
    form = TumorForm()
    if form.validate_on_submit():
        flash(f'Выбрано {form.tumor_number.data}', 'success')
    return render_template('predict.html', name=None, form=form)

# @app.post('/predict')
# def predict():
#     data = {"success": False}
#
#     # ensure an image was properly uploaded to our endpoint
#     request_json = request.get_json()
#
#     #     if request_json["description"]:
#     #         description = request_json['description']
#
#     #     if request_json["company_profile"]:
#     #         company_profile = request_json['company_profile']
#
#     #     if request_json["benefits"]:
#     #         benefits = request_json['benefits']
#
#     preds = model.predict_proba(pd.read_json(request_json))
#     data["predictions"] = preds[:, 1][0]
#     #     data["description"] = description
#     # indicate that the request was a success
#     data["success"] = True
#     print('OK')
#
#     # return the data dictionary as a JSON response
#     return jsonify(data)


if __name__ == '__main__':
    app.run()