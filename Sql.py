#encoding=utf-8

# 创建gloryroad数据库sql语句
create_database = 'CREATE DATABASE IF NOT EXISTS gloryroad DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'

# 创建testdata表
drop_table_if_exist_sql="drop table if exists testdata;"

create_table = """
    
    create table testdata(
        id int not null auto_increment comment '主键',
        bookname varchar(40) unique not null comment '书名',
        author varchar(30) not null comment '作者',
        test_result varchar(30) default null,
        primary key(id)
    )engine=innodb character set utf8 comment '测试数据表';
"""
