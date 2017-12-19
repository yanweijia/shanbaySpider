#shanbaySpider

爬取扇贝英语单词数据,将数据存储到`MongoDB`中

语言版本: `Python 2.3`

使用前请先自行安装`MongoDB`数据库
```
pip install requests
pip install pymongo
```

获取到的数据可以自己对`save_vocabulary_info(json_info)`中的json_info进行存储

## 爬虫思路
先通过网址 `https://www.shanbay.com/api/v1/bdc/example/?type=sys&vocabulary_id=词汇编号` 遍历,
发现单词后再通过网址 `https://api.shanbay.com/bdc/search/?word=待查询单词` 查询,查询完成后存储到数据库中