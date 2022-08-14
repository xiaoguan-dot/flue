import pymongo
"""
pymongo语法:
1.添加:集合.insert_[one|many]({"名称":内容})
2.删除:集合.delete_[one|many]({"名称":内容})
3.改动(更新):集合.update_[one|many]({"名称":内容},"改动方法($inc|$set)":{"名称":内容})
4.查询:集合.find_[one|many]({"名称":内容})
limit限定第()个内容,skip跳过第()个内容,sort计数
###删除合集:合集.drop
"""
mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
#markdown所见即所得
# 用户，博客名，博客内容，博客评论，全部博客，全部博客日期，个人简介，作者关于，网站首页，博客资源，外部资源
sql=mongo["blog"]#创建数据库
user=sql["user"]#用户名、密码
blogname=sql["blogname"]#所有博客名称
blogcontent=sql["blogcontent"]#博客内容，不包含博客内资源
comments=sql["comments"]#评论
date=sql["date"]#所有博客的创建日期，修改日期
intro=sql["intro"]#作者简介
resource=sql["resource"]#博客内资源
about=sql["about"]#关于作者
home=sql["home"]#首页信息
images=sql["images"]#除博客以外的所有资源（小图标，背景图等）
basic=sql["basic"]#网站后台基本定义信息