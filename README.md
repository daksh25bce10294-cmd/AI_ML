# AI_ML
This repository presents a Spam Email Detection System using Machine Learning and Natural Language Processing (NLP). It uses CountVectorizer for feature extraction and the Multinomial Naive Bayes algorithm for classification. The project includes data preprocessing, model training, evaluation, and real-time prediction of user-input messages.



# Spam Email Detection System


## Project Overview

This project is based on developing a **Spam Email Detection System** using Machine Learning techniques. The system classifies emails into **Spam** and **Not Spam** categories using Natural Language Processing (NLP). It helps in filtering unwanted messages and improves communication efficiency.

---

## Objectives

* To build a machine learning model for spam detection
* To preprocess and clean text data
* To convert text into numerical features
* To evaluate model performance using standard metrics

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* CountVectorizer
* Multinomial Naive Bayes

---

## Dataset

The dataset used in this project contains:

* Email Text
* Labels: *Ham (Not Spam)* and *Spam*

---

## Methodology

1. Load dataset using Pandas
2. Remove duplicate data
3. Convert labels into standard format
4. Extract features using CountVectorizer
5. Split dataset into training and testing sets
6. Train model using Multinomial Naive Bayes
7. Evaluate using accuracy and classification report

---

## Implementation

The project is implemented in Python using machine learning libraries. The model is trained on processed data and used to predict whether an email is spam or not. It also allows users to input custom messages for prediction.

---

## Output

* Accuracy Score
* Classification Report (Precision, Recall, F1-score)
* Real-time prediction of user input

---

## How to Run the Project

```bash
# Install required libraries
pip install pandas scikit-learn

# Run the program
python AI_ML.py
```

---

## Results

The model achieves good accuracy in classifying emails and performs efficiently on test data. It shows that Naive Bayes is effective for text classification tasks.

---

## Conclusion

This project demonstrates the practical application of Machine Learning in detecting spam emails. By using text preprocessing, feature extraction, and the Multinomial Naive Bayes algorithm, the system achieves reliable classification results. It highlights how simple models can effectively solve real-world problems and provides a strong foundation for building more advanced email filtering systems in the future.

---

## 👨‍🎓 Author

**Name :** Daksh Amitkumar Gandhi
**Reg. No. : 25BCE10294
**Course :** B.Tech CSE

---

## 📜 License

This project is developed for academic purposes.

---
