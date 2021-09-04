# 爬虫

爬取的视频范围是[B站“鬼畜”频道](https://www.bilibili.com/v/channel/68?tab=featured)的前5000条视频（按播放量排序）。

通过F12抓包，发现网页视频列表的加载是通过API请求，每次修改API的`offset`字段即可获取下一部分的视频，每次返回30个。虽然返回的内容中含有许多需要收集的信息，但是为了满足“主要内容通过爬取HTML获得”，故仅记录了这些视频的BV号，储存在本地。相关代码请见`claw/claw_list.py`。

为了爬取每个视频的信息，通过分析HTML，发现HTML中内嵌了一段JSON：`window.__INITIAL_STATE__`，其中包含视频的简介、UP主信息、投币点赞收藏数等需要的信息。于是使用正则表达式提取`r'window.__INITIAL_STATE__={[\s\S]*?};'`，解析为JSON后获得信息。视频的上传时间无法送JSON中获取，遂解析HTML，从`<meta>`中，使用正则表达式获得上传时间。相关代码请见`claw/claw_page.py`。

对于视频的评论，只能通过API获取，方式同样为加载JSON，故不赘述。代码请见`claw/claw_comment.py`。

值得一提的是，如果将爬虫的UA设置为BaiduSpider的UA，则可允许较快的请求。实际测试中，2Hz的爬取频率不会导致封禁。

爬虫的数据初步储存为JSON格式，随后将其导入SQL数据库中。

# 数据分析

