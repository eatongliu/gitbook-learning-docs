# 图解 Google V8

## 你将获得

*   V8 执行 JavaScript 代码的完整流程；
*   JavaScript 的核心特性；
*   事件循环和垃圾回收的工作机制；
*   系统优化 JavaScript 执行效率的方法。

  

## 讲师介绍

李兵，《[浏览器工作原理与实践](https://time.geekbang.org/column/intro/216?utm_term=zeusC66GZ&utm_source=app&utm_medium=geektime&utm_campaign=216-end&utm_content=v8xiangqingyejianjie0316)》课程作者，前盛大创新院高级研究员，在浏览器和前端开发领域深耕了十余年。曾在盛大创新院参与WebOS 项目，在顺网科技带领团队打造了一款给全国网吧使用的“F1 浏览器”，目前致力于为企业提供前端项目咨询和浏览器研发的基础服务。

  

## 课程介绍

V8 是 Google 基于 C++ 编写的开源高性能 JavaScript 与 WebAssembly 引擎，主要的应用包括Chrome浏览器以及Node.js。得益于Chrome浏览器的市场占有率以及Chromium阵营的不断强大，V8已经成为了当今最主流的JavaScript引擎。

但很多前端开发人员对 V8 的理解还停留在表面，只是单纯地使用 JavaScript 和调用 Web API，并不了解 V8 这个“黑盒”内部是如何工作的，项目出现问题时，也只能是“头疼医头，脚疼医脚”，没有系统的解决策略；想要系统学习V8时，也不知道从何处着手，不能迅速抓住V8的核心知识要点。

因此，我们邀请了李兵，带来第二季课程《图解 Google V8》。在这个课程中，他将完整地梳理V8的核心知识体系，通过大量图片演示，深入浅出地讲解 V8 执行 JavaScript 代码的底层机制和原理。

通过学习这门课程，你不仅可以了解完整的 V8 编译流水线，还能通过对 V8 工作机制的学习，搞懂JavaScript语言的核心特性，进而从根源解决程序上的问题，加快 JavaScript 的执行速度。

# V8知识图谱

![](https://static001.geekbang.org/resource/image/0e/10/0ea66b6ea8045a7b5eb80b38fa2d3b10.jpg)

# 模块介绍

本课程包括三个模块，分别是 JavaScript 设计思想篇、V8 编译流水线篇、事件循环和垃圾回收篇。

**JavaScript 设计思想篇**，关注 JavaScript 的设计思想，讨论它背后的核心特性，以及V8是是怎么实现这些特性的。

**V8 编译流水线篇**，带你分析 V8 的编译流水线所涉及到的具体知识点，同时也会穿插讲解一些内存分配相关的内容，因为函数调用、变量声明、参数传递或者函数返回数值都涉及到了内存分配。

**事件循环和垃圾回收篇**，深入到 V8 的心脏事件循环系统中，学习 V8 是如何实现JavaScript 单线程执行的。同时，关注垃圾回收问题，打通 V8 分配内存和回收数据的整个链路，掌握系统排查问题的方法。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/26/e3/2684822c6cb6b453c6f4abb3d89822e3.jpg)

  

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
