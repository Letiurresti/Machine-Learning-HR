import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Cargar datos desde un archivo CSV
df = pd.read_csv('./Data/processed/data_processed.csv')

# Dividir los datos en características (X) y variable objetivo (y)
X = df.drop('actual_efficacy_h', axis=1)
y = df['actual_efficacy_h']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import pickle

# Crear y entrenar el modelo de Random Forest
modelo_random_forest = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_random_forest.fit(X_train, y_train)

# Guardar el modelo entrenado con pickle
with open('model.pkl', 'wb') as model_file:
    pickle.dump(modelo_random_forest, model_file)
