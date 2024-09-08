# Business Project : Predicting the Stock News Headlines 

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

# Reading the CSV file from the specified location
df=pd.read_csv(r'C:\Users\Lenovo\Downloads/Data.csv',encoding='ISO-8859-1')

# Display the first 5 rows of the dataset to verify successful loading
print(df.head())

# Splitting the data into training and test sets
train = df[df['Date'] < '20150101']
test = df[df['Date'] > '20141231']

# Extract headline columns (Top1 to Top25) for the training set
data = train.iloc[:, 2:27]

# Rename columns for ease of access
list1 = [str(i) for i in range(25)]
data.columns = list1

# Convert headlines to lower case and remove punctuations
for index in list1:
    data[index] = data[index].str.lower().replace(to_replace=r"[^a-zA-Z]", value=" ", regex=True)

# Display the DataFrame to check the results
print(data.head())

# Create a list of all headlines for each row
headlines = []
for row in range(len(data)):
    headlines.append(' '.join([str(i) for i in data.iloc[row, 0:25]]))
    
# Display the first few entries in the headlines list to verify
print(headlines[:5])

# Implement Bag of Words
cv = CountVectorizer(ngram_range=(2, 2))  # Using bigrams
traindata_x = cv.fit_transform(headlines)

# Implement RandomForest Classifier
randomclassifier = RandomForestClassifier(n_estimators=200, criterion='entropy')
randomclassifier.fit(traindata_x, train['Label'])  # Assuming `train['Label']` is your target variable

# Transform the test data
test_transform = []
for row in range(len(test)):
    test_transform.append(' '.join([str(x) for x in test.iloc[row, 2:27]]))
    
test_data = cv.transform(test_transform)
predictions = randomclassifier.predict(test_data)
predictions

# Plot the Confusion Matrix
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues, labels=["positive", "negative"]):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(labels))
    plt.xticks(tick_marks, labels, rotation=45)
    plt.yticks(tick_marks, labels)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
# Compute confusion matrix
cm = metrics.confusion_matrix(test['Label'], predictions)  # Assuming `test['Label']` contains the true labels
print(cm)
plot_confusion_matrix(cm)
plt.show()

# Displaying the DataFrame in HTML format (if using Jupyter Notebook)
display(pd.DataFrame(data).head(1))  # Display the first row of the DataFrame in HTML format

from sklearn.metrics import classification_report,accuracy_score

accuracy_score(test['Label'],predictions)

report=classification_report(test['Label'],predictions)
print(report)
