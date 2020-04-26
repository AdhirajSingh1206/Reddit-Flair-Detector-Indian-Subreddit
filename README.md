# About Reddit Flair Detector:
This repository demonstrates the project life-cycle of a WebApp deployed to predict the Flair of a set of Reddit post in the subReddit r/india from their urls.

This Project can be subdivided into 5 parts:
  1. Data Acquisition from Reddit.
  2. Conducting Exploratory Data Analysis.
  3. Developing the actual Flair Detector using various NLP techniques.
  4. Developing a WebApp with features for automated testing of the above mentioned model.
  5. Deploying this WebApp onto Heroku.
  
The <b>deployed WebApp</b> can be found [https://flair--predictor.herokuapp.com/](https://flair--predictor.herokuapp.com/ "Flair Detector")<br>
And the link for the <b>Automated Testing Endpoint</b> can be found [https://flair--predictor.herokuapp.com/automated_testing](https://flair--predictor.herokuapp.com/automated_testing "Automated Testing Endpoint")

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
The entire code has been developed using <b>Python programming language.</b><br>
Classification models were developed majorly using <b>Sklearn and Tensorflow 2.0.</b>
The WebApp has been developed using <b>Flask web framework</b> and hosted on the <b>Heroku web server.</b>

## Data Aquisition:
[Data Aquisition](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Jupyter%20notebooks/Data%20Aquisition.ipynb)

The corresponding notebook demonstrates the scraping of data from the r/india subreddit using <b>Praw Module</b> in python.
PRAW which stands for Python Reddit API Wrapper helps us scrape data sceamlessly from any subreddit.

Post scraping the data, we saves the data in a csv file for further processing using Pandas Module.

We further load this raw Data again using Pandas and preform several <b>cleaning and regularisation</b> techniques and save it back into a csv file.

The saved data can be found in the Data folder.

Each Flair has about 230 posts corresponding to it on an average.
Adding upto <b>2242 posts</b> in total.

## EDA:


## Flair Classification Model: 
Developing the <b>classification model</b> was a 2 phase process:
1. Defining a <b>Base model</b>, which is will be used as a comparison with the more advanced models that we were test. 
2. Develop a more <b>Complex Deep Nural Network based model</b> using Tensorflow 2.0.

### Base Model:
[Best Baseline Model](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Jupyter%20notebooks/Best%20Baseline%20Model%20.ipynb)<br>
[Baseline Model Experiment-log](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Jupyter%20notebooks/Baseline%20Experiment-Log.ipynb)

Evaluated a variety a <b>Linear and Non-linear Models</b> provided by Sklearn like:
* Naive Bayes 
* Linear SVM
* Logestic Regression
* Randomforest
* Multi-layer Perceptron classifier
* XBG Classifier
Further <b>Validation</b> of each model was also done using <b>K-Fold validation</b> as it is best suited for a smaller sized data set.

<b>Linear SVM</b> was found to have the <b>Best weighted accuracy</b> over all the flairs of 67.8%. 

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/BaseModel.png)

We can observe that it produces <b>best results for Food and Policy Flairs</b> at about 88% accuracy.<br>
And produces <b>least accurate results for Photography and Politcs</b> at about 50% accuracy.

This could be due to the fact that the number of posts for there flairs was lesser as compared to the other flairs.

### Complex Model:
[Best Complex Model](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Jupyter%20notebooks/Best%20Complex%20Model.ipynb)

[Complex Model Experiment-log](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Jupyter%20notebooks/Complex%20Model%20Experiment-Log.ipynb)

I initiated the development of this model by <b>vectorizing our training corpus and preprocessing it</b>.
Then I developed serveral iterations of Sequential Models using Tensorflow 2.0

Simultaneously the <b>graph of Training and Validation Accuracy V/S number of Epoch And
The Training and Validation Loss V/S number of Epoch were plotted.</b><br>
These graphs help us to detect how the <b>model generalizes</b> and to check it there is any overfitting.
<b>Overfitting</b> can be detected whem the <b>Validation Loss curve starts to rise again</b>.

The Various Models that i tested were:
* Simple Sequential Model: This Model could <b>not converge</b>.
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(150,input_dim=input_dim, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model with <b>word embedding and dropout layer</b>: It reached a validation accuracy of 64%.
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model with <b>Custom word embedding using GloVe and our own training dat fused</b>: It reached a validation accuracy of 61%.
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
* Created an <b>RNN using LSTM Model with word embedding</b>: It reached a validation accuracy of 55%
```
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
* Sequential Model a <b>1D Convolutional layer with word embedding</b>: It reached a validation accuracy of 62%
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
This model had <b>Word Embedding coupled along with maxpooling and a 0.5 Dropout layer.</b>

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/ComplexModel.png)

As we observe that the <b>Validation Loss curve starts rising at about 10 Epochs</b>, this is when the model starts <b>Over-Training.</b> 

## Development of WebApp:
[WebApp](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/tree/master/Webapp)

Flask was used to develop the WebApp.<br>
The development of the WebApp was a 3 step process in which each step had increased complexity and untility:
  1. Development of <b>Appbase.py:</b><br>
  This script contained the basic initalizations for Flask and only a "Hello World" message was displayed as the   front-end. It was just a static App.
  2. Development of <b>AppTemp.py:</b><br>
  This script had features which enables it to receive POST requests in form of text or files.
  A more user friendly Front-End was also developed for this script.<br>
  The feature of <b>automated testing</b> was also added to the WebApp.
  3. Development of the final <b>App.py:</b><br>
  This script finally included the features for scraping the data corresponding to the Link received and then predicting its Flair using the Model file loaded, this result was then Displayed using the front-end.<br>
  The feature of receiveing multiple links at once in a file and then returning their corresponding resulting in a JSON file were also added.
### Unit testing for the WebApp:
This was done at each step by running the WebApp on my local server and then testing using a development tool called <b>POSTMAN</b> which is used to test APIs.

A <b>custom script (test_Automated_testing.py)</b> was also written to send POST requests to the App. This validated all the functioning of the App.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/automated.png)
<br>
Result of which is:
<br>
![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/automated_testing.png)

## Deployment as a Web Service:
The WebApp was deployed using Heroku which is essentially a PaaS(Platform as a Service).

I preffered uploading the WebApp code on to repository of <b>Heroku directly using its CLI</b> instead of linking Heroku with my Github account as Github limits the size of a certain file to be 100Mb max, this made it impossible to upload the Weight file of more complex models.

Even while uploading directly onto Heroku's Repository, a free account is allowed only a total slug size of 500Mb which is inclusive of all the Libraries. <br>
Due to this fact i was limited to using a rather basic model as compared to some of the more Complex Deep NN NLP techniques that i had implemented which designing and selecting the models.(Tensorflow 2.0 itself uses 380Mb as far as i remember)

Hence i Deployed the model which had been selected as a Baseline Model.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/Deployment.png)

## System Integrated Testing:
[WebApp Testing](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/tree/master/WebApp%20Testing)
Through tested was done after the WebApp was deployed on <b>Heroku.</b>
Edge case testing was done using the Front end of the App.<br>
A development tool called <b>POSTMAN</b> was used to test <b>GET and POST features of both the routines.</b>

A <b>custom script (test_automated_testing.py)</b> was also written to send POST requests to the automated testing route, validating its functioning.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/PostMan_testing.png)

<b>The WebApp stands O.K. Tested.</b>
