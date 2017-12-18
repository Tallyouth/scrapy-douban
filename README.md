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


