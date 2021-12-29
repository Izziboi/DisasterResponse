# DisasterResponse

**Introduction**<br>
This work categorizes different disasters cases and gives suggestions on the category of disaster based on the type of message received by the system from real individuals. An individual sends a text message of their situation to a system and the system matches the information in the text with a particular type of disaster and communicates the authorities who manage the system

**Python Modules Used**<br>
The python modules used in this work include:<br>
. sys <br>
. pandas <br>
. sqlite3 <br>
. sqlalchemy <br>
. sklearn <br>

**Files In the Repository**<br>
Below are the various folders and files in the repository:

**app folder**: This folder contains all the files used to develop the data dashboard. These files include

**models folder**: This folder contains all the files used to develop the data and machine learning models of this work. Some of these files are in jupyter notebook while others are the exact replica in pure python format, developed with the Udacity workspace IDE. The jupyter files include ETL_Pipeline_Preparation.ipynb and ML_Pipeline_Preparation.ipynb while the workspace files include process_data.py and run.py.


**README.md**: This very write-up.


**ETL_Pipeline_Preparation.ipynb**: This is a jupyter notebook version of the ETL pipeline preparation program. The first 7 sections present the program in a procedural form while the 8th section presents the program in a modularized form using a class with 3 methods inside. Its dependency files include messages.csv and categories.csv. These are the datasets processed by the program and output as a SQLite database file called disasterMessage.db.

**ML_Pipeline_Preparation.ipynb**: This is another jupyter notebook. It contains the program of the machine learning workflow of this work. It loads the disaster messages, tokenizes them, trains the machine learning model and gives outputs as categories of disaster that match the received messages.

**process_data.py**: This is a python version of the ETL_Pipeline_Preparation.ipynb. It was produced with the Udacity workspace IDE. It contains only the modularized version of the ETL pipeline preparation program and an independent main function that runs the class. Its dependencies are disaster_messages.csv and disaster_categories.csv. These are the datasets processed by the program and output as a SQLite database file called disast.db. The file disaster_messages.csv is exactly the same as messages.csv (mentioned above); disaster_categories.csv is the same as categories.csv while disast.db is the same as disasterMessage.db.

**messages.csv/disaster_messages.csv**: This is a dataset file in csv format which contains the various messages that signify disaster situation.

**categories.csv/disaster_categories.csv**: This is another dataset file in csv format. It shows the various categories of disaster the messages can fall into.

**disasterMessage.db/disast.db**: This is a SQLite database file where the cleaned dataset is saved. It is the output of the ETL pipeline preparation program.



