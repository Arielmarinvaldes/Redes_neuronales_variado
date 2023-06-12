import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import math

datos, metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)

datos_entrenamiento, datos_prueba = datos['train'], datos['test']

nombres_clases = metadatos.features['label'].names

# Normalizacion de los datos de (0-255 a 0-1)
def normalizar(imagenes, etiquetas):
    imagenes = tf.cast(imagenes, tf.float32)
    imagenes /= 255
    return imagenes, etiquetas

datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_prueba = datos_prueba.map(normalizar)

# Agregar los datos a cache(para usar la memoria en vez de los discos, hace el entrenamiento mas rapido)
datos_entrenamiento = datos_entrenamiento.cache()
datos_prueba = datos_prueba.cache()

# Mostrar imagenes de los datosd e prueba 
for imagen, etiqueta in datos_entrenamiento.take(1):
    break
imagen = imagen.numpy().reshape((28,28))

plt.figure()
plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure(figsize=(10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):
    imagen = imagen.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagen, cmap=plt.cm.binary)
    plt.xlabel(nombres_clases[etiqueta])

plt.show()

# Creacion de red neuronal
modelo = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28,28,1)),
tf.keras.layers.Dense(50, activation='relu'),
tf.keras.layers.Dense(50, activation='relu'),
tf.keras.layers.Dense(10, activation='softmax')]) # Se utiliza [softmax] como funcion de ativacion en las capas de salidasen las neuronas de clasificacion

# Compilar red neuronal
modelo.compile(optimizer='adam', loss = tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])

num_ej_entrenamiento = metadatos.splits["train"].num_examples
num_ej_prueba = metadatos.splits["test"].num_examples

TAMANO_LOTE = 32

datos_entrenamiento = datos_entrenamiento.repeat().shuffle(num_ej_entrenamiento).batch(TAMANO_LOTE)
datos_prueba = datos_prueba.batch(TAMANO_LOTE)

# Entrenar el modelo
historial = modelo.fit(datos_entrenamiento, epochs=5, steps_per_epoch= math.ceil(num_ej_entrenamiento/TAMANO_LOTE))
   
