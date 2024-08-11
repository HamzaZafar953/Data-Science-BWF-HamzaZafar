# Task 17

# Slicing tensors

slice_1 = train_images[10:100]
print(f'Shape of slice_1: {slice_1.shape}')

slice_2 = train_images[:, 7:-7, 7:-7]
print(f'Shape of slice_2: {slice_2.shape}')
