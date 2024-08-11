# Task 21

# Evaluate the model on the test data

loss, acc = network.evaluate(test_images, test_labels, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
