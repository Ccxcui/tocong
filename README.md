# tocong简介
linux系统下爬取tucong网站的图片并存入数据库
**scrapy工程的创建**  
在终端使用scrapy startproject work 创建work工程  
![创建工程](https://github.com/Ccxcui/tocong/blob/main/show/%E5%9B%BE%E7%89%871.png)
![打开工程]()
创建图虫爬虫  
![图虫爬虫]()
**对网页的分析并制定爬取策略**  
爬虫的入口页为：https://tuchong.com/explore/  
![网页入口]()
可以看到这页的每张图片都代表一个题材，点进去后就是这个题材下所有的相册，如下图：  
![网页结构]()
打开相册后发现相册里的图片都是用js加载的，面对这种情况可以自己分析js，并分析ajax请求，打开chrome的开发者模式，并刷新刚刚的页面  
![网页刷新后]()
看到提交请求的url以及返回的内容  
![url]()
拖动鼠标向下滑，我们可以看到请求的网页有规律地变化  
Page代表页数  
Count代表每页的图片数，为20  
于是我们可以构造出我们要爬取页面的url  
https://tuchong.com/rest/tags/自然/posts?page={}&count=20  
![url-2]()
![url-3]()
通过对其返回的内容分析，post_id下包含了图片的内容  
我们爬取图片的名字，地址，点赞人数，浏览人数  
并下载到本地，并且将图片名字和url地址保存到数据库  
**创建数据库的表**  
用mysql workbench创建数据库tupian，utf-8格式  
![sql-1]()
再在tupian数据库中创建一个tupian_table表，创建2列，一列为name，一列为url，都为字符串结构  
![sql-2]()
