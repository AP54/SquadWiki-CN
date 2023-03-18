# 服务器配置

> 文章作者：桀氓AlbertWensley

本文将详细介绍 Squad 服务器的安装流程。

## 命令行

可以将以下参数加到您的启动命令行中来配置你的服务器，添加这些参数时要注意错别字。


- **MULTIHOME** = 服务器IP地址 (可选)
- **Port** = 游戏端口 (必要)
- **QueryPort** = Steam 查询端口 (必要)
- **RANDOM** = 地图循环方式 [ALWAYS, FIRST, NONE] (可选)
- **FIXEDMAXPLAYERS** = 最大玩家数量 (可选)
- **FIXEDMAXTICKRATE** = 服务器刷新率 [Tickrate] (可选)
- **PREFERPREPROCESSOR** = CPU Affinity (可选) UNTESTED
- **-log** = 显示日志窗口 (可选)
- **-fullcrashdump** = 崩溃时保存完整的服务器日志 (可选)

例子：`start SquadGameServer.exe MULTIHOME=127.0.0.1 Port=6301 QueryPort=26301 FIXEDMAXPLAYERS=100 FIXEDMAXTICKRATE=50 RANDOM=ALWAYS -log`

### 设置处理器使用率

#### 计算使用率

![Squad_Affinity_Calculator](./img/affinity.webp){width=100% loading=lazy}

1. 点击 **菜单图标**

2. 选择 **程序员** 模式

3. 选择 **位切换键盘**

4. 单击，直到看到 **BYTE** 就是 4 核心 8 线程。（您也可以切换其它选项来适配您的CPU）

5. 点击 **HEX** 切换到十六进制


核心线程计数从 0 开始，您可以在第三张图片中看到哪个数字负责哪个线程。1= 使用；0= 不使用；


所需的结果限制在 HEX 中，如果所有核心线程都为 1，结果将显示 "FF"。


对于我们的 "/AFFINITY" 参数，我们需要 "FF" 来设置 CPU 的核心线程使用率。


如果只选择核心线程 4-7 [0000 1111]，则对应结果应该为 "F"。


!!! warning "核心线程使用数"
    尽量使用偶数的核心线程使用数（2 4 6 8），否则容易造成服务端崩溃。 

```text
F = 2核心
FF = 4核心
FFF = 6核心
FFFF = 8核心
...
```

!!! info "Windows"
    您可以使用 start-命令 来设置每个服务器的核心线程使用率（如果您在一台主机上运行多个服务器）
    `start /AFFINITY C /WAIT SquadGameServer.exe Port=6301 QueryPort=26301 FIXEDMAXPLAYERS=100 RANDOM=ALWAYS -log`

!!! info "Linux"
    Linux 用户可以通过 "taskset" 命令来设置核心线程使用率，核心线程索引从 0 开始。如果您的处理器有 8 个核心，那么您可以分配的核心就是 0-7。 
    `taskset -c 0-3 ./SquadGameServer.sh Port=6301 QueryPort=26301 FIXEDMAXPLAYERS=80 RANDOM=NONE`

## 配置文件

如果 Squad 服务端已经正确安装在了服务器上，那么配置文件应当位于以下位置：

```text
.
└── SquadGame
    └── ServerConfig
        ├── Admins.cfg
        ├── Bans.cfg
        ├── CustomOptions.cfg
        ├── ExcludedFaction.cfg
        ├── ExcludedFactionSetups.cfg
        ├── ExcludedLayers.cfg
        ├── ExcludedLevels.cfg
        ├── LayerRotation.cfg
        ├── LevelRotation.cfg
        ├── License.cfg
        ├── MOTD.cfg
        ├── Rcon.cfg
        ├── RemoteAdminListHosts.cfg
        ├── RemoteBanListHosts.cfg
        ├── Server.cfg
        ├── ServerMessages.cfg
        └── VoteConfig.cfg
```

### Admins.cfg

可以创建一个权限组，并将管理员分配到该组中。您可以创建任意类型，任意数量的权限组。这些文件在更新时将不会被覆盖，所以当添加权限时您需要前往[官方Wiki/en](https://squad.fandom.com/wiki/Server_Configuration#Adding_Admins_in_Admins.cfg)更新。 

必须使用 SteamID64，您可以在 [SteamID I/O](steamid.io/lookup) 中转换。

```cfg
Group=SuperAdmin:changemap,cheat,private,balance,chat,kick,ban,config,cameraman,debug,pause
Group=Admin:changemap,balance,chat,kick,ban,cameraman,pause
Group=Moderator:changemap,chat,kick,ban
Group=Whitelist:reserve

//实习管理员
Admin=76561115695178:Moderator //玩家 5
Admin=8915618948911:Moderator //玩家 4

//管理员
Admin=7894591951519:Admin //玩家 3
Admin=7895365435431:Admin //玩家 8792

//超级管理员
Admin=7984591565611:SuperAdmin //玩家 2
Admin=7917236241624:SuperAdmin //玩家 1 

//白名单 - VIP&SVIP
Admin=7984591565611:Whitelist //玩家 123
Admin=7984591565523:Whitelist //玩家 156
```

!!! example "管理员权限列表"

    - changemap
        执行地图相关命令（修改预设、更换地图）。

    - canseeadminchat
        查看 Admin 频道和 Teamkill 信息。

    - balance
        忽略阵营平衡跳边。

    - pause
        执行对局命令（暂停、重启、结束）。

    - cheat
        执行作弊命令。

    - private
        为服务器添加密码。

    - chat
        发送广播、发送 Admin 信息。

    - kick
        踢出玩家。

    - ban
        封禁玩家。

    - config
        修改服务器配置。

    - immune
        无法被踢出或封禁。

    - manageserver
        管理/关闭服务器。

    - cameraman
        切换摄影机视角（俗称飞天）。

    - featuretest
        执行部分调试命令。

    - forceteamchange
        执行强制跳边命令。

    - reserve
        保留预留位。

    - debug
        执行调试命令。

    - teamchange
        无冷却跳边。

### Bans.cfg

这个文件储存的是封禁玩家列表，格式为：SteamID64:封禁时间戳 //备注

```cfg
76561198039509812:0 //永久封禁-使用作弊程序
7862895148978485:1623366856 //击杀友军
```

手动添加封禁玩家时，请使用换行符作为每个封禁玩家的分割。

如果要检查封禁玩家的封禁时间或创建一个限时的玩家封禁，请使用[此工具](https://tool.chinaz.com/Tools/unixtime.aspx)转换时间戳。


### LevelRotation.cfg

若您想使用分类循环请在Server.cfg内将“MapRotationMode=”设置为LevelList或者LevelList_Randomized即可。

```cfg
# v2.0 分类循环 : 里面的内容必须为相应的地图组，与在游戏内显示的地图不一样！
//注意：只有你使用LevelList模式或LevelList_Randomized模式才会使用此文件内的循环列表

AlBasrah
Belaya
Chora
Fallujah
FoolsRoad
Gorodok
Kamdesh
Kohat
Kokan
Lashkar
Logar
Mestia
Mutaha
Narva
Skorpo
Sumari
Tallil
Yehorivka

# v2.0 加拿大DLC

GooseBay

```

### LayerRotation.cfg

此运行模式与之前的循环方式一致，直接运行指定的地图，若您想使用该循环方法请在Server.cfg内将“MapRotationMode=”设置为LayerList或者LayerList_Randomized即可 

```cfg
# v1.0 地图循环

Al Basrah AAS v1
Al Basrah AAS v2
Al Basrah Insurgency v1
Al Basrah Invasion v1
Al Basrah Invasion v2
Al Basrah RAAS v1
Al Basrah Skirmish v1
Al Basrah Skirmish v2
Al Basrah TA v1
Al Basrah TC v1
Al Basrah TC v2

Belaya AAS v1
Belaya AAS v2
Belaya Invasion v1
Belaya Invasion v2
Belaya Invasion v3
Belaya RAAS v1
Belaya RAAS v2
Belaya RAAS v3
Belaya Skirmish v1
Belaya TC v1

Chora AAS v1
Chora AAS v2
Chora Insurgency v1
Chora Invasion v1
Chora Invasion v2
Chora RAAS v1
Chora RAAS v2
Chora Skirmish v1
Chora TC v1

Fallujah AAS v1
Fallujah AAS v2
Fallujah Insurgency v1
Fallujah Invasion v1
Fallujah Invasion v2
Fallujah Invasion v3
Fallujah RAAS v1
Fallujah RAAS v2
Fallujah RAAS v3
Fallujah Skirmish v1
Fallujah Skirmish v2
Fallujah TC v1
Fallujah TC v2

Fool's Road AAS v1
Fool's Road AAS v2
Fool's Road Destruction v1
Fool's Road Invasion v1
Fool's Road RAAS v1
Fool's Road RAAS v2
Fool's Road RAAS v3
Fool's Road Skirmish v1
Fool's Road Skirmish v2
Fool's Road TC v1

Gorodok AAS v1
Gorodok AAS v2
Gorodok Destruction v1
Gorodok Insurgency v1
Gorodok Invasion v1
Gorodok Invasion v2
Gorodok RAAS v1
Gorodok RAAS v2
Gorodok RAAS v3
Gorodok RAAS v4
Gorodok RAAS v5
Gorodok Skirmish v1
Gorodok TC v1

Jensen's Range v1
Jensen's Range v2
Jensen's Range v3

Kamdesh AAS v1
Kamdesh Insurgency v1
Kamdesh Insurgency v2
Kamdesh Invasion v1
Kamdesh Invasion v2
Kamdesh Invasion v3
Kamdesh RAAS v1
Kamdesh RAAS v2
Kamdesh RAAS v3
Kamdesh RAAS v4
Kamdesh Skirmish v1
Kamdesh TC v1
Kamdesh TC v2

Kohat AAS v1
Kohat AAS v2
Kohat Insurgency v1
Kohat Invasion v1
Kohat Invasion v2
Kohat RAAS v1
Kohat RAAS v2
Kohat RAAS v3
Kohat RAAS v4
Kohat Skirmish v1
Kohat TC v1

Kokan AAS v1
Kokan Insurgency v1
Kokan Invasion v1
Kokan RAAS v1
Kokan RAAS v2
Kokan Skirmish v1
Kokan TC v1

Lashkar Valley AAS v1
Lashkar Valley AAS v2
Lashkar Valley Insurgency v1
Lashkar Valley Invasion v1
Lashkar Valley RAAS v1
Lashkar Valley Skirmish v1
Lashkar Valley TC v1
Lashkar Valley TC v2

Logar Valley AAS v1
Logar Valley AAS v2
Logar Valley Insurgency v1
Logar Valley RAAS v1
Logar Valley Skirmish v1
Logar Valley TC v1

Mestia AAS v1
Mestia Invasion v1
Mestia Invasion v2
Mestia RAAS v1
Mestia Skirmish v1
Mestia TC v1

Mutaha AAS v1
Mutaha Invasion v1
Mutaha RAAS v1
Mutaha Skirmish v1
Mutaha TC v1
Mutaha TC v2

Narva AAS v1
Narva AAS v2
Narva AAS v3
Narva Destruction v1
Narva Invasion v1
Narva Invasion v2
Narva RAAS v1
Narva Skirmish v1
Narva TA v1
Narva TC v1
Narva TC v2

Skorpo AAS v1
Skorpo Invasion v1
Skorpo Invasion v2
Skorpo RAAS v1
Skorpo RAAS v2
Skorpo RAAS v3
Skorpo RAAS v4
Skorpo Skirmish v1
Skorpo TC v1
Skorpo TC v2
Skorpo TC v3

Sumari AAS v1
Sumari Insurgency v1
Sumari Invasion v1
Sumari RAAS v1
Sumari RAAS v2
Sumari Skirmish v1
Sumari TC v1

Tallil Outskirts AAS v1
Tallil Outskirts AAS v2
Tallil Outskirts Invasion v1
Tallil Outskirts Invasion v2
Tallil Outskirts Invasion v3
Tallil Outskirts RAAS v1
Tallil Outskirts RAAS v2
Tallil Outskirts RAAS v3
Tallil Outskirts RAAS v4
Tallil Outskirts Skirmish v1
Tallil Outskirts Skirmish v2
Tallil Outskirts Skirmish v3
Tallil Outskirts Tanks v1
Tallil Outskirts Tanks v2
Tallil Outskirts TA v1
Tallil Outskirts TC v1

Yehorivka AAS v1
Yehorivka AAS v2
Yehorivka Destruction v1
Yehorivka Invasion v1
Yehorivka Invasion v2
Yehorivka RAAS v1
Yehorivka RAAS v2
Yehorivka RAAS v3
Yehorivka RAAS v4
Yehorivka RAAS v5
Yehorivka Skirmish v1
Yehorivka Skirmish v2
Yehorivka Skirmish v3
Yehorivka TA v1
Yehorivka TC v1
Yehorivka TC v2




# v1.0 加拿大DLC

CAF_Al_Basrah_Invasion_v1
CAF_Al_Basrah_Invasion_v2
CAF_Belaya_AAS_v1
CAF_Belaya_RAAS_v1
CAF_Belaya_RAAS_v2
CAF_Chora_AAS_v1
CAF_Chora_RAAS_v1
CAF_Fallujah_Invasion_v1
CAF_Fallujah_RAAS_v1
CAF_Fools_Road_RAAS_v1
CAF_Gorodok_AAS_v1
CAF_Gorodok_Invasion_v1
CAF_Gorodok_RAAS_v1
CAF_Gorodok_RAAS_v2
CAF_Gorodok_TC_v1
CAF_Jensens_Range_v4
CAF_Kamdesh_Invasion_v1
CAF_Kamdesh_RAAS_v1
CAF_Kamdesh_TC_v1
CAF_Kohat_Invasion_v1
CAF_Kokan_RAAS_v1
CAF_Lashkar_Valley_Invasion_v1
CAF_Lashkar_Valley_RAAS_v1
CAF_Lashkar_Valley_TC_v1
CAF_Logar_Valley_RAAS_v1
CAF_Manic-5_AAS_v1
CAF_Manic-5_AAS_v2
CAF_Manic-5_Invasion_v1
CAF_Manic-5_Invasion_v2
CAF_Manic-5_RAAS_v1
CAF_Manic-5_RAAS_v2
CAF_Manic-5_RAAS_v3
CAF_Manic-5_RAAS_v4
CAF_Manic-5_Skirmish_v1
CAF_Manic-5_Skirmish_v2
CAF_Manic-5_TC_v1
CAF_Mestia_RAAS_v1
CAF_Mutaha_AAS_v1
CAF_Mutaha_RAAS_v1
CAF_Mutaha_RAAS_v2
CAF_Nanisivik_AAS_v1
CAF_Nanisivik_Invasion_v1
CAF_Nanisivik_RAAS_v1
CAF_Narva_RAAS_v1
CAF_Skorpo_RAAS_v1
CAF_Sumari_AAS_v1
CAF_Tallil_Outskirts_RAAS_v1
CAF_Tallil_Outskirts_RAAS_v2
CAF_Yehorivka_Invasion_v1
CAF_Yehorivka_RAAS_v1
CAF_Yehorivka_TC_V1
```

### MOTD.cfg

```html
<a>黄色字体</a>
<a href="link.com">黄色字体链接</a>
```

“MOTD” 必须大写。

### RemoteAdminListHosts.cfg

每行应包含指向 `Admins.cfg` ，格式遵循 ![Admins.cfg](#adminscfg)。

如果您运行多个服务器，且希望所有服务器都使用一个`Admins.cfg`文件，请使用此项。 