# Libraries below are for Reddit data scraping:
import pickle
import praw
from praw.models import MoreComments

# Libraries below are for Data Cleaning and formatting:
from bs4 import BeautifulSoup
import re
import gensim
from gensim import utils
import gensim.parsing.preprocessing as gsp

# Libraries below are essential for the WebApp: 
from flask import Flask, render_template, request
import json

# Loading the Model file 
model = pickle.load(open('RM.pkl','rb'))

# Establishing connectiong with PRAW API
reddit = praw.Reddit(client_id="ffKcEa2xKfnhyg", client_secret="IJqQkTrDio0xKsKYKYmgeWSoOLM",
                     user_agent="flair_predication", username="ASingh1206",
                     password="g5gh#4$iQFGNBad")

# Utiliy Functions to Fetch, Clean and Normalize Data:
filters = [ gsp.strip_tags, gsp.strip_punctuation, gsp.strip_multiple_whitespaces,
           gsp.strip_numeric, gsp.remove_stopwords, gsp.strip_short, gsp.stem_text ]

def clean_text(text):
    text = text.lower()
    text = utils.to_unicode(text)
    for filter in filters:
        text = filter(text)
    return text

def get_data(link):
    submission = reddit.submission(url = link)
    data = {}
    data["title"] = str(submission.title)
    data["url"] = str(submission.url)
    data["body"] = str(submission.selftext)
      
    submission.comments.replace_more(limit=None)
    comment = ''
    count = 0
    for top_level_comment in submission.comments:
        comment = comment + ' ' + top_level_comment.body
        count+=1
        if(count > 10):
            break
        
    data["comment"] = str(comment)
    data['title'] = clean_text(str(data['title']))
    data['body'] = clean_text(str(data['body']))
    data['comment'] = clean_text(str(data['comment']))    
    combined_features = data["title"] + data["comment"] + data["body"] 
    return combined_features

# Initialzing the App
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html') # Renders the Front End to receive the link.

    if request.method == 'POST':
        link = request.form['link']
        cb_features = get_data(link)    # Function returns the relevent data scrapped and cleaned from Reddit
        result =  model.predict([cb_features])    # Calls the Random Forest Model and returns preddicted Flair
        print(link , result) 
        return render_template('main.html',original_input={'URl of post':link}, result=result)



@app.route('/automated_testing', methods=['GET', 'POST']) # Endpoint for Automated Testing
def automated_testing():    
    if request.method == 'POST':
        file = request.files['upload_file']     # Loades the uploaded file
        links = file.readlines()    # Breaks the text into multiple lines and removes \n
        #print(links)
        json_dict = {}
        for url in links:   # Traversing through the multiple lines in the file
            url = str(url)
            url = url[2:-3] 
            #print(url)
            cb_features = get_data(str(url))    # Function returns the relevent data scrapped and cleaned from Reddit
            result =  str(model.predict([cb_features]))     # Calls the Model and returns preddicted Flair 
            result = result[2:-2]
            #print(result)
            json_dict[url] = result     # Appends the result to a dictionary
        json_dict = json.dumps(json_dict)
        return json.loads(json_dict)    # Returns a json file with all the links and their corresponding Flairs
    
    if request.method == 'GET':
        return "Please send a post request with a text file containing links to r/india."

if __name__ == '__main__':
    app.run(debug = False)