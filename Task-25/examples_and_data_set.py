# Task 25

# Convert the text to a stream of character indices
all_ids = ids_from_chars(tf.strings.unicode_split(text, 'UTF-8'))

# Create a TensorFlow dataset from the character indices
ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)

# Example of characters to ids and back
for ids in ids_dataset.take(10):
    print(chars_from_ids(ids).numpy().decode('utf-8'))

# Define sequence length and create sequences
seq_length = 100
sequences = ids_dataset.batch(seq_length + 1, drop_remainder=True)

# Join the tokens back into strings and print some examples
for seq in sequences.take(5):
    print(text_from_ids(seq).numpy())

# Function to split input and target text for the RNN
def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text

# Create the dataset
dataset = sequences.map(split_input_target)

# Print an example of input and target text
for input_example, target_example in dataset.take(1):
    print("Input :", text_from_ids(input_example).numpy())
    print("Target:", text_from_ids(target_example).numpy())
