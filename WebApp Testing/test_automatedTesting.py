import requests

url = "https://flair--predictor.herokuapp.com/automated_testing"


files = {'upload_file': open('file.txt','rb')}
r = requests.post(url, files=files)
print(r.text)