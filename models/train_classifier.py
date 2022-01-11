# Import libraries

import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

# Import more libraries
import sys
import re
import pickle
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

from sklearn.base import BaseEstimator, TransformerMixin

# Database and pickle file paths
DisasterResponse = 'sqlite:///data/DisasterResponse.db'
classifier = 'classifier.pkl'

class StartingVerbExtractor(BaseEstimator, TransformerMixin):
    '''
    This class is a starting verb extractor. It uses the tokenize function to attempt 
    extracting verbs starting with different tags.

    INPUT: It takes the sklearn's BaseEstimator and TransformerMixin as its input parameters.

    OUTPUT: 1 or 0, depending on the tags in the tokenized text.
    '''
    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return 1
        return 0

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)


def tokenize(phrase):
    '''
    This function tokenizes and lemmatizes texts - it converts texts to lower-case word tokens,
    removes punctuations and stop words, and normalizes verbs to their primary forms.
    
    INPUT: Normal texts
    
    OUTPUT: list: A list of tokenized strings.
    '''
    
    token = word_tokenize(phrase)
    lemmatize = WordNetLemmatizer()

    tidytoken = []
    for t in token:
        newtoken = lemmatize.lemmatize(t).lower().strip()
        tidytoken.append(newtoken)

    return tidytoken


def load_data(database_filepath):
    '''
    This function loads the cleaned database file from the ETL pipeline
    and extracts some useful columns for subsequent use.
    
    INPUT: .db file: The disaster response database file from the ETL pipeline
    
    OUTPUT: A bundle of the following:
    1. X: array-like: The values of the message column in an array-like format.
    2. y: array-like: The values of the 36 category columns in an array-like format.
    3. categorynames: list: A list of the names of the 36 category columns
    '''
    engine = create_engine(DisasterResponse)
    df = pd.read_sql("SELECT * FROM dtable", engine)
    X = df.message.values
    y = df.drop(columns=['id', 'message', 'genre', 'categories'], axis=1).values
    categorynames = list(df.columns[4:,])
    
    return X, y, categorynames


def build_model():
    '''
    This function builds the model of this machine learning pipeline. 
    It prepares the pipeline, tunes the model with some parameters,
    and finally carries out a grid search on the feature parameters.
    
    INPUT: No input parameter
    
    OUTPUT: dict: Returns a dictionary of the best parameters of the model.
    '''
    
    # Pipeline using feature union to simultaneously run the 
    # transformers and the classifiers.
    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)), 
                ('tfidf', TfidfTransformer())])), 
            ('starting_verb', StartingVerbExtractor())])), 
        ('clf', MultiOutputClassifier(RandomForestClassifier(
            n_estimators=10, random_state=1, n_jobs=2)))])
    
    # Parameter tunning
    parameters = {
        'features__text_pipeline__vect__ngram_range': ((1, 1), (1, 2)), 
        'clf__estimator__min_samples_split': [2, 3, 4], 
        'features__transformer_weights': (
            {'text_pipeline': 1, 'starting_verb': 0.5},)}
    
    print(pipeline.get_params().keys())
    
    # Grid search implementation
    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=3)
    return cv
    

def evaluate_model(model, X_test, Y_test, category_names):
    
    '''
    This function carries out the prediction and some result
    calculations for the model and prints them out.
    
    INPUT:
    1. obj: The build_model() object.
    2. array-like: X_test.
    3. array-like: Y_test.
    4. list: A list of the names of the categories columns.
    
    OUTPUT:
    Prints out the following:
    1. The categories column names.
    2. The classification report, featuring precision, recall, f1-score and support.
    3. Accuracy score
    4. Best parameters
    '''
    predicts = model.predict(X_test)
    for i in range(len(category_names)):
        print('\nCategory: {} '.format(category_names[i]))
        print(classification_report(Y_test[:, i], predicts[:, i]))
        print('Accuracy:', (predicts[:, i] == Y_test[:, i]).mean())
        print("Best Parameters:", model.best_params_)


def save_model(model, model_filepath):
    '''
    This function generates a pickle file for the model
    and also saves it with a given pickle file name.
    
    INPUT:
    1. obj: The build_model() object.
    2. str: A file path for the pickle file.
    
    OUTPUT:
    Returns a pickled file and saves it in the pickle file name
    provided on the pickle file path.
    '''
    return pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        DisasterResponse, classifier = sys.argv[1:]
        print('\nLoading data...\n    DATABASE: {}'.format(DisasterResponse))
        X, Y, category_names = load_data(DisasterResponse)
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.2, random_state=1)
        
        print('\nBuilding model...')
        model = build_model()
        
        print('\nTraining model...')
        model.fit(X_train, Y_train)
        
        print('\nEvaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('\nSaving model...\n    MODEL: {}'.format(classifier))
        save_model(model, classifier)

        print('\nTrained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
    