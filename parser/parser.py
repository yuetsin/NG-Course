# parser.py
#
# yuetsin 2019. all rights reserved.


from curriculum import *
from utils import *
from requester.request_postgrad import query_postgrad_data
from requester.request_undergrad import query_undergrad_data

import os
import json
import pprint
import datetime


start_year = int(input("Input the year when the term started >>> "))
term = int(input(
    "Input the term code (1 = autumn, 2 = spring, 3 = summer >>> "))


data = {
    'data': [],
    'generate_time': ''
}


current_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.abspath(os.path.join(
    current_path, "../release/%d_%d/%d.json" % (start_year, start_year + 1, term)))

counter = 0
quick_go = False

input("Going to start querying undergrad data. Undergraduates jAccount required. Press enter to continue ...")

for curric in query_undergrad_data(start_year, term):
    counter += 1
    data['data'].append(curric)
    if not quick_go:
        pprint.pprint(curric)
        if input("\n\tpress enter to continue; input s and enter to enable quick-through\n") == 's':
            quick_go = True
    print("#", counter)

quick_go = False

input("Going to start querying postgrad data. Press enter to continue ...")

for curric in query_postgrad_data(start_year, term):
    counter += 1
    data['data'].append(curric)
    if not quick_go:
        pprint.pprint(curric)
        if input("\n\tpress enter to continue; input s and enter to enable quick-through\n") == 's':
            quick_go = True
    print("#", counter)

data['generate_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
json_file.close()
