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
# 用户名称，图标，文章名，内容，评论，历史文章，日期，简介，关于，首页，背景图
sql=mongo["blog"]#创建数据库
user=sql["user"]#用户名、密码
usericon=sql["usericon"]#用户图标
blogname=sql["blogname"]#所有博客名称
blogcontent=sql["blogcontent"]#博客内容，不包含博客内资源
comments=sql["comments"]#评论
date=sql["date"]#所有博客的创建日期，修改日期
intro=sql["intro"]#作者简介
resource=sql["resource"]#博客内资源
about=sql["about"]#关于作者
home=sql["home"]#首页信息
images=sql["images"]#除博客以外的所有资源（小图标，背景图等）