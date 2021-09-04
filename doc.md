# 服务器

## 系统功能

### 视频列表页（首页）

- 显示总数
- 视频标题、封面、作者
- 播放按钮，跳转B站链接
- 底部分页跳转

![网页捕获_4-9-2021_201510_localhost](https://img.i207m.top/2021/09_0c9b9b49acd356ae19ffdc420dd8392c.jpeg)

### UP主列表页

- 显示总数
- UP主名称、头像
- 底部分页跳转

![网页捕获_4-9-2021_201638_localhost](https://img.i207m.top/2021/09_cfba05a3720215f7be78431d5155ece1.jpeg)

### 视频信息页

- 视频播放量等信息
- UP主信息
- 嵌入播放器代码
- 视频简介
- 评论

![网页捕获_4-9-2021_201620_localhost](https://img.i207m.top/2021/09_1573dbd0cc05bd35153e4077fc9c8819.jpeg)

### UP主信息页

- UP主信息
- UP的视频列表
- 底部分页跳转

![网页捕获_4-9-2021_20170_localhost](https://img.i207m.top/2021/09_00e399f1702db4828377113cc02381dc.jpeg)

### 搜索页

- 可选择搜索类别
- 显示结果数量和用时（<1ms）
- 底部分页跳转

![网页捕获_4-9-2021_201741_localhost](https://img.i207m.top/2021/09_5e84a5ad51794df00fac63a2c44fd3fa.jpeg)

![网页捕获_4-9-2021_201836_localhost](https://img.i207m.top/2021/09_9677acbaa209505f6e0753efae494bdf.jpeg)

### 更多细节

- 界面是响应式的，会根据窗口大小重新布局元素。如图为移动端显示情况：

![网页捕获_4-9-2021_201523_localhost](https://img.i207m.top/2021/09_da1cd31124e3bffff0c0b851670428e3.jpeg)

![网页捕获_4-9-2021_201556_localhost](https://img.i207m.top/2021/09_f6dc01c1c4bc97f3a0ed5ecbdd1c87b7.jpeg)

- 鼠标悬浮动画
- 输入页码范围的错误提示
- “回到顶部”按钮

![屏幕截图 2021-09-04 212811](https://img.i207m.top/2021/09_5b838c2c5363f8547b16cd477bf3cb52.jpg)

## 数据

使用SQLite3管理数据。数据分为两个表，分别记录视频信息和UP主信息。结构如下：

```python
class Video(models.Model):
    aid = models.IntegerField(unique=True)
    bvid = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    cover = models.CharField(max_length=80)
    num_view = models.IntegerField()
    num_like = models.IntegerField()
    num_coin = models.IntegerField()
    num_favorite = models.IntegerField()
    up_id = models.IntegerField(db_index=True)
    up_name = models.CharField(max_length=40)
    up_face = models.CharField(max_length=80)
    upload_time = models.CharField(max_length=20)
    reply = models.JSONField()
    
class Up(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    face = models.CharField(max_length=80)
    sign = models.TextField()
    num_fan = models.IntegerField()
```

为加快响应速度，Video表对`id,aid,up_id`都建立了索引；Up表对`id`建立了索引。

视频信息共5006条，UP主信息共1900条。数据库总大小27.8MB。

## 相关技术

使用Django Template渲染网页。

CSS框架使用基于Material Design的[Dogfalo](https://github.com/Dogfalo)/**[materialize](https://github.com/Dogfalo/materialize)**库。这一框架较为轻便，仍具有许多功能，例如响应式布局等。且框架自带的卡片、按钮、输入框等样式可以方便地用于网页设计。

使用[vfeskov](https://github.com/vfeskov)/**[vanilla-back-to-top](https://github.com/vfeskov/vanilla-back-to-top)**库，实现“返回顶部”按钮。

搜索算法为SQLite3查询。
