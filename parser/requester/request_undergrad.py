#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuetsin
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@file: request_undergrad.py
@time: 2019/9/16
'''
import electsysApi.login as login
import electsysApi.manip as manip
import electsysApi.shared as shared
import electsysApi.modules as modules
import getpass
import re

MAX_LIMIT = 10000

log = login.Login()


def query_undergrad_data(start_year, term):
    username = input("jAccount ID: >>> ")
    password = getpass.getpass("jAccount Password: >>> ")

    log.get_captcha(display=True, on_screen=True)
    captcha = input("Input Captcha: >>> ")

    print("Login Response: ")
    s = log.attempt(username, password, captcha)

    if s == None:
        print("bad response")
        exit(1)

    print("ok (maybe)")

    result = modules.conditional_query(
        s, start_year, term, max_limit=MAX_LIMIT)
    print("result count:", len(result))

    result_all = []

    for course in result:
        try:
            weeks = [x for x in re.split(
                "-|周", course.qsjsz) if x]
            if len(weeks) == 1:
                start_week = int(weeks[0])
                end_week = start_week
            elif len(weeks) == 2:
                start_week = int(weeks[0])
                end_week = int(weeks[1])
            else:
                continue
            result_all.append({
                "identifier": course.jxbmc,
                "holder_school": course.kkxy,
                "name": course.kcmc,
                "year": int(course.xnm),
                "term": int(course.xq),
                "target_grade": int(course.nj),
                "teacher": course.jsxx,
                "teacher_title": course.jszc,
                "credit": course.xf,
                "weeks": []

            })
        except:
            continue
