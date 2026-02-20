# OpenResty从入门到实战

## 你将获得

*   构建OpenResty完整知识体系；
*   高性能OpenResty编码指南；
*   开源项目源码分析与实战；
*   从0搭建微服务API网关。

  

## 讲师介绍

温铭，OpenResty 软件基金会第一任主席，《OpenResty 最佳实践》开源书的发起人和作者，Apache APISIX 项目 VP。曾任某开源商业公司合伙人，前 360 开源技术委员会委员。他在互联网安全公司工作了 10 年，负责开发过云查杀、反钓鱼和企业安全产品。

  

## 课程介绍

对于每一个服务端开发工程师来说，高性能、高并发都是避不开的话题，谁不希望开发高性能的服务端，做出能支持千万甚至上亿用户的系统呢？

不管你的开发语言和平台是什么，学会 OpenResty 都会对你有所裨益。使用OpenResty，你可以用 Lua 语言来进行字符串和数值运算、查询数据库、发送 HTTP 请求、执行定时任务、调用外部命令等，还可以用 FFI 的方式调用外部 C 函数。这基本上可以满足服务端开发所需的所有功能。

可以说，掌握了 OpenResty，**你就可以同时拥有脚本语言的开发效率和迭代速度，以及 NGINX C 模块的高并发和高性能优势**。

不过，OpenResty 的学习资料还比较少，官方也只有 API 文档，而网上能找到的资料也不够系统。可以说，绝大部分的 OpenResty 使用者都是在摸着石头过河，很难实现系统、权威的学习。

在这个专栏里，温铭将带你轻松快速入门，并给你描绘 OpenResty 的全貌，建立完整的知识体系；同时，他会串联整个专栏来实战应用，带你从零开始搭建一个 API 网关。为了让你接触更真实的使用场景，温铭还在专栏里特别增加了多节视频课程，进行开源项目的源码分析和实战演练，帮你真正掌握OpenResty这款开发利器。

根据 OpenResty 使用者的现状分析，专栏内容分为5大模块。

**模块一，入门篇**。OpenResty 由 NGINX 和 LuaJIT 两部分构成，这一模块会介绍它们的基础知识，以及其中经常遇到的缺陷与陷阱；同时会带你浏览下OpenResty 仓库的近 70 个项目。虽然OpenResty 经常被叫做 ngx-lua，但 lua-nginx-module 仅仅是冰山一角，你需要清晰的全局观来学习 OpenResty 的“真面目”，不能“身在此山中”。

**模块二，API篇**。这是 OpenResty 对外暴露的 Lua 接口，也是你编写 OpenResty 代码最常用到的部分。这一模块会把这些指令和 API 分门别类逐步介绍给你，并引导你思考一些易忽略的关键点，比如，这些 API 为什么这么设计？为什么要增加一些看上去和 NGINX 无关的功能？希望能让你知其然，更知其所以然。

**模块三，测试篇**。这可能是本专栏最“高冷”的部分，不少 OpenResty 的代码贡献者都在编写测试案例时遇到过困难。`test::nginx` 功能异常强大，但也有很高的学习门槛，就连详细文档也不足以填平它。除此之外，这一部分还会带你讨论服务端性能测试，作为 OpenResty 中的最佳实践，在你测试 Java、Go、Node.js 等其他语言开发的系统时，它一样适用。

**模块四，性能优化篇**。OpenResty 的性能优化技巧，一直是开发者最关注的问题。这个模块会提供 OpenResty 的编码指南，让你从一开始写代码时，就能规避性能问题；并且会手把手地教你，如何使用火焰图这种科学、可量化的工具来定位性能问题，而不是依靠猜测。

**模块五，实战篇**。OpenResty 社区中有一个很明显的趋势，就是越来越多的开发者把 OpenResty 用在 API 网关的开发中，这是一个非常明智和务实的选择。这个模块会带你把前面所学的知识串联起来，搭建出一个 API 网关的雏形。你可以在此基础上，直接添加自己的模块来实现业务需求，不用再重新造轮子。

  

## 课程目录

![](https://static001.geekbang.org/resource/image/4d/20/4dce464099b7d47a8249602ce7a9bb20.jpg)

  

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
