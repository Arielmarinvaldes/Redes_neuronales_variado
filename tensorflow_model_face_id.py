import tensorflow as tf
from tensorflow.keras import layers, model


# Define las dimensiones de entrada de la imagen
input_shape = (128, 128, 3)

# Crea un modelo de red neuronal convolucional para extraer características de la imagen del rostro
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())

# Agrega una capa completamente conectada para clasificar la identidad del rostro
model.add(layers.Dense(num_classes, activation='softmax'))

# Compila el modelo utilizando una función de pérdida, un optimizador y una métrica
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrena el modelo utilizando los datos preprocesados
model.fit(x_train, y_train, epochs=num_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

# Evalúa el modelo utilizando un conjunto de datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)

# Guarda el modelo entrenado para su uso en el asistente virtual
model.save('reconocimiento_facial.h5')