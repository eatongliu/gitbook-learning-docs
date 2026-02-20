# 深入剖析Kubernetes

## 你将获得

*   容器基础知识详解
*   从 0 搭建 Kubernetes 集群
*   剖析 Kubernetes 的核心特性
*   掌握基于 Kubernetes 的容器编排

  

## 讲师介绍

张磊，曾就职于微软研究院，《Docker 容器与容器云》作者，2021年 CNCF 基金会 TOC 名单中国内唯一的入选者。

Kubernetes 社区资深成员与项目维护者，长期专注并活跃于容器集群管理与云计算数据中心领域，连续三次被微软授予该领域“最有价值专家”（MVP）称号。

  

## 课程介绍

过去几年，以 Docker、Kubernetes 为代表的容器技术已发展为一项通用技术，BAT、滴滴、京东、头条等大厂，都争相把容器和 K8S 项目作为技术重心，试图“放长线钓大鱼”。

但容器技术本身偏向运维，namespace 资源隔离、cgroups 资源限制等概念，对开发者来说，理解起来比较困难。尤其在实施 K8S 落地时，总有一些问题被反复提及，比如：

*   为什么容器里只能跑“一个进程”？
*   之前一直用的某个 JVM 参数，在容器里怎么不好使了？
*   为什么 Kubernetes 不能固定 IP 地址？容器网络连不通，该如何 Debug？
*   K8S 中 StatefulSet 和 Operator 到底什么区别？PV 和 PVC 又该怎么用？

这些问题的答案和原理并不复杂，但很难一两句话解释清楚。因为容器技术涉及操作系统、网络、存储、调度、分布式原理等方方面面的知识，是个名副其实的全栈技术。

而其技术体系里那些“牵一发而动全身”的主线，比如 Linux 进程模型对容器本身的重要意义，“控制器”模式对整个 K8S 项目提纲挈领的作用等等，不会详细展现在 Docker 或 Kubernetes 官方文档中，但它们**才是掌握容器技术体系的精髓所在**，这也是张磊的《深入剖析 Kubernetes》专栏的核心内容。

张磊花费数月时间，经过多次改版，构建出如今的知识框架，适合所有初学者和进阶容器技术的伙伴，帮你逐层理清容器背后的技术本质与设计思想，并结合对其核心特性的剖析与实践，加深你对容器技术的理解。

本专栏共包括如下四大模块：

**1\. “白话”容器技术基础：**用饶有趣味的解说，梳理容器技术生态的发展脉络，讲述容器技术的来龙去脉与实现原理，让你知其然，并且知其所以然。

**2\. Kubernetes集群的搭建与实践：**以浅显易懂的语言，讲述Kubernetes集群背后的原理，并从0开始搭建一套Kubernetes集群，带你领略Kubernetes集群的“一键安装”。

**3\. 容器编排与Kubernetes核心特性剖析：**这个模块从分布式系统设计的视角出发，归纳出这些特性中体现出来的普遍方法，然后再逐一阐述Kubernetes项目关于编排、调度和作业管理的各项核心特性。

**4\. Kubernetes开源社区与生态：**磊哥会带你思考如何同团队一起平衡内外部需求，逐渐成为社区中不可或缺的一员。

专栏上线两年多，口碑一直不错，希望也能帮你在技术实践中发挥出 Kubernetes 最大的价值。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/df/4a/dfc800cca64bfc384aeabfd275e1404a.jpg)[](https://time.geekbang.org/hybrid/pvip?utm_term=zeusGWSM1&utm_source=zeusEEMMH&utm_medium=wechat-social&utm_campaign=K8s&utm_content=100092901)

  

## 适合人群

*   具备一定服务端基础知识，对容器感兴趣的互联网从业者；
*   想要进阶容器技术的软件开发人员；
*   希望在容器时代大展拳脚的运维工程师和架构师；
*   希望了解和学习容器技术背后原理的技术管理者、技术销售和市场从业者。

  

## 特别放送

#### 免费领取福利

[![](https://static001.geekbang.org/resource/image/b0/9b/b01d6e3d17b9708b70b81ce043e4e69b.jpg?wh=1035x360)](https://u.geekbang.org/subject/intro/1000861?utm_source=zhuanlanxiangqingye&utm_medium=app&utm_term=appzhuanlanxiangqingye&gk_cus_user_wechat=university)  
  

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
