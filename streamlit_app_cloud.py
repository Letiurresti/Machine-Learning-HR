import streamlit as st
import joblib

# Cargar el modelo entrenado
model = joblib.load('model_str.pkl')

# Crear un menú de navegación en la barra lateral
menu = st.sidebar.radio("Menú de Navegación", ("Inicio", "Predicción"))

if menu == "Inicio":
    st.title("Bienvenidx a la Predicción del Rendimiento")
    st.markdown("La Transformación Digital ha llegado a Recursos Humanos.")

    st.markdown("Esta aplicación te permite predecir el rendimiento de los empleados en función de varios factores, como la edad, el sexo, el rol, el compromiso, la mentalidad abierta, el estilo de trabajo y el día de la semana.")
elif menu == "Predicción":
    st.title("Predicción del Rendimiento")

    # Agregar campos para entrada de datos
    sub_age = st.number_input("Edad del Empleado", min_value=18)

    sub_sex_mapping = {'Male': 1, 'Female': 0}
    sub_sex = st.selectbox("Sexo del Empleado", list(sub_sex_mapping.keys()))
    sub_sex_encoded = sub_sex_mapping.get(sub_sex)

    sub_role_mapping = {'Laborer': 1, 'Team Leader': 2, 'Shift Manager': 3}
    sub_role = st.selectbox("Rol del Empleado", list(sub_role_mapping.keys()))
    sub_role_encoded = sub_role_mapping.get(sub_role)

    sub_commitment_h = st.number_input("Compromiso", min_value=0.0, max_value=1.0)
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
        input_features = [sub_age, sub_sex_encoded, sub_role_encoded, sub_commitment_h,
                          sub_openmindedness_h, sub_workstyle_h_encoded, event_weekday_encoded]

        # Realizar la predicción usando el modelo
        prediction = model.predict([input_features])

        st.write(f"El rendimiento será de: {prediction[0]}")
