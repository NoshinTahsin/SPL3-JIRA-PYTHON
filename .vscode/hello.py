import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
with open('G:/jumble-jira/issue-data-jumble.json') as f:
  data = json.load(f)

num_of_projects=len(data["projects"])
print(num_of_projects)

for i in range(0,num_of_projects):
    print(data["projects"][i]['name'])
    print(len(data["projects"][i]['issues']))
    #print(data["projects"][i]['description'])
    #print(data["projects"][i]['type'])
    #print(data["projects"][i]['components'])

print(data["projects"][0]['issues'][14])

print(data["projects"][0]['issues'][14]['summary'])
print(data["projects"][0]['issues'][14]['assignee'])
print(data["projects"][0]['issues'][14]['description'])

example_sent = data["projects"][0]['issues'][14]['description']

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
