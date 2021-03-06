# request_postgrad.py
#
# yuetsin, 2018. all rights reserved.

import re
import os
import json
import urllib
import random
import pprint
import requests

from lxml import etree
from time import sleep


def sanit(s):
    return s.replace('\xa0', '').replace('&nbsp', '').strip()


QUICK_MODE = False

USES_PROXY = False

DEBUG = False

proxy_list = []
if USES_PROXY:
    with open("../proxy/proxylist.1", "r") as f:
        proxy_list = f.readlines()


if QUICK_MODE:
    campus_list = [1, 2, 3, 5]
else:
    campus_list = list(range(1, 9))


def parse_leaf(item, params):
    if item.xpath(params) != []:
        return item.xpath(params)[0].text
    else:
        return ""


queryUrl = "http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp"


campuses = ["闵行校区", "徐汇校区", "卢湾校区", "法华校区", "七宝校区", "外地", "上海市精神卫生中心", "临港校区"]

campuses_id = ["Any 校区", "闵行", "徐汇", "卢湾",
               "法华", "七宝", "外地", "上海市精神卫生中心", "临港"]

school_id = ['00000', '01000', '01900', '02000', '03000', '03100', '03200', '03300', '03400', '03500', '03600', '03700', '03900', '05000', '07100', '07200', '08000', '08200', '09000', '09600', '10000', '11000', '12000', '13000', '14000', '15000', '16000', '17000', '18000', '19000', '20000', '21000', '22000', '22100', '23000', '25100', '26000', '27000', '28000', '29000', '29100', '31000', '33000', '34000', '35000',
             '35100', '35200', '36000', '37000', '38000', '39000', '40200', '40400', '41300', '41500', '41600', '41700', '43000', '64000', '65000', '70000', '71000', '71100', '71200', '71900', '72000', '72100', '72200', '72300', '72400', '72500', '72600', '72700', '72800', '72900', '73000', '73100', '73200', '75000', '75100', '75200', '75300', '75400', '75500', '75600', '76000', '78100', '79000', '79100', '79200', '79300', '99999']

han_numbers = ['rua!', '一', '二', '三', '四', '五', '六', '日']

month_tbl = ['pika!', '09', '02', '06']

session = requests.session()

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Host': 'www.yjs.sjtu.edu.cn:81',
    'Origin': 'http://www.yjs.sjtu.edu.cn:81',
    'Referer': 'http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp',
    'Upgrade-Insecure-Requests': '1'
}

session.headers.update(headers)


def query_postgrad_data(start_year, term):
    # start_year = int(input("Input the year when the term started >>> "))
    # term = int(
    #     input("Input the term code (1 = autumn or 2 = spring or 3 = summer >>> "))

    if term != 1:
        start_year += 1

    result_array = []

    for camp in [0]:
        for school in school_id:

            postParams = {'XQDM': str(start_year) + month_tbl[term],
                          'xiaoqu': '',
                          'skyy': '',
                          'YXDM': school,
                          'KCDM': ''
                          }

            print("\n#############\nprepare for: ")
            print(postParams)

            if not USES_PROXY:
                sleep(2)
                # Sleep 2 seconds before call .post

                requestUrl = session.post(queryUrl, data=postParams)

                sleep(2)
                # Sleep 2 seconds before call .get
                #

                query_result = etree.HTML(requestUrl.text)
            else:
                try:
                    proxy = proxy_list[random.randrange(len(proxy_list))]
                    print("proxy:{}".format(proxy))
                    s = requests.Session()
                    proxies = {
                        "http": "http://{}".format(proxy.strip()), "https": "https://{}".format(proxy.strip())
                    }

                    headers = {
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
                        'Host': 'www.yjs.sjtu.edu.cn:81',
                        'Origin': 'http://www.yjs.sjtu.edu.cn:81',
                        'Referer': 'http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp',
                        'Upgrade-Insecure-Requests': '1'
                    }
                    ret = s.post(url=queryUrl, data=postParams,
                                 headers=headers, proxies=proxies, timeout=4)
                    rc = ret.content.decode("utf-8")
                    query_result = etree.HTML(requestUrl.text)
                except:
                    print("proxy %s failed. fallback" % proxy)
                    proxy_list.remove(proxy)
                    sleep(2)
                    # Sleep 2 seconds before call .post

                    requestUrl = session.post(queryUrl, data=postParams)

                    sleep(2)
                    # Sleep 2 seconds before call .get
                    #

                    query_result = etree.HTML(requestUrl.text)

                # print("gotta " + requestUrl.text)
                print("Campus + school has " +
                      str(len(query_result.xpath('//*[@id="table_5"]/tbody/tr'))))

            for item in query_result.xpath('//*[@id="table_5"]/tbody/tr'):
                try:
                    nod = item.xpath('td[1]/div/a')
                    if len(nod) == 0:
                        print("Throw up one piece.")
                        continue

                    code = parse_leaf(item, 'td[1]/div/a')
                    holder_school = parse_leaf(item, 'td[7]/div')
                    name = parse_leaf(
                        item, 'td[2]/div/a').split(code)[0]

                    classname = parse_leaf(
                        item, 'td[2]/div/a').split(code)
                    identifier = classname[1] if len(classname) > 1 else code
                    year = start_year
                    term = term
                    target_grade = 0

                    teacher = [name.text for name in item.xpath('td[6]/div/a')]

                    print("teacher field is: ", teacher)
                    # if DEBUG:
                    #     input()
                    language = parse_leaf(item, 'td[5]/div')
                    credit = float(parse_leaf(item, 'td[4]/div'))

                    notes = "授课语言：" + language + \
                        "。" + parse_leaf(item, 'td[12]/div')
                    student_number = int(parse_leaf(item, 'td[10]/div'))

                    campus = parse_leaf(item, 'td[8]/div')
                    arrangement = parse_leaf(item, 'td[9]/div')

                    general_data = {
                        "identifier": identifier,
                        "code": code,
                        "holder_school": sanit(holder_school)[5:],
                        "name": name,
                        "year": year if term == 1 else (year - 1),
                        "term": term,
                        "target_grade": target_grade,
                        "teacher": teacher,
                        "credit": credit,
                        "student_number": student_number,
                        "notes": sanit(notes)
                    }

                    arrs = arrangement.split(' ')
                    for arr in arrs:
                        odd_even_flag = 0
                        if '(单周)' in arr:
                            arr = arr.replace('(单周)', '')
                            print("Marked 单周. arr = " + arr)
                            odd_even_flag = 1
                        elif '(双周)' in arr:
                            arr = arr.replace('(双周)', '')
                            print("Marked 双周. arr = " + arr)
                            odd_even_flag = 2

                        arr_info = [x for x in re.split(
                            "-|周,星期|第|-|节", arr) if x]
                        if len(arr_info) < 6:
                            # print("Throw up " + arr)
                            # Skip this bad loop
                            continue

                        start_week = int(arr_info[0])
                        end_week = int(arr_info[1])

                        if len(arr_info) >= 7:
                            classroom = arr_info[5] + \
                                '-' + '-'.join(arr_info[6:])
                        else:
                            classroom = arr_info[5]
                        classroom = classroom.replace('教学一楼', '教一楼')

                        sessions = []
                        for i in range(int(arr_info[3]), int(arr_info[4]) + 1):
                            sessions.append(i)

                        new_obj = {}
                        new_obj.update({
                            'week_day': han_numbers.index(arr_info[2]),
                            'sessions': sessions,
                            "campus": sanit(campus),
                            'classroom': sanit(classroom).split('/')[-1].replace(')', '').replace('(', '')
                        })

                        print("获得教室 ", new_obj['classroom'])

                        weeks = []
                        if odd_even_flag == 0:
                            for i in range(start_week, end_week + 1):
                                weeks.append(i)
                        elif odd_even_flag == 1:
                            for i in range(start_week, end_week + 1):
                                if i % 2 == 1:
                                    weeks.append(i)
                        elif odd_even_flag == 2:
                            for i in range(start_week, end_week + 1):
                                if i % 2 == 0:
                                    weeks.append(i)

                        print("convert ", arr, ' => ',
                              weeks, '的', sessions, '节')
                        new_obj.update({
                            "weeks": weeks
                        })
                    general_data.update({
                        "arrangements": [new_obj]
                    })
                    result_array.append(general_data)
                    # print(json.dumps(part, ensure_ascii=False))
                    pprint.pprint(general_data)

                    if DEBUG:
                        input()
                except:
                    input("giving up one")
            print("Finish data grab for %s %s. Now %d counts" %
                  (campuses_id[camp], school, len(result_array)))
    return result_array


if __name__ == '__main__':
    query_postgrad_data(2019, 1)
