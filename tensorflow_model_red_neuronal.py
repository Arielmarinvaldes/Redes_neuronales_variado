import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt


"""
Modelo de red neuronal - para calcular (grados_celcius a fahrenheit)
"""
celcius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 91], dtype=float)

# Crea un modelo de red neuronal utilizando TensorFlow
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([oculta1, oculta2, salida])

# Compila el modelo
model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss='mean_squared_error')

# Entrena el modelo
print("Comenzando a entrenar...")
historial = model.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

# Muestra el gráfico de pérdida
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history['loss'])

print("Hagamos una prediccion")
resultado = model.predict([100.0])
print("El resultado es " + str(resultado) + " Fahrenheit!")