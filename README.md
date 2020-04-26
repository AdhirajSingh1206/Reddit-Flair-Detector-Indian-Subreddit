# About Reddit Flair Detector:
This repository demonstrates the project life cycle of a WebApp deployed to predict the Flair of a set of Reddit post in the subReddit r/india from their urls.

This Project can be subdivided into 5 parts:
  1. Data Acquisition from Reddit.
  2. Conducting Exploratory Data Analysis.
  3. Developing the actual Flair Detector using various NLP techniques.
  4. Developing a WebApp with features for automated testing of the above mentioned model.
  5. Deploying this WebApp onto Heroku.
  
The deployed WebApp can be found [https://flair--predictor.herokuapp.com/](https://flair--predictor.herokuapp.com/ "Flair Detector")<br>
And the link for the Automated Testing Endpoint can be found [https://flair--predictor.herokuapp.com/automated_testing](https://flair--predictor.herokuapp.com/automated_testing "Automated Testing Endpoint")

![WebApp](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/WebApp.png )

## Directory Structure:
The description of files and folders can be found below:
1. [Data](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/tree/master/Data) - Contains all types of data( CSV files, Pickled Weight files, h5 weight files etc.)
2. [Jupyter Notebooks](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/tree/master/Jupyter%20notebooks) - Contains the jupyter notebooks for Data Acquisition, EDA, Model selection, Experiment Logs.
3. [WebApp](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/tree/master/Webapp) - Contains all files to deploy the WebApp.  
4. [WebApp Testing](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/tree/master/WebApp%20Testing) - Contains files to test the WebApps Automated_testing feature.
  
## How to reproduce this project:
1. Clone into repository into any folder `git clone https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit.git`
2. Create a virtual environment by the command `virtualenv -p python3 FlairPred`
and Activate it using `source FlairPred/bin/activate`
3. Install all the dependencies using the command `pip3 install -r requirements.txt`
4. Go inside the WebApp folder and enter command `Python3 flask_app.py` to start the local server. It can be found at [http://localhost:5000](http://localhost:5000 "Local Server")

## Project Development:

![.](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/Project_managment.png)

## Code Base 
The entire code has been developed using Python programming language.<br>
Classification models were developed majorly using Sklearn and Tensorflow 2.0.
The WebApp has been developed using Flask web framework and hosted on the Heroku web server.

## Data Aquisition:
The corresponding notebook demonstrates the scraping of data from the r/india subreddit using Praw Module in python.
PRAW which stands for Python Reddit API Wrapper helps us scrape data sceamlessly from any subreddit.

Post scraping the data, we saves the data in a csv file for further processing using Pandas Module.

We further load this raw Data again using Pandas and preform several cleaning and regularisation techniques and save it back into a csv file.

The saved data can be found in the Data folder.

Each Flair has about 230 posts corresponding to it on an average.
Adding upto 2242 posts in total.

## EDA:


## Flair Classification Model: 
Developing the classification model was a 2 phase process:
1. Defining a Base model, which is will be used as a comparison with the more advanced models that we were test. 
2. Develop a more Complex Deep Nural Network based model using Tensorflow 2.0.

### Base Model: 
Evaluated a variety a Linear and Non-linear Models provided by Sklearn like:
* Naive Bayes 
* Linear SVM
* Logestic Regression
* Randomforest
* Multi-layer Perceptron classifier
* XBG Classifier
Further Validation of each model was also done using K-Fold validation as it is best suited for a smaller sized data set.

Linear SVM was found to have the Best weighted accuracy over all the flairs. 

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/BaseModel.png)

We can observe that it produces best results for Food and Policy Flairs at about 88% accuracy.
And produces least accurate results for Photography and Politcs at about 50% accuracy.

### Complex Model:
I initiated the development of this model by vectorizing our training corpus and preprocessing it.
Then i developed serveral iterations of Sequential Models using Tensorflow 2.0

Simultaneously the graph of Training and Validation Accuracy V/S number of Epoch And
The Training and Validation Loss V/S number of Epoch were plotted.
This graphs help us to detect how the model generalizes and to check it there is any overfitting.
Overfitting can be detected whem the Validation Loss curve starts to rise again.

The Various Models that i tested were:
* Simple Sequential Model: This Model could not converge.
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(150,input_dim=input_dim, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model with word embedding and dropout layer: It reached a validation accuracy of 60%
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model with Custom word embedding using GloVe and our own training dat fused: It reached a validation accuracy of 
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, weights=[embedding_matrix],
                              input_length=max_length, trainable=True),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model with Custom word embedding using GloVe and our own training dat fused: It reached a validation accuracy of 
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, weights=[embedding_matrix],
                              input_length=max_length, trainable=True),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Created an RNN using LSTM Model with word embedding: It reached a validation accuracy of
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model a 1D Convolutional layer with word embedding: It reached a validation accuracy of
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Conv1D(128, 13, activation='relu'),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(500, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

Out of All these Models, the 2nd Model has the best results.<br>
This model had Word Embedding coupled along with maxpooling and a 0.5 Dropout layer.
![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/ComplexModel.png)

As we observe that the Validation Loss curve starts rising at about 10 Epochs, this is when the model starts Over-Training. 

## Development of WebApp: 
Flask was used to develop the WebApp.<br>
The development of the WebApp was a 3 step process in which each step had increased complexity and untility:
  1. Development of AppBase.py:<br>
  This script contained the basic initalizations for Flask and only a "Hello World" message was displayed as the   front-end. It was just a static App.
  2. Development of AppTemp.py:<br>
  This script had features which enables it to receive POST requests in form of text or files.
  A more user friendly Front-End was also developed for this script.<br>
  The feature of automated testing was also added to the WebApp.
  3. Development of the final App.py:<br>
  This script finally included the features for scraping the data corresponding to the Link received and then predicting its Flair using the Model file loaded, this result was then Displayed using the front-end.<br>
  The feature of receiveing multiple links at once in a file and then returning their corresponding resulting in a JSON file were also added.
### Unit testing for the WebApp:
This was done at each step by running the WebApp on my local server and then testing using a 3rd party software called POSTMAN which is used to test APIs.

A custom script (Automated_testing.py) was also written to send POST requests to the App. This validated all the functioning of the App.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/automated.png)
<br>
Result of which is:
<br>
![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/automated_testing.png)

## Deployment as a Web Service:
The WebApp was deployed using Heroku which is essentially a PaaS(Platform as a Service).
I preffered uploading the WebApp code on to repository of Heroku directly using its CLI instead of linking Heroku with my Github account as Github limits the size of a certain file to be 100Mb max, this made it impossible to upload the Weight file of more complex models.

Even while uploading directly onto Heroku's Repository, a free account is allowed only a total slug size of 500Mb which is inclusive of all the Libraries. <br>
Due to this fact i was limited to using a rather basic model as compared to some of the more Complex Deep NN NLP techniques that i had implemented which designing and selecting the models.(Tensorflow 2.0 itself uses 380Mb as far as i remember)

Hence i Deployed the model which had been selected as a Baseline Model.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/Deployment.png)

## System Integrated Testing:
Through tested was done after the WebApp was deployed on Heroku.
Edge case testing was done using the Front end of the App.<br>
A development tool called POSTMAN was used to test GET and POST features of both the routines.

A custom script (Automated_testing.py) was also written to send POST requests to the automated testing route, validating its functioning.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/PostMan_testing.png)

The WebApp stands O.K. Tested.
