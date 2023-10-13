import streamlit as st
import joblib

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

st.title("App de Predicción")

# Agregar campos para entrada de datos
sub_ID = st.number_input("ID del Empleado", min_value=98000001, max_value=98000789)
sub_age = st.number_input("Edad del Empleado", min_value=18)

sub_sex_mapping = {'Male': 1, 'Female': 0}
sub_sex = st.selectbox("Sexo del Empleado", list(sub_sex_mapping.keys()))
sub_sex_encoded = sub_sex_mapping.get(sub_sex)

sub_shift = st.number_input("Turno del Empleado", min_value=1, max_value=3)

sub_role_mapping = {'Laborer': 1, 'Team Leader': 2, 'Shift Manager': 3}
sub_role = st.selectbox("Rol del Empleado", list(sub_role_mapping.keys()))
sub_role_encoded = sub_role_mapping.get(sub_role)

sub_health_h = st.number_input("Salud", min_value=0.0, max_value=1.0)
sub_commitment_h = st.number_input("Compromiso", min_value=0.0, max_value=1.0)
sub_perceptiveness_h = st.number_input("Perceptividad", min_value=0.0, max_value=1.0)
sub_dexterity_h = st.number_input("Destreza", min_value=0.0, max_value=1.0)
sub_sociality_h = st.number_input("Socialidad", min_value=0.0, max_value=1.0)
sub_goodness_h = st.number_input("Benevolencia", min_value=0.0, max_value=1.0)
sub_strength_h = st.number_input("Fortaleza", min_value=0.0, max_value=1.0)
sub_openmindedness_h = st.number_input("Mentalidad Abierta", min_value=0.0, max_value=1.0)

sub_workstyle_h_mapping = {'Group A': 1, 'Group B': 2, 'Group C': 3, 'Group D': 4, 'Group E': 5}
sub_workstyle_h = st.selectbox("Estilo de Trabajo", list(sub_workstyle_h_mapping.keys()))
sub_workstyle_h_encoded = sub_workstyle_h_mapping.get(sub_workstyle_h)

event_weekday_mapping = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
event_weekday_name = st.selectbox("Día de la Semana", list(event_weekday_mapping.keys()))
event_weekday_encoded = event_weekday_mapping.get(event_weekday_name)


# Botón para realizar la predicción
if st.button("Predecir"):
    # Preparar los datos para la predicción
    input_features = [sub_ID, sub_age, sub_sex_encoded, sub_shift, sub_role_encoded, sub_health_h, sub_commitment_h, 
                      sub_perceptiveness_h, sub_dexterity_h, sub_sociality_h, sub_goodness_h, 
                      sub_strength_h, sub_openmindedness_h, sub_workstyle_h_encoded, event_weekday_encoded]

    # Realizar la predicción usando el modelo
    prediction = model.predict([input_features])
    
    st.write(f"La predicción es: {prediction[0]}")
