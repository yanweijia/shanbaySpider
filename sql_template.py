# -*- coding:utf-8 -*-
# 创建 stock 数据库
CREATE_DATABASE_WORDS = "CREATE DATABASE IF NOT EXISTS `words` default charset=utf8"

USE_DATABASE_WORDS = "USE `words`"

# 创建 cet4 表
CREATE_TABLE_CET4 = """
    CREATE TABLE `cet4` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
          `word` varchar(100) NOT NULL DEFAULT '' COMMENT '单词',
          `pron_us` varchar(100) DEFAULT NULL COMMENT '美式音标',
          `pron_uk` varchar(100) DEFAULT NULL COMMENT '英式音标',
          `definition` varchar(255) DEFAULT NULL COMMENT '中文,词性及翻译',
          `other_info` text COMMENT '其他信息,JSON格式',
          `audio` varchar(5000) DEFAULT NULL COMMENT '美式读音,URL或base64编码',
          PRIMARY KEY (`id`),
          KEY `word_index` (`word`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='大学英语4级';
"""
# 创建 cet6 表
CREATE_TABLE_CET6 = """
    CREATE TABLE `cet6` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
          `word` varchar(100) NOT NULL DEFAULT '' COMMENT '单词',
          `pron_us` varchar(100) DEFAULT NULL COMMENT '美式音标',
          `pron_uk` varchar(100) DEFAULT NULL COMMENT '英式音标',
          `definition` varchar(255) DEFAULT NULL COMMENT '中文,词性及翻译',
          `other_info` text COMMENT '其他信息,JSON格式',
          `audio` varchar(5000) DEFAULT NULL COMMENT '美式读音,URL或base64编码',
          PRIMARY KEY (`id`),
          KEY `word_index` (`word`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='大学英语6级';
"""
# 创建 words 表
CREATE_TABLE_WORDS = """
    CREATE TABLE `words` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
          `word` varchar(100) NOT NULL DEFAULT '' COMMENT '单词',
          `pron_us` varchar(100) DEFAULT NULL COMMENT '美式音标',
          `pron_uk` varchar(100) DEFAULT NULL COMMENT '英式音标',
          `definition` varchar(255) DEFAULT NULL COMMENT '中文,词性及翻译',
          `other_info` text COMMENT '其他信息,JSON格式',
          `audio` varchar(5000) DEFAULT NULL COMMENT '美式读音,URL或base64编码',
          PRIMARY KEY (`id`),
          KEY `word_index` (`word`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='所有单词词汇表';
"""


# 清空 cet4 表
CLEAN_TABLE_CET4 = "DELETE FROM `cet4`"
# 清空 cet4 表
CLEAN_TABLE_CET6 = "DELETE FROM `cet6`"
# 清空 words 表
CLEAN_TABLE_WORDS = "DELETE FROM `words`"

# 插入数据到 CET4
INSERT_INTO_CET4 = "INSERT INTO `cet4` (`id`,`word`,`pron_us`,`pron_uk`,`definition`,`other_info`,`audio`)VALUES(%s,%s,%s,%s,%s,%s,%s)"
# 插入数据到 CET6
INSERT_INTO_CET6 = "INSERT INTO `cet6` (`id`,`word`,`pron_us`,`pron_uk`,`definition`,`other_info`,`audio`)VALUES(%s,%s,%s,%s,%s,%s,%s)"
# 插入数据到 WORDS
INSERT_INTO_WORDS = "INSERT INTO `words` (`id`,`word`,`pron_us`,`pron_uk`,`definition`,`other_info`,`audio`)VALUES(%s,%s,%s,%s,%s,%s,%s)"