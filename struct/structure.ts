
export interface Arrangement {
    // 单次上课的具体参数
    // 一门课可能会在一个学期内包含不同的课程教室组合
    // 由一个 Arrangement 数组来描述

    // 星期几？约定使用 1 ～ 7 分别代表周一到周日。
    week_day: number;
    
    // 授课周次
    weeks: number[];
    
    // 授课节次
    sessions: number[];
    
    // 授课校区
    campus: string;
    
    // 授课教室
    classroom: string;
}

export interface Curriculum {
    // 行课安排
    arrangements: Arrangement[];

    // [str 型] 历年分配的课程代码，不重复。
    identifier: string;

    // [str 型] 课程课号
    code: string;

    // [str 型] 开课院系
    holder_school: string;

    // [str 型] 课程名称
    name: string;

    // [int 型] 开课学年，n 代表 n 至 (n + 1) 学年
    year: number;

    // [int 型] 开课学期。1 代表秋季学期，2 代表春季学期，3 代表夏季小学期
    term: number;

    // [int 型] 授课面向的年级。0 代表非特定年级开课
    target_grade: number;

    // [list<str> 型] 授课教师。可能有多名
    teacher: string[];

    // [float 型] 学分。实际操作按 0.5 的倍数取整
    credit: number;
    
    // [str 型] 备注。或许为空。
    notes: string;
    
    // [int 型] 选课学生人数（非实时数据）
    student_number: number;
}