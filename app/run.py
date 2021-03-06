import json
import plotly
import pickle
import pandas as pd
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine
from sklearn.base import BaseEstimator, TransformerMixin


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


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///data/DisasterResponse.db')
df = pd.read_sql_table('dtable', engine)

# load model
model = joblib.load("models/classifier.pkl")
# with open('models/classifier.pkl', 'rb') as f:
#     model = pickle.load(f)

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    # Maximum values in each category
    
    categ_names = list(df.columns[4:])
    max_values = list(df.iloc[:,4:].max().values) # Maximum values in each category
    
    
    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        
        
        {
            'data': [
                Bar(
                    x=categ_names,
                    y=max_values,
                    orientation = 'v',
                )
            ],
           
            'layout': {
                'title': 'Maximum Values of Categories',
                'yaxis': {
                    'title': "Value"
                },
                'xaxis': {
                    'title': "Category"
                    
                },
            }
        },
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))
    
    
    cat_names = list(classification_results.keys())
    cat_values = list(classification_results.values())
    
    for val in range(len(cat_names)):
        if cat_values[val] >= 1:
            graphs = [
                {
                    'data': [
                        Bar(
                            x=cat_names,
                            y=cat_values,
                            orientation = 'v',
                        )
                    ],

                    'layout': {
                        'title': 'Predicted Categories',
                        'yaxis': {
                            'title': "Category Value"
                        },
                        'xaxis': {
                            'title': "Category Name"
                        }
                    }
                },
            ]
        else:
            pass
         
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # This will render the go.html Please see that file. 
    return render_template('go.html', query=query, classification_result=classification_results,
                          ids=ids, graphJSON=graphJSON)
    
    
def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()