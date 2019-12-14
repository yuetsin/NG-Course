{
    "data": [{
        "identifier": {{[str 型] 历年分配的课程代码，不重复。}},
        "code": {{[str 型] 课程课号}},
        "holder_school": {{[str 型] 开课院系}},
        "name": {{[str 型] 课程名称}},
        "year": {{[int 型] 开课学年，n 代表 n 至 (n + 1) 学年}},
        "term": {{[int 型] 开课学期。1 代表秋季学期，2 代表春季学期，3 代表夏季小学期}},
        "target_grade": {{[int 型] 授课面向的年级。0 代表非特定年级开课}},
        "teacher": {{[list<str> 型] 授课教师。可能有多名}},
        "credit": {{[float 型] 学分。实际操作按 0.5 的倍数取整}},
        "notes": {{[str 型] 备注。或许为空。}},
        "arrangements": [{
            "weeks": {{[list<int> 型] 上课周次}},
            "week_day": {{[int 型] 星期几}},
            "sessions": {{[list<int> 型] 每日授课节次。存在极少的不连续情况}},
            "campus": {{[str 型] 授课校区}},
            "classroom": {{[str 型] 授课地点}}
        }, < ... >]
        "student_number": {{[int 型] 选课学生人数（非实时数据）}}
    }, 
    < ... >
    ]
    "generate_time": {{[str 型] 数据生成时间。yyyy-MM-DD HH:mm:ss}}
}
