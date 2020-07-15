<img src="https://github.com/yuetsin/NG-Course/blob/master/misc/title.png?raw=true" width="300" alt="NG-Course" />

![Travis (.org)](https://img.shields.io/travis/yuetsin/NG-Course?label=travis%20ci)
[![Actions Status](https://github.com/yuetsin/NG-Course/workflows/build/badge.svg)](https://github.com/yuetsin/NG-Course/actions)
![GitHub](https://img.shields.io/github/license/yuetsin/NG-Course.svg?style=flat-square)
![GitHub release](https://img.shields.io/github/release/yuetsin/NG-Course.svg?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/yuetsin/NG-Course.svg?style=flat-square)
[![About Mine](https://img.shields.io/badge/see-mine-inactive.svg?style=flat-square)](https://github.com/yuetsin/curricula)

上海交通大学本科生 + 研究生历年课程基本数据集。

[数据样例（JSON）](https://github.com/yuetsin/NG-Course/blob/master/struct/structure.jsonnet) [Demo](https://yuetsin.github.io/index.html)

## JSON Link

### 2019 至 2020 学年

[秋季学期](https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2019_2020_1.json)、[春季学期](https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2019_2020_2.json)

### 2018 至 2019 学年

[秋季学期](https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2018_2019_1.json)、[春季学期](https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2018_2019_2.json)、[夏季学期](https://raw.githubusercontent.com/yuetsin/NG-Course/master/release/2018_2019_3.json)

### 测试数据

[10 则](https://raw.githubusercontent.com/yuetsin/NG-Course/master/example/10.json)、[100 则](https://raw.githubusercontent.com/yuetsin/NG-Course/master/example/100.json)、[1000 则](https://raw.githubusercontent.com/yuetsin/NG-Course/master/example/1000.json)

## Dump 数据

### 安装依赖

``` shell
pip[3] install -r requirements.txt
```

### 开始
运行 `/NG-Course/parser/parser.py` 脚本来开始。
> ⚠️ 需要输入一个有效关联到本科生的 jAccount 账户来同步。登录请求不会被代理。

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

- [ ] 医学院课程数据

## 数据来源

* 本科课程来自 [`electsysq` 查询接口](http://electsysq.sjtu.edu.cn/ReportServer/Pages/ReportViewer.aspx?%2fExamArrange%2fLessonArrangeForOthers&rs:Command=Render) 和 [教学信息服务网](http://i.sjtu.edu.cn/)

> 版权所有 © 1999 - 2019 上海交通大学网络信息中心 上海交通大学教务处 沪交ICP 备 05005

* 研究生课程来自 [课表查询接口](http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp)

> 版权所有 © 2019 上海交通大学研究生院 沪交ICP 备 50534
