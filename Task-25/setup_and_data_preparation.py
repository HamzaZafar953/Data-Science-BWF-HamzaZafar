# Task 25

import tensorflow as tf
import numpy as np
import os
import time

# Download the Shakespeare dataset
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# Read the data
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

# Print length of text and the first 250 characters
print(f'Length of text: {len(text)} characters')
print(text[:250])

# Unique characters in the file
vocab = sorted(set(text))
print(f'{len(vocab)} unique characters')

# Vectorize the text
example_texts = ['abcdefg', 'xyz']
chars = tf.strings.unicode_split(example_texts, input_encoding='UTF-8')

# Create the StringLookup layer
ids_from_chars = tf.keras.layers.StringLookup(vocabulary=list(vocab), mask_token=None)
ids = ids_from_chars(chars)

# Invert the representation
chars_from_ids = tf.keras.layers.StringLookup(vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None)

# Function to convert ids to text
def text_from_ids(ids):
    return tf.strings.reduce_join(chars_from_ids(ids), axis=-1)

# Print some examples
tf.strings.reduce_join(chars, axis=-1).numpy()
