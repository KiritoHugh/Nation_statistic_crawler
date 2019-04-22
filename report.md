# 爬国家统计局数据 & 用Python连接mysql数据库



------

本次任务主要用到一些网络爬虫的基本知识，还有mysql的一些基础知识，以及使用python的mysql的API.

## 1.代码细节

- 设计了一个类.在设计这个类时,我特地考虑了如何提高此类的可重用性.
  特别的，在登记数据的成员函数中，传入参数设计为了爬到的数据numpy矩阵,namelist　指出了该矩阵数据的表头,tablename　是要登记数据的表的名字,yearspan　是数据的时间跨度（这里一般数据都有年份这个属性）.对于提交到数据库的sql语句,都由这些参数生成,而不是一句句手写.

```python
＃　每个实例对应一个数据库 ip 地址以及 database 的名称,用户的名称,密码．
class Cnect_Database(object):
    ＃　初始化
    def __init__(self,ip,user,db,charset):
    
	＃　连接数据库
	def connect(self,ps):

	＃　向数据库中某表登记数据
	def register(self,data,namelist,tablename,yearspan):

	＃　从数据库中检索数据
	def retrieval(self,itemlist,tablename):
```

* 对于从网站爬数据,以及绘图的操作,由于每次的任务的变化都很大，所以没有必要封装成类.所以就封装为函数,分别放在get_from_web.py 和　create_fig.py 函数中.

  

* 一个觉得很有用的小技巧：把一个多层dict,list嵌套的形式的str转换为python中的多层dict,list嵌套变量的方法.

  使用　eval()　函数可以直接得到是python对象的返回值．

  使用exac() 可以运行字符串形式的python语句，在需要敲重复代码的地方非常好用．

  

  

## 2.统计图机及其分析

<figure><img src = 'https://github.com/KiritoHugh/Nation_statistic_crawler/blob/master/HW1_1.png'><figcaption><center>hw1.1</figcaption></figure>

<figure><img src = 'https://github.com/KiritoHugh/Nation_statistic_crawler/blob/master/HW1_2.png'><figcaption><center>hw1.2</figcaption></figure>

<figure><img src = 'https://github.com/KiritoHugh/Nation_statistic_crawler/blob/master/HW1_3.png'><figcaption><center>hw1.3</figcaption></figure>

<figure><img src = 'https://github.com/KiritoHugh/Nation_statistic_crawler/blob/master/HW1_4.png'><figcaption><center>hw1.4</figcaption></figure>

* 可以看到我国人口近20年来一直稳定增长，2018年我国人口已经约14亿.可见我国人口大国的称号名副其实. hw1.1图中，男女人口数的各自细节不能明显看出，在hw1.3图中，可以更好的看到，在政府的宣传以及时代的进步下，民众的生育观念进步了，更加科学了，所以男女比失调的现象越来越得到改善，可以预测，在接下来的几年里，这一情况还将持续改善．hw1.2图中，可以明显的看到，城市人口的增长远超过总人口的增长，相应的，农村人口减少的也特别快，这是因为近年来，我国的城市化进程发展的非常快，所以农村人口向城市人口转化的进程就进行的特别快．

在第一个任务里，我们能初步看到我国人口数量和比例在近年来的变化．为了进一步考察我国的人口变化细节，于是第二个任务选择爬取人口的增长率信息．

<figure><img src = 'https://github.com/KiritoHugh/Nation_statistic_crawler/blob/master/HW2_popu.png'><figcaption><center>hw2.1</figcaption></figure>

<figure><img src = 'https://github.com/KiritoHugh/Nation_statistic_crawler/blob/master/HW2_ratio.png'><figcaption><center>hw2.2</figcaption></figure>

* hw2.1是根据爬取的信息所绘制的人口数相对数量图，可以看到，2018年的我国人口已经是1999年人口的115%左右了，这还是在实行计划生育的时期，所以可以想到，由于人口基数大以及我国民众的传统观念，计划生育控制人口是一个非常明智的政策．

* hw2.2图中分别画出了人口的出生率，死亡率，自然增长率．可以看到在计划生育的实行下，人口的出生率在下降中趋于平缓．其中值得注意的是2014年和2016年，我国在2013开始实施＂单独二孩＂（夫妻一方是独生子女），所以2014年，出生率出现一次小幅上扬．2015年我国开始实施＂全面二孩＂政策，所以2016年出生率出现一次大幅上扬,不过接下来的两年，人们对生育的热情似乎放缓．
  对于死亡率，近20年来人口死亡率比较稳定，不知道为什么2006年起死亡率略微上升了一些，可能是那时起到达自然死亡年龄的所对应的几十年前的人口数变多了．



## 3.收获与感受

* 学会了一些网络爬虫的基本知识．以及相关的python工具包．

* 学会了一些数据库的基本概念，以及sql语句．还学会了在本地部署sql服务器,以及python的sql工具包．

* 进一步熟悉了Matplotlib工具包．

* 知道了一个国家宏观信息的来源，国家统计局网址．

* 深度了解了我国近20年来的人口的各方面情况．

* 关于写爬虫的感受

  * 静态网页很好爬：

    * 只要用requests库直接把html爬下来，然后用正则表达式匹配即可。但是到了目前互联网发展阶段，已经很少有静态网页了。

  * 动态网站：

    * 所谓的动态的网页，就是网页编写者只是将网页写成一个框架，具体的数据会放在服务器的数据库了。

      比如说，网页是一个书架，你希望获得金融类的书籍，那你就可以向服务器发出这么一个请求——“我希望获得金融类的书籍”，那么服务器就会返回相应的书籍，书架上就会呈现相应的金融类的书籍。这里的请求实际上是http请求，也就是网页作为前端与服务器作为后端之间的信息通信。动态网页是目前比较常见的网页形式，因为数据量越来越大，动态网页逐渐成为一种呈现的方式，具体的数据会保存在服务器的数据库中，并且不断地改变着。

    * http 请求主要有get,post 两种．可以构造按规则构造url，从而从服务器请求得到数据.

    * 有的网站不是用发送请求的方式获得数据的．这时候可以模拟浏览器行为，比如使用Selenium（本来是用来做网站的自动化测试的）．但是速度就比较慢了．