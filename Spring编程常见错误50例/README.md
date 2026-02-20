# Spring编程常见错误50例

## 你将获得

*   拿来即用的 Spring 编程备忘录
*   Spring 核心技术及源码拆解
*   Spring Web 关键处理流程详解
*   Spring 开发 50+ 常见问题解决方案

  

## 讲师介绍

傅健，Netty 源码贡献者，《微服务之道：度量驱动开发》作者之一，思科中国研发中心平台软件工程师，从业经验 10 余年。

期间做过很多项目，从移动端应用到文档存储系统，从消息系统到电话接入系统。也接触过很多不同类型的开源软件，很喜欢深究原理，所以现在也是 Netty、Jedis、Spring Data Redis、influxdb–java、Jenkins 等很多开源项目的 Contributor。

  

## 课程介绍

Spring 的广泛应用，让原本一些错综复杂的开发工作变得简单起来。这也让很多后端程序员，尤其是 Java 程序员，从中获益。

只要你使用过 Spring，有过一些线上的开发经验，或多或少都会遇到类似这样的问题：

虽然完成了工作，但是总觉得心里没底。例如在给一个接口类添加 @RestController 注解时，你会想换成 @Controller 会更好吗？

为什么只是稍微“动”了下，就出故障了呢？例如在 Spring Boot 中，将 Controller 层的类移动到 Application 的包之外，Controller 层提供的接口就直接“失效”了。

而当真正遇到问题时，又该从何查起？例如有些代码在一些项目中是可以运行的，但是换成另外一个项目就不可以了。甚至有时候都不是换一个项目，只是添加了一些新功能，也会出问题。

当你习惯于 Spring 的便捷强大，是否还能跳出那些既定规则，去思考这些问题背后的原理？面对海量源码，又是否能够快速找到解决方案？

这个专栏衍生于傅健老师近 10 年的开发总结 ToDoList，从中节选出了 50+ 代表性案例进行分析，给出最佳解决方案，希望这份避坑指南能带给你最直接的帮助与收获！

### 课程设计

本专栏共分为以下三个部分，可以对照以下这张图去理解设计思路：

![](https://static001.geekbang.org/resource/image/83/fc/834c92d778378859acf4e0e02ee778fc.png)

**Spring Core 篇：**包括 Bean 定义、注入、AOP 等核心功能的使用问题讲解，这是 Spring 的基石。不管未来是做 Spring Web 开发，还是使用 Spring Cloud 技术栈，你都绕不开这些实践。

**Spring Web 篇：**出于大多项目使用 Spring 还是为了进行 Web 开发考虑，作者梳理了从请求 URL 解析、Header 解析、Body 转化到授权等 Web 开发必知必会案例。它们正好涵盖了从一个请求到来，到响应回去这一完整流程。

**Spring 补充篇：**重点介绍 Spring 测试、Spring 事务、Spring Data 相关问题。最后，总结 Spring 使用中发生问题的根本原因。

### 特别说明

1.  为了方便你实践与验证，示例代码可通过 [GitHub](https://github.com/jiafu1115/springissue) 链接下载，点击即可获取。
2.  专栏中案例+代码偏多，不建议仅通过音频学习，重点参考文稿。
3.  这门课需要一定的基础，你要清楚最基本的 Spring 使用知识，比如如何自动注入一个 Bean，如何使用 AOP 等。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/56/69/56b3694ccdde78cfc5197e9a28087069.jpg)

  

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
