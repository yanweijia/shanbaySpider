#shanbaySpider

爬取扇贝英语单词数据,将数据存储到`MongoDB`中

语言版本: `Python 2.3`

使用前请先自行安装`MongoDB`数据库
```
pip install requests
pip install pymongo
pip install mysql-python DBUtils
```

获取到的数据可以自己对`save_vocabulary_info(json_info)`中的json_info进行存储

## 爬虫思路
先通过网址 `https://www.shanbay.com/api/v1/bdc/example/?type=sys&vocabulary_id=词汇编号` 遍历,

发现单词后再通过网址 `https://api.shanbay.com/bdc/search/?word=待查询单词` 查询,查询完成后存储到数据库中

具体请看代码中注释

## 注意
线程数别要设置太高,否则反爬机制会暂禁用 IP ,需要高效率爬虫可以自行添加代理

如
```
proxies={"http": "http://localhost:1080"}
res = request.get(url,proxies=proxies)
```

# 主要代码文件
shanbaySpider.py 爬虫类

converter.py  将爬取到mongoDB中的数据读取出来转换到mysql中.