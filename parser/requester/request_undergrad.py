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
            try:
                notes = course.xkbz
                print("extra notes: ", notes)
            except:
                notes = ""

            arrangements = []

            classrooms = course.jxdd.split(';')

            arrangement_strs = course.sksj.split(';')

            print("classrooms: ", classrooms)
            if len(classrooms) == 0:
                classrooms = ['教室未定']
            print("len(classroom) and len(arrangements): ",
                  len(classrooms), len(arrangement_strs))
            for arrangement in arrangement_strs:
                actual_weeks = []
                phases = [x for x in re.split(
                    "第|{|}", arrangement) if x]

                weekday = phases[0]
                # like 星期一
                print("weekday: (like 星期一) ", weekday)

                weekday_num = ['星期期', '星期一', '星期二', '星期三',
                               '星期四', '星期五', '星期六', '星期日']

                session = phases[1]
                # like 1-2节
                print("session: like 1-2节 ", session)

                weeks = phases[2]
                # like 3周,9周
                print("weeks: like 3周,9周 ", weeks)

                for weeksp in weeks.split(','):
                    weeks = [x for x in re.split(
                        "-|周", weeksp.replace('(单)', '').replace('(双)', '')) if x]
                    print("len of weeks: ", len(weeks))
                    if len(weeks) == 1:
                        actual_weeks.append(int(weeks[0]))
                    elif len(weeks) == 2:
                        if '(单)' in weeksp:
                            oddEvenType = 0
                        elif '(双)' in weeksp:
                            oddEvenType = 1
                        else:
                            oddEvenType = 2
                        start_week = int(weeks[0])
                        end_week = int(weeks[1])
                        for i in range(start_week, end_week + 1):
                            if oddEvenType == 0 and i % 2 == 0:
                                continue
                            if oddEvenType == 1 and i % 2 == 1:
                                continue
                            actual_weeks.append(i)
                    else:
                        print("unresolvable week arr.: ", course.qsjsz)
                        input()
                        continue

                actual_jcs = []
                for daysp in session.split(','):
                    jcs = [x for x in re.split(
                        "-|节", daysp) if x]
                    if len(jcs) == 1:
                        actual_jcs.append(int(jcs[0]))
                    elif len(jcs) == 2:
                        start_jc = int(jcs[0])
                        end_jc = int(jcs[1])
                        for i in range(start_jc, end_jc + 1):
                            actual_jcs.append(i)
                    else:
                        print("unresolvable day arr.: ", course.skjc)
                        input()
                        continue
                try:
                    classroom = classrooms[arrangement_strs.index(arrangement)]
                except:
                    classroom = classrooms[-1]
                arrangements.append({
                    "weeks": actual_weeks,
                    "week_day": weekday_num.index(weekday),
                    "sessions": actual_jcs,
                    "campus": course.xqmc,
                    "classroom": classroom if classroom != '' else '教室未定'
                })

            result_all.append({
                "identifier": course.jxbmc,
                "code": course.kch,
                "holder_school": course.kkxy,
                "name": course.kcmc,
                "year": int(course.xnm),
                "term": int(course.xq),
                "target_grade": int(course.nj) if course.nj.isdigit() else 0,
                "teacher": course.jsxx.split(','),
                "credit": course.xf,
                "notes": notes,
                "student_number": course.xkrs,
                "arrangements": arrangements
            })
            print("course: ", course.kcmc, "\nweek: ",
                  course.qsjsz, " => ", actual_weeks)
            # input()
        except e:
            print(
                "giving up one, due to critical mismatch. press enter to continue, or control + c to terminate")
            input()
            continue
    return result_all


if __name__ == '__main__':
    query_undergrad_data(2019, 1)
