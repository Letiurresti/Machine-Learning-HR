import streamlit as st
import joblib

# Carga el modelo entrenado
model = joblib.load('model_pipeline.joblib')

st.title("App de Predicción")

# Agregar campos para entrada de datos
sub_age = st.number_input("Edad del Empleado", min_value=0)
sub_sex = st.selectbox("Sexo del Empleado", ["Male", "Female"])
sub_shift = st.number_input("Turno del Empleado", min_value=0)
sub_role = st.selectbox("Rol del Empleado", ["Laborer", "Team Leader", "Shift Manager"])
sub_health_h = st.number_input("Salud", min_value=0.0)
sub_commitment_h = st.number_input("Compromiso", min_value=0.0)
sub_perceptiveness_h = st.number_input("Perceptividad", min_value=0.0)
sub_dexterity_h = st.number_input("Destreza", min_value=0.0)
sub_sociality_h = st.number_input("Socialidad", min_value=0.0)
sub_goodness_h = st.number_input("Benevolencia", min_value=0.0)
sub_strength_h = st.number_input("Fortaleza", min_value=0.0)
sub_openmindedness_h = st.number_input("Mentalidad Abierta", min_value=0.0)
sub_workstyle_h = st.selectbox("Estilo de Trabajo", ["Group A", "Group B", "Group C", "Group D", "Group E"])
event_weekday_name = st.selectbox("Día de la Semana", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

# Botón para realizar la predicción
if st.button("Predecir"):
    # Preparar los datos para la predicción
    input_features = [sub_age, sub_sex, sub_shift, sub_role, sub_health_h, sub_commitment_h, 
                      sub_perceptiveness_h, sub_dexterity_h, sub_sociality_h, sub_goodness_h, 
                      sub_strength_h, sub_openmindedness_h, sub_workstyle_h, event_weekday_name]
    
    # Realizar la predicción usando el modelo
    prediction = model.predict([input_features])
    
    st.write(f"La predicción es: {prediction[0]}")
