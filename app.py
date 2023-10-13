from flask import Flask, request, render_template
import joblib

# Carga el modelo Random Forest previamente entrenado
model_path = "model.pkl"
model = joblib.load(model_path)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Obtiene los datos de entrada del formulario
        sub_age = float(request.form.get('sub_age'))
        sub_sex = request.form.get('sub_sex')
        sub_shift = int(request.form.get('sub_shift'))
        sub_role = int(request.form.get('sub_role'))
        sub_health_h = float(request.form.get('sub_health_h'))
        sub_commitment_h = float(request.form.get('sub_commitment_h'))
        sub_perceptiveness_h = float(request.form.get('sub_perceptiveness_h'))
        sub_dexterity_h = float(request.form.get('sub_dexterity_h'))
        sub_sociality_h = float(request.form.get('sub_sociality_h'))
        sub_goodness_h = float(request.form.get('sub_goodness_h'))
        sub_strength_h = float(request.form.get('sub_strength_h'))
        sub_openmindedness_h = float(request.form.get('sub_openmindedness_h'))
        sub_workstyle_h = int(request.form.get('sub_workstyle_h'))
        event_weekday_name = int(request.form.get('event_weekday_name'))

        # Realiza la predicción utilizando el modelo
        input_data = [sub_age, sub_sex, sub_shift, sub_role, sub_health_h, sub_commitment_h, sub_perceptiveness_h, sub_dexterity_h,
                      sub_sociality_h, sub_goodness_h, sub_strength_h, sub_openmindedness_h, sub_workstyle_h, event_weekday_name]
        prediction = model.predict([input_data])

        # Muestra la predicción en la plantilla HTML
        return render_template('result.html', prediction=prediction[0])

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template
import joblib

app = Flask(__name)

# Ruta para cargar el formulario HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del formulario
    sub_ID = int(request.form['sub_ID'])
    sub_age = int(request.form['sub_age'])
    sub_sex = request.form['sub_sex']
    sub_shift = int(request.form['sub_shift'])
    sub_role = int(request.form['sub_role'])
    sub_health_h = float(request.form['sub_health_h'])
    sub_commitment_h = float(request.form['sub_commitment_h'])
    sub_perceptiveness_h = float(request.form['sub_perceptiveness_h'])
    sub_dexterity_h = float(request.form['sub_dexterity_h'])
    sub_sociality_h = float(request.form['sub_sociality_h'])
    sub_goodness_h = float(request.form['sub_goodness_h'])
    sub_strength_h = float(request.form['sub_strength_h'])
    sub_openmindedness_h = float(request.form['sub_openmindedness_h'])
    sub_workstyle_h = int(request.form['sub_workstyle_h'])
    event_weekday_name = int(request.form['event_weekday_name'])

    # Cargar el modelo previamente entrenado
    model_path = 'model.pkl'
    model = joblib.load(model_path)

    # Preparar los datos para hacer una predicción
    user_data = [[sub_age, sub_sex, sub_shift, sub_role, sub_health_h, sub_commitment_h,
                  sub_perceptiveness_h, sub_dexterity_h, sub_sociality_h, sub_goodness_h,
                  sub_strength_h, sub_openmindedness_h, sub_workstyle_h, event_weekday_name]]

    # Realizar la predicción
    prediction = model.predict(user_data)

    # Devolver la predicción al usuario
    return f'La predicción es: {prediction[0]}'

if __name__ == '__main__':
    app.run(debug=True)
