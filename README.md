# scrapy-douban
基于scrapy框架
scrapy是爬虫一个很好用的框架，快速高效，下面是我爬取豆瓣影人图集的过程

编辑器：pycharm

平台：windows

python版本： python2.7.13

包只需要进入cmd，pip install scrapy就可以，不用安装其他第三方包

## pycharm
pycharm编辑器需要配置scrapy的运行环境，在根目录下创建一个begin.py文件，如下

### begin.py
![](https://github.com/Tallyouth/work-image/blob/master/QQ%E6%88%AA%E5%9B%BE20171218180519.png)

这是为pycharm运行scrapy做的配置，其实也就是在cmd命令行输入运行scrapy
### items.py
![](https://github.com/Tallyouth/work-image/blob/master/QQ%E6%88%AA%E5%9B%BE20171218182440.png)

当然，首先要做的就是在items中加入要储存的容器名，基本操作，哈哈

这里我爬取的是a_image_url，scrapy最主要的运行文件是spider下创建的一个文件（名字你随便起，不过你要让别人看的懂你在爬什么，要不还怎么装逼）
这里我随便起的，叫spider
### spider.py
![](https://github.com/Tallyouth/work-image/blob/master/QQ%E6%88%AA%E5%9B%BE20171218183631.png)

这里需要从scrapy的spider中导入scrapy最基本的爬虫类spider，而selector也是爬取网页信息的一种方式，当然还要从上面的items中导入刚才的容器类

name 很重要，就像汽车的钥匙

download_delay 设置下载延迟，爬虫还是要点道德的好不好

allowed_domains 规定你爬取的范围，默认全部，我发现不设置也有好处，这里就不说了

start_urls 这是爬虫的开始，第一个网络请求就是从这里开始的，具体大家看看源代码吧

这里我们爬取的是豆瓣（url=https://movie.douban.com/celebrity/1016930/photos/?type=C&start=0&sortby=like&size=a&subtype=a）

scrapy使用的是parse来实现爬取逻辑

item = SatomiPicItem()就是导入容器，用xpath从网页解析出来想好的东西，要放到这个容器里返回，交给后面的来处理

xpath用法自行Google 

一般来说，爬取不会爬取一页，我们要想实现爬取多页，就要爬取出来下一页的url，然后使用Requests（next_url）来爬取下一页，其实这里有个超级简单的方法，使用spiders下的Crawlspider类，可以实现网页的多页爬取，我这里不知道为什么老是网页重定向，还没弄清楚怎么回事儿
![](https://github.com/Tallyouth/work-image/blob/master/QQ%E6%88%AA%E5%9B%BE20171218183652.png)
### setting.py

这里面就是放置配置文件的，比如代理啊 设置下载延迟啊 什么的，我试过了，豆瓣是要使用代理的，设置user-agent，要不爬不下来，对了，保存文件的配置也在这里面
![](https://github.com/Tallyouth/work-image/blob/master/QQ%E6%88%AA%E5%9B%BE20171218200455.png)

### pipelines.py

![](https://github.com/Tallyouth/work-image/blob/master/QQ%E6%88%AA%E5%9B%BE20171218201113.png)

在scrapy里有一个专门下载图片的类，是ImagesPipeline，它可以通过get_media_requests函数来自动爬取图片

# 结束
到这里基本就结束了，运行begin.py文件，就开始爬取了，这里展示几张
![](https://github.com/Tallyouth/work-image/blob/master/3e21996a368818f75c6098ab230d655b4aaa3fa7.jpg)
![](https://github.com/Tallyouth/work-image/blob/master/3e35580bf260dee063676e721e6ea2aa28d0a1c7.jpg)
![](https://github.com/Tallyouth/work-image/blob/master/3e59ee7bfc10d9651ddbad600750946d39742699.jpg)
![](https://github.com/Tallyouth/work-image/blob/master/3ea1543a85ced3e270b83525f4dcc8665a0e2cc7.jpg)





