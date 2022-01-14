# DisasterResponse

**Introduction**<br>
This work categorizes different disaster cases and predicts the category of disaster based on the type of message received by the system from real individuals. An individual sends a text message of their situation to a system and the system matches the information in the text with a particular type of disaster and communicates the authorities who manage the system. The system is able to make these predictions based on thousands of disaster-related texts collected and stored on the database system of the authorities. These texts are then used to train the prediction model to enable it recognize similar texts and match them with the stored ones and then use them to predict the possible categories of the said disaster. The data used in this work were adapted from Figure Eight. Figure Eight was a technology company that specializes on data science. It uses machine learning and artificial intelligence to label images, speech, texts, audio and video. It was acquired by appen in 2019.

**Python Modules Used**<br>
The python modules used in this work include:<br>
- re <br>
- sys <br>
- pandas <br>
- sqlite3 <br>
- sqlalchemy <br>
- sklearn <br>
- nltk <br>
- pickle <br>
- numpy <br>
- sklearn <br>
- json <br>
- plotly <br>
- flask <br>

**Files and Folders In the Repository**<br>
Below are the various folders and files in the repository:

**data**: This folder contains 4 files namely, disaster_messages.csv, disaster_categories.csv, process_data.py and DisasterResponse.db.

**-disaster_messages.csv**: This is a csv file of differents texts indicating different types of disaster that people face in times of crisis. This includes natural disasters and human-influenced disasters. There are thousands of such messages arranged in a tabular form in this file.

**-disaster_categories.csv**: This file is also a csv file. It contains different headings under which the messages in disaster_messages.csv can be categorized. These categories are also arranged in a tabular form and have the same number of rows as the disaster_messages.csv.

**-process_data.py**: This is a python file where the 2 datasets anove were processed. Here, an ETL pipeline was executed on the datasets - the 2 datasets were merged; the 36 different categories were used to create columns and the number of times each of them featured for each message were entered in their rows; an unwanted column of the merged dataset, called 'original', was dropped and the final clean dataset was saved as a SQLite database file, called DisasterResponse.db.

**-DisasterResponse.db**: This is the cleaned dataset which would be used to build the model of this work. It contains the messages, the message genres, the disaster categories and again, 36 columns, each of which is a disaster category. These 36 columns serve as categorical columns for the original 36 different disaster categories.

**models folder**: This folder contains the files used to develop the machine learning models of this work. They include train_classifier.py and classifier.pkl.zip.

**-train_classifier.py**: This file performs 2 basic tasks - preparing the messages to be suitable for machine learning application and using the prepared messages to predict the possible category of disaster it represents. To achieve this, it tokenizes and lemmatizes the messages using the Natural Language Toolkit module. It builds the model, applying grid search. The trained model then predicts the disaster category. The sklearn's machine learning algorithms played vital roles here. In order to possibly make predictions from multiple columns (36 columns) the MultiOutputClassifier class of the sklearn was applied. Furthermore, it saves the model as a pickle file for subsequent use.

**-classifier.pkl.zip**: This is the pickle file of the trained model arising from the train_classifier.py file. It is in zip format to compress it enough to the level that Github would accept it.

**app folder**: This folder contains all the files used to develop the data dashboard. It primarily contains a python file called run.py and a sub-folder called templates. The templates sub-folder contains two html files namely, master.html and go.html.

**-run.py**: This file contains the python codes that make the data at the backend too be available at the frontend. It uses the flask module to communicate with the html files at the frontend, while it uses the plotly module to plot graph. The graph in this case is a bar chart showing the 3 genres in the dataset and the number of times each of them featured.

**-master.html**: This is the home page of the visualization dashboard. It provides a text field for a message to be entered and a classification button to be clicked for the system to categorize the message. Below this field is the initial visualization which is a bar chart of the 3 genres with their individual number of features.

**-go.html**: When a message is entered on the message field on the dashboard homepage and the classification button is clicked, the 36 disaster categories enlist below, taking over the position of the prior bar chart. The categories that are predicted to align with the entered message are shaded with light green colour, while the ones that are not predicted remain unshaded. This effects come from the go.html file. It inherits the attributes of the master.html file and then replaces the bar chart with the list of the dasaster categories.

**How To Run The Program**<br>
It would be imperative to first mention that this work was done on Udacity Workspace IDE. This IDE is Linux-based; so if you are using a Windows- or Mac-based IDE or code editor, the structure or mode of operation may not be the same.
- To run the ETL pipeline program, remember that it is located in the data folder. Open a terminal and type: python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db.<br>
- The machine learning pipeline program is located in the models folder. To run that, open a terminal and type: python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl.<br>
- Then to run the web app program to display results, access the app folder by typing the following on the terminal: python app/run.py. By this time, the web app would be running and served on port 3001. Open another terminal and type: env | grep WORK. It would return two variables (WORKSPACEDOMAIN=udacity-student-workspaces.com and WORKSPACEID, in my own case, it was view6914b2f4, yours may be different). Now open a new web browser tab and on the address bar, type: https://view6914b2f4-3001.udacity-student-workspaces.com (this is my own web address, please use yours). You would then see the home page of the web app.<br>
- Now insert any disaster message and click the 'Classify Message' and the prediction result would appear. 

**Result**<br>
- On the homepage, are 2 bar charts:<br>
- The first shows the different genres in the dataset and the number of times each of them featured (see figure below).<br>

![pic1](https://user-images.githubusercontent.com/44449730/149242374-5d2949e6-db3a-4110-9411-d2df04d6898b.jpg)<br>
- The second shows the different categories and the maximum value of each (see figure below).<br>

![pic2](https://user-images.githubusercontent.com/44449730/149242742-faa2f9ab-2f34-4285-b238-c785df63c2f3.jpg)<br>

- When a text is inserted into the text field on the home page and 'Classify Message' button is clicked, the prediction result appears. On this page, there are also 2 visualizations:<br>
- The first shows all the categories, shading the predicted ones with light green color. So the unshaded ones are not part of the prediction (see figure below).<br>

![pic3](https://user-images.githubusercontent.com/44449730/149242849-dde8e9ae-cafd-48c9-ae09-5f1392cdd701.jpg)

- The second shows the predicted categories in a bar chart. The height of each bar is the maximum value of the category. The unpredicted categories do not have any bar (see figure below).<br>

![pic4](https://user-images.githubusercontent.com/44449730/149243005-ebbe32b3-771e-43b2-9fa7-1d6a4f8170c6.jpg)


**Summary**<br>
The above arrangement of the files follows the procedure followed in actualizing this project. The work flowed from ETL pipeline preparation, through machine learning pipeline preparation to data visualization. This work successfully manipulates human texts and uses them to make predictions. However, more work can still be done on the project, especially on the visualization area but due to time constraint, it is left at this level for now. Contributions are therefore welcome from interested persons who wish to add suitable features to the work, to make it more competitive.

**Conclusion**<br>
A machine learning model was therefore developed following the procedure stated above. It is worthy to mention that the grid search parameters of the machine learning pipeline were very few. This was because it was taking a lot of time to train the model. Choosing more parameters means taking more time to process the codes. It took about 32 minutes to train the model in this case and that was somewhat uneconomical. For practice purposes, more parameters could be chosen to see their efffects on the entire system and the results as well.

**Acknowledgement**<br>
From the buttom of my heart, I appreciate the Udacity Mentors for their immense help to me during the execution of this project. Without their support, possibly I could not have got this far. I say a big thank you to them. I also thank Figure Eight for providing us with the datasets used to carry out this project. Furthermore, more gratitude goes to the authors of the online materials I consulted to enable me solve some of the challenges I encountered in the course of the project. Some of them are Mosh Hamedani, the authors of pandas and sklearn. Thanks also to google, for providing the search engine, through which the materials I used were accessed. Please accept my gratitude.

**References**<br>
1. https://classroom.udacity.com/nanodegrees/nd025/parts/34d62b5a-f380-4223-85dd-7c195994d028/modules/f7c70326-948b-4f97-b368-bec2ac9ad4ba/lessons/706456a2-8784-4961-a40f-f5607769aa43/concepts/21f7a292-ea41-4c96-9121-c38eb4fdaeef
2. https://ianlondon.github.io/blog/pickling-basics/ 
3. https://codewithmosh.com/courses/417695/lectures/9219316
4. https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html#min-tut-10-text
5. https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html
6. https://datatofish.com/replace-values-pandas-dataframe/
7. https://github.com/Katba-Caroline/Disaster_Response_Message_Classification_Pipelines/blob/master/app/run.py
8. https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github
