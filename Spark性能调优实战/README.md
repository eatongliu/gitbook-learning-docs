# Spark性能调优实战

## 你将获得

*   深入浅出的 Spark 核心原理
*   全面解析 Spark SQL 性能调优
*   应用开发、配置项设置实操指南
*   手把手带你实现一个分布式应用

  

## 讲师介绍

吴磊，现任 Comcast Freewheel 机器学习团队负责人，负责计算广告业务中机器学习应用的实践、落地与推广。曾任职于 IBM、联想研究院、新浪微博，具备丰富的数据库、数据仓库、大数据开发与调优经验。

吴磊热爱技术分享，擅长从生活的视角解读技术。做过Spark Summit China 2017 讲师、World AI Conference 2020 讲师，在《IBM developerWorks》和《程序员》杂志，以及InfoQ上发表过多篇技术文章，深受好评。

  

## 课程介绍

目前，Spark已然成为分布式数据处理技术的事实标准，也在逐渐成为各大头部互联网公司的标配。对于数据领域的任何一名工程师来说，Spark开发都是一项必备技能；而想要进入大厂，就更得有丰富的Spark性能调优经验。

可现实情况是，我们想要快速上手开发应用很容易，把握应用的执行性能却总也找不到头绪，比如：

*   明明都是内存计算，为什么我用了RDD/DataFrame Cache，性能反而更差了？
*   网上吹得神乎其神的调优手段，为啥到了我这就不好使呢？
*   并行度设置得也不低，为啥我的CPU利用率还是上不去？
*   节点内存几乎全都划给Spark用了，为啥我的应用还是OOM？

为此，我们特意邀请到了吴磊老师，他根据自己多年的数据处理经验，梳理出了一套关于性能调优的方法论，帮助你在有效加速 Spark 作业执行性能的同时，也建立起以性能为导向的开发习惯。

除此之外，他还会手把手教你打造一个分布式应用，带你从不同角度洞察汽油车摇号的趋势和走向，让你对性能调优技巧和思路的把控有一个“质的飞跃”。

* * *

### **课程模块设计**

课程按照原理、性能、实战分为三大部分。

**原理篇**：主要讲解与性能调优息息相关的核心概念，包括RDD、DAG、调度系统、存储系统和内存管理。力求用最贴切的故事和类比、最少的篇幅，让你在最短的时间内掌握其核心原理，为后续的性能调优打下坚实的基础。

**性能篇**：虽然Spark的应用场景可以分为5大类，包括海量批处理、实时流计算、图计算、数据分析和机器学习。但它对Spark SQL的倾斜和倚重也是有目共睹，所以性能篇主要分两部分来讲。

一部分主要讲解性能调优的通用技巧，包括应用开发的基本原则、配置项的设置、Shuffle的优化、资源利用率的提升。另一部分会专注于数据分析领域，借助Spark内置优化如Tungsten、AQE和典型场景如数据关联，总结Spark SQL中的调优方法和技巧。

**实战篇**：以2011-2019的《北京市汽油车摇号》数据为例，手把手教你打造一个分布式应用，带你从不同角度洞察汽油车摇号的趋势和走向，帮助你实践我们的方法论和调优技巧，不仅要学得快，也要学得好！

除此之外，课程更新期间，还会不定期地针对一些热点话题进行加餐。比如，和Flink、Presto相比，Spark有哪些优势；再比如，Spark的一些新特性，以及业界对于Spark的新探索。这也能帮助你更好地面对变化，把握先机。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/f9/f7/f9fc3d1cyy855100f0be324122dccef7.png)

  

## 特别放送

#### 免费领取福利

[![](https://static001.geekbang.org/resource/image/0c/04/0caf085f7c8a0cdda793d541722dcf04.jpg?wh=1029x315)](https://time.geekbang.org/article/374158)  
  

#### 限时活动推荐

[![](https://static001.geekbang.org/resource/image/67/a0/6720f5d50b4b38abbf867facdef728a0.png?wh=1035x360)](https://shop18793264.m.youzan.com/wscgoods/detail/2fmoej9krasag5p?dc_ps=2913145716543073286.200001)

  

## 订阅须知

1.  订阅成功后，推荐通过“极客时间”App端、Web端学习。
2.  本专栏为虚拟商品，交付形式为图文+音频，一经订阅，概不退款。
3.  订阅后分享海报，每邀一位好友订阅有现金返现。
4.  戳此[先充值再购课更划算](https://shop18793264.m.youzan.com/wscgoods/detail/2fmoej9krasag5p?scan=1&activity=none&from=kdt&qr=directgoods_1541158976&shopAutoEnter=1)，还有最新课表、超值赠品福利。
5.  企业采购推荐使用“[极客时间企业版](https://b.geekbang.org/?utm_source=geektime&utm_medium=columnintro&utm_campaign=newregister&gk_source=2021020901_gkcolumnintro_newregister)”便捷安排员工学习计划，掌握团队学习仪表盘。
6.  戳此[申请学生认证](https://promo.geekbang.org/activity/student-certificate?utm_source=geektime&utm_medium=caidanlan1)，订阅课程享受原价5折优惠。
7.  价格说明：划线价、订阅价为商品或服务的参考价，并非原价，该价格仅供参考。未划线价格为商品或服务的实时标价，具体成交价格根据商品或服务参加优惠活动，或使用优惠券、礼券、赠币等不同情形发生变化，最终实际成交价格以订单结算页价格为准。
