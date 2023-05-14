# 服务器标签

> 文章作者：TL

本文将介绍 Squad 服务器标签的具体配置流程。

## 添加标记

标签可以在 `server.cfg` 中配置。它们应被添加到 `Tags` 行并用空格分隔。默认情况下，所有客户端过滤器都设置为显示 `Any` 标记，这将显示所有服务器，包括未标记的服务器。在客户端上按标记进行过滤将把搜索结果缩小到与过滤器中使用的标记匹配的服务器。我们建议您使用适用于您的服务器的每个类别的标签，因为它可以帮助玩家过滤服务器列表到他们的游戏风格和偏好。不添加标签将意味着玩家只能在服务器浏览器中看到你的服务器，如果他们没有过滤特定的标签类别。

例如：`Tags= language_en language_nl mode_aas mode_raas mode_invasion playstyle_relaxed exp_experience maprot_voting`

### 语言标签

最多添加两个。

- 英语: `language_en`

- 中文: `language_zh`

- 俄语: `language_ru`

- 德语: `language_de`

- 土耳其语: `language_tr`

- 乌克兰语: `language_uk`

- 法语: `language_fr`

- 葡萄牙语: `language_pt`

- 波兰语: `language_pl`

- 瑞典语: `language_sv`

- 泰语: `language_th`

- 荷兰语: `language_nl`

- 芬兰语: `language_fi`

- 朝鲜语: `language_ko`

- 西班牙语: `language_es`

- 挪威语: `language_no`

- 日语: `language_ja`

- 丹麦语: `language_da`

- 意大利语: `language_it`

- 捷克语: `language_cs`

- 他加禄语: `language_tl`

- 印尼语: `language_id`

- 哈萨克语: `language_kk`

- 阿拉伯语: `language_ar`

- 希伯来语: `language_he`

### 游戏模式标签

最多添加三个。

- Invasion: `mode_invasion`

- AAS: `mode_aas`

- RAAS: `mode_raas`

- Destruction: `mode_destruction`

- Territory Control: `mode_tc`

- Insurgency: `mode_insurgency`

- Seed: `mode_seed`

- Skirmish: `mode_skirmish`

- Training: `mode_training`
  
### 游戏风格标签

最多添加一个。

-  娱乐：`playstyle_relaxed`

-  高质量对局：`playstyle_focused`

-  军事模拟：`playstyle_milsim`

### 游戏经验标签

-  新手：`exp_newplayer`

-  老手：`exp_experience`

### 地图切换模式标签

-  地图池：`maprot_rotation`

-  玩家投票：`maprot_voting`

### 规则标签

规则标签只显示在服务器预览卡上。在服务器浏览器过滤器和查找匹配功能中不使用它们。

-  正确命名小队以获得载具使用权：`rule_vehicle_name_claim`

-  载具先到先得：`rule_vehicle_fcfs`

-  注重已知的点位不要急于去其他点位：`rule_play_objective`

-  不要去压家：`rule_no_main_camping`

-  需要载具装的载具禁止单载：`rule_no_soloing_vehicle`

-  锁队受到人数限制的：`rule_lock_restrictions`

-  `rule_mech_inf_restrictions `
