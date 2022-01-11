# DisasterResponse

**Introduction**<br>
This work categorizes different disaster cases and predicts the category of disaster based on the type of message received by the system from real individuals. An individual sends a text message of their situation to a system and the system matches the information in the text with a particular type of disaster and communicates the authorities who manage the system. The system is able to make these predictions based on thousands of disaster-related texts collected and stored on the database system of the authorities. These texts are then used to train the prediction model to enable it recognize similar texts and match them with the stored ones and then use them to predict the possible categories of the said disaster. The data used in this work were adapted from Figure Eight. Figure Eight was a technology company that specializes on data science. It uses machine learning and artificial intelligence to label images, speech, texts, audio and video. It was acquired by appen in 2019.

**Python Modules Used**<br>
The python modules used in this work include:<br>
. re <br>
. sys <br>
. pandas <br>
. sqlite3 <br>
. sqlalchemy <br>
. sklearn <br>
. nltk <br>
. pickle <br>
. numpy <br>
. sklearn <br>

**Files and Folders In the Repository**<br>
Below are the various folders and files in the repository:

**data**: This folder contains 4 files namely, disaster_messages.csv, disaster_categories.csv, process_data.py and DisasterResponse.db.

**-disaster_messages.csv**: This is a csv file of differents texts indicating different types of disaster that people face in times of crisis. This includes natural disasters and human-influenced disasters. There are thousands of such messages arranged in a tabular form in this file.

**-disaster_categories.csv**: This file is also a csv file. It contains different headings under which the messages in disaster_messages.csv can be categorized. These categories are also arranged in a tabular form and have the same number of rows as the disaster_messages.csv.

**-process_data.py**: This is a python file where the 2 datasets anove were processed. Here, an ETL pipeline was executed on the datasets - the 2 datasets were merged; the 36 different categories were used to create columns and the number of times each of them featured for each message were entered in their rows; an unwanted column of the merged dataset, called 'original', was dropped and the final clean dataset was saved as a SQLite database file, called DisasterResponse.db.

**-DisasterResponse.db**:


**app folder**: This folder contains all the files used to develop the data dashboard. It primarily contains a python file called run.py and a sub-folder called templates. The templates sub-folder contains two html files namely master.html and go.html.<br>
**-run.py**: 

 

**models folder**: This folder contains all the files used to develop the data and machine learning models of this work. Some of these files are in jupyter notebook while others are the exact replica in pure python format, developed with the Udacity workspace IDE. The jupyter files include ETL_Pipeline_Preparation.ipynb and ML_Pipeline_Preparation.ipynb while the workspace files include process_data.py and run.py.


**README.md**: This very write-up.


**ETL_Pipeline_Preparation.ipynb**: This is a jupyter notebook version of the ETL pipeline preparation program. The first 7 sections present the program in a procedural form while the 8th section presents the program in a modularized form using a class with 3 methods inside. Its dependency files include messages.csv and categories.csv. These are the datasets processed by the program and output as a SQLite database file called disasterMessage.db.

**ML_Pipeline_Preparation.ipynb**: This is another jupyter notebook. It contains the program of the machine learning workflow of this work. It loads the disaster messages, tokenizes them, trains the machine learning model and gives outputs as categories of disaster that match the received messages.

**process_data.py**: This is a python version of the ETL_Pipeline_Preparation.ipynb. It was produced with the Udacity workspace IDE. It contains only the modularized version of the ETL pipeline preparation program and an independent main function that runs the class. Its dependencies are disaster_messages.csv and disaster_categories.csv. These are the datasets processed by the program and output as a SQLite database file called disast.db. The file disaster_messages.csv is exactly the same as messages.csv (mentioned above); disaster_categories.csv is the same as categories.csv while disast.db is the same as disasterMessage.db.

**messages.csv/disaster_messages.csv**: This is a dataset file in csv format which contains the various messages that signify disaster situation.

**categories.csv/disaster_categories.csv**: This is another dataset file in csv format. It shows the various categories of disaster the messages can fall into.

**disasterMessage.db/disast.db**: This is a SQLite database file where the cleaned dataset is saved. It is the output of the ETL pipeline preparation program.



