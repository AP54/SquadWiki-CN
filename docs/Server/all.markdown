#服务器配置教程
====================================================================================
>文章作者：crystal

本文将介绍Squad服务器的具体配置流程。

##导航栏
1. [命令行](#command)
    1.1 [设计处理器使用率](#set)
    1.2 [计算使用率](#set)
    1.3 [Winsows](#Windows)
    1.4 [Linux](#Linux)

2. [配置文件](#disposition)
   2.1 [权限组【管理员】](#pzfile)
   2.2 [权限列表](#permissions)
   2.3 [封禁玩家](#playerban)
   2.4 [地图循环模式](#map1)
   2.5 [地图循环：添加创意工坊地图](#map2)
   2.6 [服务器介绍【每日消息】](#server)
   2.7 [远程权限组【管理员】列表](#server)
   2.8 [远程封禁玩家列表](#server)
   2.9 [服务器配置](#serverset)
   2.10 [服务器消息](#servermessage)
   2.11 [远程管理【Rcon】](#servermessage)

3. [比赛模式](#match)
   
   <span id ="command"> </span>
![](2023-03-08-00-49-49.png)

<font size=5>命令行</font>
________
可以将以下参数添加到您的启动命令行中来配置你的服务器，添加这些参数时要注意错别字

<br>
</br>

**MULTIHOME** =  服务器IP地址可选(可选)
**Port** =    游戏端口(必要)
**QueryPort** =    Steam查询端口(必要)
**RANDOM** =    地图循环方式[ALWAYS,FIRST,NONE] (可选)
**FIXEDMAXPLAYERS** =  最大玩家数量(可选)
**FIXEDMAXTICKRATE** = 服务器刷新率[Tickrate] (可选)
**PREFERPREPROCESSOR** = CPU Affinity (可选) UNTESTED
**-log** = 显示日志窗口 (可选)
**-fullcrashdump** = 崩溃时保存完整的服务器日志 (可选)

例子：

    start SquadGameServer.exe MULTIHOME=127.0.0.1 Port=6301 QueryPort=26301 FIXEDMAXPLAYERS=100 FIXEDMAXTICKRATE=50 RANDOM=ALWAYS -log

<span id ="set"></span>

<br>
</br>

<font size=5> 设置处理器使用率</font>
________
<br></br>
计算使用率
![](../Squad_Affinity_Calculator.png)

***打开您的Windows计算器***

1- 点击**菜单图标**
2- 选择**程序员模式**
3- 选择**位切换键盘**
4- 单击，知道看到**BYTE**就是四核心八线程(您也可以切换其他选项来适配您的CPU)
5- 点击**HEX**切换到十六进制

核心线程计数从 0 开始，您可以在第三张图片中看到哪个数字负责哪个线程。1=使用；0=不使用；
所需的结果限制在 HEX 中，如果所有核心线程都为 1，结果将显示 "FF"。
对于我们的 "/AFFINITY" 参数，我们需要 "FF" 来设置 CPU 的核心线程使用率。
如果之选择核心线程 4-7 [0000 1111]，则对应结果应该为 "F"。
<font color=red size=4>尽量使用偶数的 核心线程 使用数（2 4 6 8），否则容易造成服务端崩溃。</font>

    F=2核心
    FF=4核心
    FFF=6核心
    FFFF=8核心
    .....以此类推

<br>
</br>

<span id="Windows"></span>

<font size=4.5>Windows</font>

您可以使用 start-命令 来设置每个服务器的核心线程使用率（如果您在一台主机上运行多个服务器）：


    start /AFFINITY C /WAIT SquadGameServer.exe Port=6301 QueryPort=26301 FIXEDMAXPLAYERS=100 RANDOM=ALWAYS -log
<br>

<span id ="Linux"></span>

<font size=4.5>Linux</font>



Linux 用户可以通过 "taskset" 命令来设置核心线程使用率，核心线程索引从 0 开始。如果您的处理器有 8 个核心，那么您可以分配的核心就是 0-7。


    cd server1; taskset -c 0-3 ./SquadGameServer.sh Port=6301 QueryPort=26301 FIXEDMAXPLAYERS=80 
    RANDOM=NONE

<span id="disposition"></span>
<br>
</br>
<br>
</br>

<font size=5> 配置文件</font>
______

服务器的配置文件目录位于：C:\servers\squad_server\SquadGame\ServerConfig\

    Admins.cfg                     # 权限组[管理员]
    Bans.cfg                       # 封禁玩家列表
    License.cfg                    # 许可证
    MapRotation.cfg                # 地图循环列表
    MOTD.cfg                       # 服务器介绍[每日消息]
    Rcon.cfg                       # 远程管理配置
    RemoteAdminListHosts.cfg       # 远程权限组[管理员]列表
    RemoteBanListHosts.cfg         # 远程封禁玩家列表
    Server.cfg                     # 服务器配置
    ServerMessages.cfg             # 服务器循环[红字]公告
 
 <span id="pzfile"></span>
<br>
</br>
<font size=4>权限组【管理员】</font>

____
文件名：Admins.cfg

可以创建一个权限组，并将管理员分配到该组中，您可以创建任意类型，任意数量的权限组。这些文件在更新时将不会被覆盖，所以当我们添加权限时您需要前往官方[Wiki/cn]()更新。

必须使用 SteamID64，您可以在 steamid.io/lookup 中转换。

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

<span id="permissions"></span>
<br>
</br>

权限列表

    changemap                      # 更换/预设地图              
    pause                          # 暂停游戏
    cheat                          # 使用作弊命令
    private	                       # 设置服务器密码
    balance	                       # 忽略服务器阵营平衡
    chat                           # 管理员聊天/服务器公告
    kick                           # 踢出玩家
    ban                            # 封禁玩家
    config                         # 更改服务器配置
    cameraman                      # 摄影机 - 管理员视角
    immune                         # 无法被 踢出/封禁
    manageserver                   # 关闭服务器
    reserve                        # 预留位
    debug                          # 调试
    teamchange                     # 忽略更换阵营时间限制
    forceteamchange                # 允许执行强制更换阵营命令
    canseeadminchat                # 查看 管理员聊天/友军击杀/管理员加入 消息 

<span id="playerban"></span>
<br>
</br>
封禁玩家：Bans.cfg

这个文件储存的是封禁玩家列表，格式为：SteamID64:封禁时间戳//备注

    76561198039509812:0 //永久封禁-使用作弊程序
    7862895148978485:1623366856 //击杀友军 
手动添加封禁玩家时，请使用**换行符**作为每个封禁玩家的分割

如果要检查封禁玩家的封禁时间或创建一个限时的玩家封禁，请使用此工具转换时间戳：
- https://tool.chinaz.com/Tools/unixtime.aspx

<span id="map1"></span>
<br>
</br>

<font size=4>地图循环模式</font>
_____

在2.0地图更新后，现在有两种模式来进行地图循环，第一种是分类循环，第二种是逐个循环，逐个循环方法与1.0的MapRotation.cfg的方法类似

**文件名：LevelRotation.cfg**

若您想使用分类循环请在Server.cfg内将“MapRotationMode=”设置为LevelList或者LevelList_Randomized即可

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
    Manic-5

**文件名：LayerRotation.cfg**

此运行模式与之前的循环方式一致，直接运行指定的地图，若您想使用该循环方法请在Server.cfg内将“MapRotationMode=”设置为LayerList或者LayerList_Randomized即可

``` 
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
<span id="map2"></span>
<br>
<font size=4>地图循环：</font>
详情请看：[如何添加一个或多个Steam创意工坊地图到您的Squad服务器](severworkshop.md)
 
 
 <br>
 <span id="server"></span>
 </br>
 <br>

<font size=4>服务器介绍【每日消息】</font>
**文件名：MOTD.cfg**

MOTD.cfg 支持两个 HTML 标记：

    <a>黄色字体</a>
    <a href="link.com">黄色字体链接</a>
<font color=red>注意：MOTD.cfg 文件名必须是大写的，对 UNIX 很重要。</font>

<br>
</br>

<font size=4>远程权限组【管理员】列表</font>

**文件名：RemoteAdminListHosts.cfg**

每行应包含指向 封禁玩家 列表的URL，封禁玩家格式与上面 封禁玩家 相同。
如果您运行多个服务器，且希望所有服务器都使用一个 封禁玩家 文件，请使用此项。

<br>
</br>
<br>

<font size=4>远程封禁玩家列表</font>
**文件名：RemoteBanListHosts.cfg**

每行应包含指向 封禁玩家 列表的URL，封禁玩家格式与上面 封禁玩家 相同。

如果您运行多个服务器，且希望所有服务器都使用一个 封禁玩家 文件，请使用此项。

<span id="serverset"></span>
<br>
</br>
<br>
<font size=4>服务器配置</font>
____
**文件名：Server.cfg**

这个文件储存的是常规的服务器配置，新添加的内容请前往 官方Wiki/en 更新。
因此您如果想更改默认值，您需要手动把配置项添加到现有服务器配置中。

- 如果服务器名称的特殊字符在 服务器列表 中显示为 "?????"，解决方法：将特殊字符粘贴到文本编辑器，然后再复制到配置文件。示例：ServerName="Test Server Λ".
- AutoTkBanTime: 此选项可用于在服务器玩家击杀7个友军时，自动封禁的时间秒数。例子: AutoTkBanTime=1209600 封禁玩家 14 天
- PublicQueueLimit：标准是 PublicQueueLimit=25，这将公共队列限制为 25。=0 意味着不会有公共队列。=-1 是无限队列。

```c
ServerName="Squad Dedicated Server"
IsLANMatch=false
ShouldAdvertise=true
MaxPlayers=40
NumReservedSlots=0
PublicQueueLimit=25
NumPlayersDiffForTeamChanges=3
AllowTeamChanges=true
PreventTeamChangeIfUnbalanced=true
EnforceTeamBalance=true
RejoinSquadDelayAfterKick=180
ServerMessageInterval=300
ServerPassword=Password
AutoTkBanTime=1209600
TKAutoKickEnabled=true //设置为 false 则禁用服务器击杀友军自动踢出，认证服务器必须为 true。
RecordDemos=false
VehicleClaimingDisabled=false
VehicleKitRequirementDisabled=false
AllowQA=false
// 强制启用服务器认证 (仅 OWI 开发人员 & qa 管理员)
AllowCommunityAdminAccess=false
// 强制启用服务器认证 (仅 OWI 开发人员)
AllowDevProfiling=false
```

<span id="servermessage"></span>
<br>
</br>
<font size=4>服务器消息</font>

<br>

**文件名：ServerMessages.cfg**

在游戏中每次隔x秒按顺序循环发送一条消息（基于服务器配置）

<br>
</br>

<font size=4>远程管理[Rcon]</font>

**文件名：Rcon.cfg**

如果您不想使用远程管理[Rcon]，请将密码[Password=]设置为空。 注意：如果IP为0.0.0.0，将自动绑定到默认的公网IP。

```dotnetcli
// 远程管理[Rcon] IP
// 或者，在命令行中使用以下参数来设置：
// RCONIP=0.0.0.0
   IP=0.0.0.0

// 远程管理[Rcon] 端口
// 或者，在命令行中使用以下参数来设置：
//  RCONPORT=21114
    Port=21114

// 远程管理[Rcon] 密码
// 如果为空，则关闭 远程管理[Rcon]。
// 或者，在命令行中使用以下参数来设置：
//  RCONPASSWORD=MyPassword
    Password=

// 远程管理[Rcon] 并发数量
// 同时使用 Rcon 连接到服务器的最大数量
// 或者，在命令行中使用以下参数来设置：
// RCONMAXCONNECTIONS=5
   MaxConnections=5

// 远程管理[Rcon] 超时时间（秒）
// 可选值为：30 - 3600
// 或者，在命令行中使用以下参数来设置：
// RCONSECONDSBEFORETIMEOUTCHECK=120
   SecondsBeforeTimeoutCheck=120
```

<span id ="match"></span>
<br>

<font size=5>比赛模式</font>
_____

1. 要启用比赛模式，至少启动一次服务器以生成必要的文件。
2. 进入服务器文件夹，找到 \Saved\Config\WindowsServer 或 Saved\Config\LinuxServer 下的 Game.ini 文件，然后根据需要 添加/修改 内容。
3. 需要重新启动服务器才能更改比赛模式配置。