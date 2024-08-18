# Task 23

# Load the Xception model and set up for classification and localization
base_model = keras.applications.xception.Xception(weights="imagenet", include_top=False)
avg = keras.layers.GlobalAveragePooling2D()(base_model.output)
class_output = keras.layers.Dense(n_classes, activation="softmax")(avg)
loc_output = keras.layers.Dense(4)(avg)

model = keras.models.Model(inputs=base_model.input, outputs=[class_output, loc_output])

# Compile the model with two losses
model.compile(loss=["sparse_categorical_crossentropy", "mse"],
              loss_weights=[0.8, 0.2],
              optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, decay=0.001),
              metrics=["accuracy"])
