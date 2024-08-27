# Task 25

# Training the model
EPOCHS = 20

# Directory to save checkpoints
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

# Train the model
history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
