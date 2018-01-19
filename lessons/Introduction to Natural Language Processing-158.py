## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()

## 3. Tokenizing the Headlines ##

tokenized_headlines = []

for submission in submissions['headline']:
    tokenized_headlines.append( submission.split(" ") )

## 4. Preprocessing Tokens to Increase Accuracy ##

# LOWERCASE AND PUNCTUATION
punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []

for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")  
        tokens.append(token)
    clean_tokenized.append( tokens)

## 5. Assembling a Matrix of Unique Words ##

# CREATE MATRIX WITH PANDAS
# A ROW FOR EACH HN SUBMISSION
# A COLUMN FOR EACH TOKEN APPEARING TWICE OR MORE
import numpy as np
unique_tokens = []
single_tokens = []

for tokens in clean_tokenized:
    for token in tokens:
        if token not in single_tokens:
            single_tokens.append(token)
        elif token in single_tokens and token not in unique_tokens:
            unique_tokens.append(token)
            
counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

print (counts.head())

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for i, item in enumerate(clean_tokenized):
    for token in item:
        if token in unique_tokens:
            counts.iloc[i][token] += 1
            
print(counts.head())

## 7. Removing Columns to Increase Accuracy ##

#REMOVE COLS WITH TOO FEW OR MANY APPERANCES
word_counts = counts.sum(axis=0)
counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]
print(counts.head())

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()

clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

# CALCULATE MEAN SQUARED ERROR
mse = sum((predictions - y_test) ** 2) / len(predictions)