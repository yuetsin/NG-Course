{
	"data": [{
        // [str 型] 历年分配的课程代码，不重复。
		"identifier": "005-(2017-2018-2)OC901(教学班)",

		// [str 型] 课程课号
		"code": "OC901",

        // [str 型] 开课院系
		"holder_school": "船舶海洋与建筑工程学院",

        // [str 型] 课程名称
		"name": "海洋学导论",

        // [int 型] 开课学年，n 代表 n 至 (n + 1) 学年
		"year": 2017,

        // [int 型] 开课学期。1 代表秋季学期，2 代表春季学期，3 代表夏季小学期
		"term": 3,

        // [int 型] 授课面向的年级。0 代表非特定年级开课
		"target_grade": 0,

        // [list<str> 型] 授课教师。可能有多名
		"teacher": ["徐航"],

        // [float 型] 学分。实际操作按 0.5 的倍数取整
		"credit": 2.0,

		// [list<dict> 型] 行课安排
		"arrangements": [{
			// [list<int> 型] 上课周次
			"weeks": [2, 3, 5, 7, 9, 11, 13],

			// [int 型] 星期几
			"week_day": 1,

			// [list<int> 型] 
			// 每日授课节次。存在极少的不连续情况
			"sessions": [1, 2, 7, 8]

			// [str 型] 授课校区
			"campus": "闵行",

			// [str 型] 授课地点
			"classroom": "东下院402",
		}, < ... >]
		
        // [int 型] 选课学生人数（非实时数据）
		"student_number": 60
	}, 
	< ... >
	]

    // [str 型] 数据生成时间。yyyy-MM-DD HH:mm:ss
    "generate_time": "2018-12-03 14:37:44"
}