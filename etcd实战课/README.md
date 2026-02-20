# etcd实战课

## 你将获得

*   etcd 系统学习路径
*   etcd 核心原理解析
*   掌握实践中各类 etcd 问题的解决方案
*   构建高可靠的 etcd 集群运维体系

  

## 讲师介绍

唐聪，腾讯云资深工程师，etcd 活跃贡献者。

唐聪一直从事于内部公共组件建设，曾负责大规模排行榜、Redis 平台建设，目前负责腾讯云及内部公共 etcd 平台的建设与维护，是腾讯云 etcd 负责人。

他主导了腾讯 etcd 平台从 0 到 1 的建设，解决过众多大规模业务增长过程中遇到的存储稳定性、可扩展性等痛点，拥有万级 Kubernetes 和 etcd 集群规模的实战、治理经验。同时，他也是 2020 年 etcd 社区全球 Top3 的活跃贡献者，修复了 etcd 数据不一致、内存泄露、死锁、panic 等众多问题，提升了 etcd 在大规模数据场景下的启动、读性能等。

  

## 课程介绍

随着 Kubernetes 成为容器编排领域霸主，etcd 也越来越火热。目前，etcd 的 GitHub star 数已超过 34.2K，它的应用场景相当广泛，从服务发现到分布式锁，从配置存储到分布式协调等等。可以说，etcd 已经成为了云原生和分布式系统的存储基石。

另外，etcd 作为最热门的云原生存储之一，在腾讯、阿里、Google、AWS、美团、字节跳动、拼多多、Shopee 等公司都有大量的应用，覆盖的业务可不仅仅是 Kubernetes 相关的各类容器产品，更有视频、推荐、安全、游戏、存储、集群调度等核心业务。

但是很多同学在使用 Kubernetes、etcd 的过程中，或多或少都会遇到下面这些问题：

*   etcd Watch 机制能保证事件不丢吗？ (原理类)
*   哪些因素会导致你的集群 leader 发生切换呢? (稳定性类)
*   为什么基于 Raft 实现的 etcd 还可能会出现数据不一致呢？ (一致性类)
*   当你在一个 namespace 下创建了数万个 Pod/CRD 资源时，同时频繁通过标签去查询指定 Pod/CRD 资源时，APIServer 和 etcd 为什么扛不住呢? (最佳实践类)

基于此，唐聪老师从自己万级 Kubernetes 集群和 etcd 集群规模的治理相关经验出发，把 etcd 的学习过程分为了大中小三个目标，让你由小及大，从掌握一个个知识点的小目标出发，做到了解、熟练使用 etcd 的中等目标，最终能够完美解决业务过程中的各类痛点。

**模块设置**

课程主体分为两大模块，分别是**基础篇**和**实践篇**。

**基础篇**

基础篇会帮助你建立起对 etcd 的整体认知，搞懂读写请求、各个核心特性背后的原理，为后面的实践篇打下基础。

另外，基础篇也是对一个中小型分布式存储系统从 0 到 1 的实现案例解读，学习它你收获的不仅仅是 etcd，更是如何构建分布式存储系统的理论知识。

**实践篇**

实践篇将带你从 0 到 1 亲手参与构建一个简易的分布式 KV 数据库，进一步提升你对分布式存储系统的认知。为你分析 etcd 在 Kubernetes 中的应用，让你对 Kubernetes 原理有更深层次的理解。

当然，顾名思义，实践篇还会为你解读 etcd 在实际使用过程中可能会出现的各类典型问题，帮助你提前避坑，遇到类似问题时能独立分析、解决。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/26/a2/26acb9e8e3c4bab313da8c32487940a2.png)

  

## 特别放送

#### 免费领取福利

[![](https://static001.geekbang.org/resource/image/16/13/1664800067c250a67yy94c57d0e76c13.jpg?wh=1035x360)](https://time.geekbang.org/article/428647)  
  

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
