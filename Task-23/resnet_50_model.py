# Task 23

from tensorflow.keras.applications import resnet50

model = resnet50.ResNet50(weights="imagenet")

# Assuming 'images' is a batch of images you want to process
images_resized = tf.image.resize(images, [224, 224])
inputs = resnet50.preprocess_input(images_resized * 255)
Y_proba = model.predict(inputs)

# Decoding predictions
top_K = resnet50.decode_predictions(Y_proba, top=3)
for image_index in range(len(images)):
    print(f"Image #{image_index}")
    for class_id, name, y_proba in top_K[image_index]:
        print(f" {class_id} - {name:12s} {y_proba * 100:.2f}%")
    print()
