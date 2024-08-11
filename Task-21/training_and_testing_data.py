# Task 21

print("Training data")
print(f"- X = {train_images.shape}, y = {train_labels.shape}")
print(f"- Holds {train_images.shape[0] / 70000 * 100:.2f}% of the overall data")

print("\n")

print("Testing data")
print(f"- X = {test_images.shape}, y = {test_labels.shape}")
print(f"- Holds {test_images.shape[0] / 70000 * 100:.2f}% of the overall data")
