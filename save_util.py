# -*- coding:utf-8 -*-
import MySqlConn

import sql_template
import json


def save_word_words(json_info):
    """
        保存单词数据到 mysql 中
        :param json_info: json格式的单词数据
        :return:
        """
    mysql = MySqlConn.Mysql()
    try:
        json_info.pop('_id')
        mysql.insert_one(sql_template.INSERT_INTO_WORDS, (
            json_info['data']['id'],
            json_info['data']['content'],
            json_info['data']['pronunciations']['us'],
            json_info['data']['pronunciations']['uk'],
            json_info['data']['definition'],
            json.dumps(json_info, ensure_ascii=False),
            json_info['data']['audio']
        ))
        mysql.commit()
    except BaseException, arguement:
        print '插入信息失败,原因: ', arguement
    finally:
        mysql.dispose()

def clean_table_info():
    """
    清空其中的信息
    :return:
    """
    mysql = MySqlConn.Mysql()
    try:
        mysql.update(sql_template.USE_DATABASE_WORDS, ())
        mysql.delete(sql_template.CLEAN_TABLE_CET6, ())
        mysql.delete(sql_template.CLEAN_TABLE_CET4, ())
        mysql.delete(sql_template.CLEAN_TABLE_WORDS, ())
        mysql.commit()
    except BaseException, arguement:
        print '清空表失败,信息: ', arguement
    finally:
        mysql.dispose()
