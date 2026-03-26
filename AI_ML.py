import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("Ham_spam_dataset.csv")

data.drop_duplicates(inplace=True)
data['Label'] = data['Label'].replace(['Ham', 'Spam'], ['Not Spam', 'Spam'])

messages = data['Email Text']
labels = data['Label']


mess_train, mess_test, cat_train, cat_test = train_test_split(messages, labels)


cv = CountVectorizer(stop_words='english')
features_train = cv.fit_transform(mess_train)
features_test = cv.transform(mess_test)


model = MultinomialNB()
model.fit(features_train, cat_train)

predictions = model.predict(features_test)

print("Accuracy:", accuracy_score(cat_test, predictions))
print("\nClassification Report:\n")
print(classification_report(cat_test, predictions))


def predict(message):
    input_data = cv.transform([message])
    result = model.predict(input_data)
    return result[0]

user_input = input("\nEnter your own message: ")
print("Prediction:", predict(user_input))