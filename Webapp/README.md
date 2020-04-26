# WebApp Development:
Flask was used to develop the WebApp.<br>
The development of the WebApp was a 3 step process in which each step had increased complexity and untility:
  1. Development of AppBase.py:<br>
  This script contained the basic initalizations for Flask and only a "Hello World" message was displayed as the   front-end. It was just a static App.
  2. Development of AppTemp.py:
  This script had features which enables it to receive POST requests in form of text or files.
  A more user friendly Front-End was also developed for this script.<br>
  The feature of automated testing was also added to the WebApp.
  3. Development of the final App.py:
  This script finally included the features for scraping the data corresponding to the Link received and then predicting its Flair using the Model file loaded, this result was then Displayed using the front-end.<br>
  The feature of receiveing multiple links at once in a file and then returning their corresponding resulting in a JSON file were also added.

Template Folder contains all the html files.


### Unit testing for the WebApp:
This was done at each step by running the WebApp on my local server and then testing using a Development tool called POSTMAN which is used to test APIs.

A custom script (Automated_testing.py) was also written to send POST requests to the App. This validated all the functioning of the App.

![](https://github.com/AdhirajSingh1206/Reddit-Flair-Detector-Indian-Subreddit/blob/master/Readme-Images/PostMan_testing.png)
