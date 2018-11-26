# Given the url https://opentdb.com/api.php?amount=50, use urlopen to fetch its content into a string

from urllib.request import urlopen
import json

import mlab
from data import Quiz
mlab.connect()

url = "https://opentdb.com/api.php?amount=50"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")
# print(type(page_content)) 

content_dict = json.loads(page_content)
# print(content_dict.keys(), content_dict.values())
for i in content_dict.keys(): # 02 keys = response_code , results
    # print(i, content_dict[i], sep=" : ")
    for j in content_dict["results"]: # value = list consisted of dict
        quiz = Quiz(category = j["category"], type1 = j["type"], difficulty = j["difficulty"], question = j["question"], correct_answer = j["correct_answer"], incorrect_answers = j["incorrect_answers"]) # j is a dict #keys = category, type, difficulty, question, correct_answer, incorrect_answers
        quiz.save()