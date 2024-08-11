# Task 21

# Fit the model

batch_size = 256
n_epochs = 15
val_split = 0.2

# Train the model

history = network.fit(train_images, train_labels, validation_split=val_split,
                      epochs=n_epochs, batch_size=batch_size)

# Plotting training and validation accuracy

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
