# Linux内核技术实战课

## 你将获得

*   掌握 Linux 底层基础知识
*   疑难问题的排查定位方法
*   4 类稳定性问题案例分析
*   Linux 内核专家的应用实战经验

  

## 讲师介绍

邵亚方，前蘑菇街技术专家，Linux Kernel活跃贡献者，在Linux内核领域深耕了10余年，先后在华为、蘑菇街、Juniper Networks等知名互联网企业从事内核研发工作。他擅长从Linux系统内核层⾯来分析解决实际疑难问题，提高业务性能。Linux Kenrel活跃贡献者，主要活跃在Linux内核的内存管理子系统（linux-mm）。

  

## 课程介绍

我们知道，业务增长对服务稳定性的要求必定会急剧增加。像TCP重传该怎么分析、怎么在运⾏时不打断任务的情况下排查内存泄漏问题、CPU sys利⽤率⾼怎么办，这些实实在在的问题，不仅难以解决，甚至在定位和排查的环节就会面临诸多挑战。

实际上，应对复杂稳定性问题，除了从业务的视角来看以外，还需要你能够从系统、内核的视⻆来分析。一些业务高手，之所以能直击问题本质，解决别人解决不了的问题，也是因为他们能让内核知识为业务服务。比如，当发生TCP重传时，有人可以从tcpdump里面的信息看到是哪个TCP连接进行重传，然而高手们却可以通过这些信息看到为什么会发生重传。

当然，Linux内核知识本身就十分庞杂，学习曲线陡峭，对于应用开发者或者运维来说，确实没有必要去搞懂它的每个细节、机制，去理解它所有的设计思想。对于非内核从业者来说，能够让内核知识解决我们生产环境下遇到的实实在在的问题，更好地满足实际需求就够了。

邵亚方深耕Linux领域多年，他将通过“解决问题，满足需求”的方式，从生产环境中四类典型问题（Page Cache管理、内存泄漏、TCP重传、内核态CPU利用率飙高）入手，带你去了解：你的应用程序是怎么跟系统资源打交道的；你的业务类型应该要选择什么样的配置才会更好；出了棘手问题该如何一步步排查等问题，让Linux内核更好地服务你的应用程序。

#### 模块介绍

本课程包括4大模块，每个模块都会按照基础篇、案例篇和分析篇的方式来呈现。

**Page Cache管理模块**，会带你重点分析如何更好地利用Page Cache来减少无谓的I/O开销，Page Cache管理不当会引起的一些问题，以及如何去分析和解决这类问题。

**内存泄漏模块**，会为你重点分析应用程序都是如何从系统中申请内存以及如何释放的。通过内存泄露这类案例来带你了解应用程序使用内存的细节，以及如果内存使用不当会引发的一些问题。当然，也会带你去观察、分析和解决这类问题。

**TCP重传模块**，重点分析TCP连接的建立、传输以及断开的过程，分析这个过程究竟会受哪些配置项的影响，如果配置不当会引起什么网络问题。然后从TCP重传这类具体案例出发，来带你认识你必须要掌握的一些网络细节知识，以及遇到网络相关的问题时，你该如何去分析和解决它。

**内核态CPU利用率飙高模块**，带你分析应用程序该如何高效地使用CPU，以及哪些情况下会导致CPU的使用很低效：比如内核态CPU利用率过高就是一个很低效的表现。针对内核态CPU利用率高的这个案例，会侧重为你讲解哪些Linux内核的特性或者系统配置项会引起这种问题，以及如何分析和解决具体的问题。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/75/46/75f29596ebb715a663751f664ddcba46.jpg)

  

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
