# 正则表达式入门课

## 你将获得

*   正则表达式的系统学习路径
    
*   事半功倍的分类记忆法
    
*   常见正则问题及解决方案
    
*   多场景案例实操正则应用
    

  

## 讲师介绍

涂伟忠，现任某大型企业高级研发工程师，工作以来一直从事后端服务研发工作，在服务端开发方面有非常丰富的实战经验。编程十多年来，他一直坚持技术输出，著有《Django开发从入门到实践》一书，也是极客时间每日一课《[15分钟带你快速掌握正则表达式](https://time.geekbang.org/dailylesson/detail/100044029)》的作者。

  

## 课程介绍

作为计算机领域最伟大的发明之一，正则表达式简单、强大，它可以极大地提高我们文本处理的效率。但是，很多人提起正则，都会是下面这样的场景：

1.  哎，不会写正则，算了，从网上直接找现成的吧；
2.  阻挠我学正则的，不是我的内心，而是难记的正则符号。

你是不是也觉得似曾相识呢？但如果止步于此，我们永远都不能真正掌握正则这个利器。

比如，我们很难从网上找到适合自己业务场景的正则表达式，如果自己还不会改的话，就很容易出现性能问题，例如正则出现大量的回溯，拖垮了CPU。

除此之外，不会正则还会降低我们的工作效率，其实很多看似麻烦的事情，用正则可以轻松搞定。比如下面这个例子，从文本中找出连续出现的重复单词。你可以看到，正则可以很方便地帮我们搞定这个需求。

```
>>> import re
>>> test_str = "the little cat cat in the hat hat."
>>> re.sub(r'(\w+) \1', r'\1', test_str)
'the little cat in the hat.'

```

因此，涂伟忠老师打算用一套系统化的方式教你巧妙地记忆、掌握正则，并一步步讲述正则的知识框架，最后通过对比不同编程语言和编译器中的正则，教你在实操中理解并学会正则表达式。

## 课程模块设计

课程共两个模块，分别是基础篇和应用篇。

**正则基础篇**

基础篇将讲述正则的基础概念和知识，比如正则元字符、匹配模式等，帮助用户巧妙记忆正则，并系统地建立有关正则的基础框架，为下一步的进阶打下基础。

**正则应用篇**

在应用篇中，将讲述正则的进阶内容，比如正则中的断言是什么，正则都有哪些流派，不同编译器里的正则都有什么不同？通过这些内容，可以让你更加游刃有余地使用正则，把正则这个工具更好地落地到实际工作中。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/af/3b/af068e3af5a2723dc2036bf4deac2f3b.jpg)

  

## 特别放送

#### 免费领取福利

[![](https://static001.geekbang.org/resource/image/69/dc/69c52d08278a2164dc5b061ba342a5dc.jpg?wh=960x301)](https://time.geekbang.org/article/427012)

  

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
