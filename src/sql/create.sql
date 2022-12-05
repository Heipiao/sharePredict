create database usersInfo;
CREATE TABLE IF NOT EXISTS `all_user_info`(
`id` INT UNSIGNED AUTO_INCREMENT KEY COMMENT '用户编号',
`username` VARCHAR(20) NOT NULL UNIQUE COMMENT '用户名',
`nickname` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '昵称',
`rank` INT NOT NULL DEFAULT 1  COMMENT '等级',
`score` INT NOT NULL DEFAULT 0  COMMENT '积分',
`url` CHAR(200) NOT NULL DEFAULT '' COMMENT '头像url',
`password` CHAR(32) NOT NULL COMMENT '密码',
`email` VARCHAR(50) NOT NULL UNIQUE COMMENT '邮箱',
`age` TINYINT UNSIGNED NOT NULL DEFAULT 18 COMMENT '年龄',
`sex` ENUM('man','woman','baomi') NOT NULL DEFAULT 'baomi' COMMENT '性别',
`tel` CHAR(11) NOT NULL UNIQUE DEFAULT '' COMMENT   '电话',
`addr` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '地址',
`idcard` CHAR(18) NOT NULL UNIQUE  DEFAULT '' COMMENT  '身份证号',
`married` TINYINT(1) NOT NULL DEFAULT 0 COMMENT '0代表未结婚，1代表已结婚',
`salary` FLOAT(8,2) NOT NULL DEFAULT 0 COMMENT '薪水',
`job` CHAR(32) NOT NULL DEFAULT ''COMMENT '职业',
`school` CHAR(32) NOT NULL DEFAULT ''COMMENT '学历',
`uni` CHAR(32) NOT NULL DEFAULT '' COMMENT '大学学校'
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

insert into all_user_info(password,nickname,username,email,tel)values("123456","刘思亮","leoliu","lsl8315@163.com","15619461086");

create database businessInfo; 
CREATE TABLE IF NOT EXISTS `all_output_report_info_daily`(
`id` INT UNSIGNED AUTO_INCREMENT KEY COMMENT '唯一编号',
`dt` DATETIME NOT NULL  COMMENT '日期-年月日',
`create_time` DATETIME NOT NULL  COMMENT '日期-年月日时分秒',
`cost_time` INT  UNSIGNED  DEFAULT 0  COMMENT '花费的时间',
`share_daily_rise_summary` TEXT   COMMENT '每日涨停股推荐',
`share_daily_backtest` TEXT  COMMENT '每日回测结果',
`share_daily_fall_summary` TEXT COMMENT '每日跌停股推荐',
`etf_daily_summary` TEXT   COMMENT '每日ETF推荐',
`reserve_summary_1` TEXT  COMMENT '预留1',
`reserve_summary_2` TEXT  COMMENT '预留2',
`reserve_summary_3` TEXT   COMMENT '预留3',
`reserve_summary_4` TEXT  COMMENT '预留4',
`reserve_summary_5` MEDIUMTEXT COMMENT '预留5',
`reserve_summary_6` MEDIUMTEXT  COMMENT '预留6',
`reserve_summary_7` MEDIUMTEXT  COMMENT '预留7',
`reserve_summary_8` MEDIUMTEXT  COMMENT '预留8',
`reserve_summary_9` MEDIUMTEXT  COMMENT '预留9'
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

insert into all_output_report_info_daily(dt,create_time,share_daily_rise_summary)values(CURDATE(),NOW(),"[{\"name\":\"中国平安\",\"id\":\"000001.SZ\"},{\"name\":\"三一重工\",\"id\":\"600031.SH\"}]");
