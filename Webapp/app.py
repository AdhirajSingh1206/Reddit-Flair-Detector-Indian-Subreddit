import pickle
import praw
from praw.models import MoreComments

from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
import gensim
nltk.download('stopwords')

from flask import Flask, render_template, request
import json

app = Flask(__name__, template_folder='templates')

model = pickle.load(open('RM.pkl','rb'))

reddit = praw.Reddit(client_id="ffKcEa2xKfnhyg", client_secret="IJqQkTrDio0xKsKYKYmgeWSoOLM",
                     user_agent="flair_predication", username="ASingh1206",
                     password="g5gh#4$iQFGNBad")


replace_by_space = re.compile('[/(){}\[\]\|@,;]')
replace_symbol = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower() # lowercase text
    text = replace_by_space.sub(' ', text) # replace certain symbols by space in text
    text = replace_symbol.sub('', text) # delete symbols from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove STOPWORDS from text
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

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')

    if request.method == 'POST':
        link = request.form['link']
        cb_features = get_data(link)
        result =  model.predict([cb_features])
        print(link , result) 
        return render_template('main.html',original_input={'URl of post':link}, result=result)

@app.route('/automated_testing', methods=['GET', 'POST'])
def automated_testing():    
    if request.method == 'POST':
        file = request.files['upload_file'] 
        #content = str(file.read())
        links = file.readlines()
        #print(links)
        json_dict = {}
        for url in links:
            url = str(url)
            url = url[2:-3]
            print(url)
            cb_features = get_data(str(url))
            result =  str(model.predict([cb_features]))
            result = result[2:-2]
            print(result)
            json_dict[url] = result
        json_dict = json.dumps(json_dict)
        return json.loads(json_dict)
    
    if request.method == 'GET':
        return "Please send a post request with a text file containing links to r/india."

if __name__ == '__main__':
    app.run(debug = True)