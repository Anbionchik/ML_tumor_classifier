from flask import Flask, request, render_template, url_for, flash, redirect
import pandas as pd
import dill
from forms import TumorForm

# Обработчики и запуск Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "7b8abeeece4cec3a07c68f1979c185e426061afbd1b1951dd1702859bc07074cd1d8dbb371ff42cf16e8"

with open('models/lightgbm_pipeline.dill', 'rb') as in_strm:
    model = dill.load(in_strm)
data = pd.read_csv('data/X_test.csv')
threshold = 0.6249811557828746


@app.route("/", methods=['GET'])
def _():
    return redirect(url_for('general'))

@app.route("/home", methods=["GET"])
def general():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def fill_predict():
    form = TumorForm()
    range_limit = data.shape[0]
    if form.validate_on_submit():
        flash(f'Выбран объект № {form.tumor_number.data}.')
        prediction = predict(form.tumor_number.data)
        if prediction:
            flash(f'Злокачественное образование.', 'danger')
        else:
            flash(f'Доброкачественное образование.', 'success')

    return render_template('predict.html', range_limit=range_limit, form=form)


def predict(tumor_number):
    tumor_object = pd.DataFrame(data.iloc[tumor_number - 1]).T
    prediction = model.predict_proba(tumor_object)[:, 1]
    if prediction > threshold:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()

