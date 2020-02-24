#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuetsin
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@file: request_undergrad_pysjtu.py
@time: 2020/2/24
'''


# import electsysApi.login as login
# import electsysApi.manip as manip
# import electsysApi.shared as shared
# import electsysApi.modules as modules

import re
import sys
import pysjtu
import getpass

arguments = sys.argv

session = pysjtu.Session()

if len(arguments) > 2:
    print("usage: <%s> optional: <pysjtu session file path>" % arguments[0])
    exit(-1)
elif len(arguments) == 2:
    use_session = True
    session.load(arguments[1])
else:
    use_session = False
    username = input("jAccount ID: >>> ")
    password = getpass.getpass("jAccount Password: >>> ")
    session.login(username=username, password=password)


def sanit(s):
    return s.replace('\xa0', '').replace('&nbsp', '').strip()


MAX_LIMIT = 10000


def query_undergrad_data(start_year, term):
    global session

    client = pysjtu.Client(session=session)

    query = client.query_courses(year=start_year, term=term - 1)
    result_all = []

    for course in query:
        result_all.append({
            "identifier": course.class_name,
            "code": course.course_id,
            "holder_school": course.faculty,
            "name": course.name,
            "year": start_year,
            "term": term,
            "target_grade": 0,
            "teacher": course.teacher,
            "credit": course.credit,
            "notes": '',
            "student_number": course.xlass.students_elected,
            "arrangements": []
        })

    return result_all


if __name__ == '__main__':
    query_undergrad_data(2019, 1)
