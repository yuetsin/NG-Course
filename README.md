# NG-Course

上海交通大学本科生 + 研究生历年课程基本数据集。

![GitHub](https://img.shields.io/github/license/yuetsin/NG-Course.svg)
![GitHub release](https://img.shields.io/github/release/yuetsin/NG-Course.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/yuetsin/NG-Course.svg)

---

## Status

| Data Branch  | Status |
| ------------- | ------------- |
| Master (Default)  | [![Build Status](https://travis-ci.org/yuetsin/NG-Course.svg?branch=master)](https://travis-ci.org/yuetsin/NG-Course)  |
| Beta (Pre-Release)  | [![Build Status](https://travis-ci.org/yuetsin/NG-Course.svg?branch=be-ta)](https://travis-ci.org/yuetsin/NG-Course)  |
| Develop | [![Build Status](https://travis-ci.org/yuetsin/NG-Course.svg?branch=dev)](https://travis-ci.org/yuetsin/NG-Course)  |

## 自己 Dump 数据

### 依赖

``` shell
pip[3] install -r requirements.txt
```
### 设定 Proxy（可选）

1. 如无需启用代理来 dump 研究生课程数据，可将 `/NG-Course/parser/requester/request_postgrad.py` 中第 23 行修改为：
``` python3
Line 23:    USES_PROXY = False
```
2. 如需启用代理，则确保上述 `.py` 文件配置为
``` python3
Line 23:    USES_PROXY = True
```
并在 `/NG-Course/proxy/proxylist.1` 中填入 HTTP 代理 ip:port（一行一个）并保存。

> Info: 建议使用中国大陆 IP 代理来提高速度。

3. 运行 `/NG-Course/parser/parser.py` 脚本来开始。
> Warning: ⚠️ 需要输入一个有效关联到本科生的 jAccount 账户来同步。登录信息不会被代理。

## JSON 地址

### 2019 至 2020 学年

* 秋季学期 `https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2019_2020_1.json`


### 2018 至 2019 学年

* 秋季学期 `https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2018_2019_1.json`

* 春季学期 `https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2018_2019_2.json`

* 夏季学期 `https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2018_2019_3.json`

## 数据包括

- [x] 课程名称、课号

- [x] 授课教师、开课院系

- [x] 行课时间安排

- [x] 授课教室

- [x] 选课人数（非实时）

## 数据**不**包括

- [ ] 授课内容介绍

- [ ] 先修课程依赖

- [ ] 课件及任何学习资料

## 数据结构

[查看数据存储结构（JSON 样例）](https://github.com/yuetsin/NG-Course/blob/master/struct/structure.jsonnet)

## 数据来源

* 本科课程来自 [`electsysq` 查询接口](http://electsysq.sjtu.edu.cn/ReportServer/Pages/ReportViewer.aspx?%2fExamArrange%2fLessonArrangeForOthers&rs:Command=Render) 和 [教学信息服务网](http://i.sjtu.edu.cn/)

> 版权所有 © 1999 - 2019 上海交通大学网络信息中心 上海交通大学教务处 沪交ICP 备 05005

* 研究生课程来自 [课表查询接口](http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp)

> 版权所有 © 2019 上海交通大学研究生院 沪交ICP 备 50534

## 已知问题

- [ ] 不包含上海交通大学医学院课程数据。

- [ ] 2017 年秋季学期门牌号改动之后，新旧教室不对应。

- [ ] 研究生课程教师无职称信息。

## 数据分布

### 闵行校区
上院、中院、下院、东上院、东中院、东下院、木兰楼、陈瑞球楼、杨咏曼楼

### 徐汇校区
徐汇中院、教一楼、新上院、工程馆

 > 由于数据源质量问题，以下校区教室信息不完善，仅供参考
### 卢湾校区
### 法华（长宁）校区
### 七宝校区
### 临港校区
### SMHC（上海市精神卫生中心）
