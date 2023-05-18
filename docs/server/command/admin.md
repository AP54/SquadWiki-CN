# 管理命令

> 页面贡献者：桀氓AlbertWensley

本文详细介绍了 Squad 游戏中命令控制台（ ++tilde++ 键打开）的所有管理命令，供管理员查阅。

普通玩家也可阅读本文作简单了解，若有意成为服务器管理员可前往[入驻组织](/union/)部分，查看各组织详情页中管理招募的相关信息。

有关命令权限的信息请查看[管理员权限级别 - 控制命令简介](/server/command)。

## AdminKick

权限：kick

描述：从服务器中踢出玩家

参数：Adminkick <昵称或SteamID> <踢出理由>

示例：`AdminKick zhangsan Intentional TK`

## AdminKickById

权限：kick

描述：从服务器中踢出玩家

参数：AdminKickById <玩家编号> <踢出理由>

示例：`AdminKickById 75 Intentional TK`

## AdminBan

权限：ban

描述：在服务器上封禁玩家。封禁时长格式：0=永久，1d=一天，1M=一月。

参数：AdminBan <昵称或SteamID> <封禁时长> <封禁理由>

示例：`AdminBan zhangsan 0 cheat`

## AdminBanById

权限：ban

描述：在服务器上封禁玩家。封禁时长格式：0=永久，1d=一天，1M=一月。

参数：AdminBanById <玩家编号> <封禁时长> <封禁理由>

示例：`AdminBan 75 0 cheat`


## AdminBroadcast

权限：chat

描述：发送广播信息

参数：AdminBroadcast <广播信息>

示例：`AdminBroadcast TK后请道歉！`

## ChatToAdmin

权限：chat

描述：发送 Admin 信息

参数：ChatToAdmin <信息>

示例：`ChatToAdmin example`

## AdminEndMatch

权限：pause

描述：立即结束对局

参数：AdminEndMatch

## AdminPauseMatch

权限：pause

描述：暂停对局

参数：AdminPauseMatch

## AdminUnpauseMatch

权限：pause

描述：继续对局

参数：AdminUnpauseMatch

## AdminChangeLayer

权限：changemap

描述：立即切换地图

参数：AdminChangeLayer <地图名称>

示例：`AdminChangeLayer Albasrah_AAS_v1`

## AdminSetNextLayer

权限：changemap

描述：切换预设地图

参数：AdminSetNextLayer <地图名称>

示例：`AdminSetNextLayer Albasrah_AAS_v1`

## AdminSetMaxNumPlayers

权限：config

描述：设置服务器玩家最大人数

参数：AdminSetMaxNumPlayers <最大玩家数量>

示例：`AdminSetMaxNumPlayers 95`

## AdminSetServerPassword

权限：config

描述：更改服务器密码。参数为空时即设置为无密码

参数：AdminSetServerPassword <服务器密码>

示例：`AdminSetServerPassword 112233`

## AdminSlomo

权限：cheat

描述：设置时间流速（基础倍率为 1）

参数：AdminSlomo <时间倍率>

示例：`AdminSlomo 0.5`

## AdminForceTeamChange

权限：forceteamchange

描述：强制玩家跳边

参数：AdminForceTeamChange <昵称或SteamID>

示例：`AdminForceTeamChange zhangsan`

## AdminForceTeamChangeById

权限：forceteamchange

描述：强制玩家跳边

参数：AdminForceTeamChangeById <玩家编号>

示例：`AdminForceTeamChangeById 75`


## AdminForceAllDeployableAvailability

权限：cheat

描述：设置是否忽略部署物生成规则

参数：AdminForceAllDeployableAvailability <0>|<1>

## AdminDisableVehicleClaiming

权限：cheat

描述：设置载具是否要求乘员装备

参数：AdminDisableVehicleClaiming <0>|<1>

## AdminForceAllRoleAvailability

权限：cheat

描述：设置兵种是否限制人数

参数：AdminForceAllRoleAvailability <0>|<1>

## AdminNetTestStart

权限：debug

描述：开始网络测试并显示客户端日志

参数：AdminNetTestStart

## AdminNetTestStop

权限：debug

描述：结束网络测试并显示客户端日志

参数：AdminNetTestStop

## AdminListDisconnectedPlayers

权限：kick

描述：列出最近断开连接的玩家

参数：AdminListDisconnectedPlayers

## TraceViewToggle

权限：featuretest

描述：在屏幕中心显示一个准星，并显示其瞄准对象的有关信息

参数：TraceViewToggle

## TraceViewToggle

权限：featuretest

描述：在屏幕中心显示一个准星，并显示其瞄准对象的有关信息

参数：TraceViewToggle

## AdminCreateVehicle

权限：featuretest

描述：生成一辆载具（仅在本地服务器或自定义服务器上可用）

参数：AdminCreateVehicle <载具路径>

示例：`AdminCreateVehicle /Game/Vehicles/Minsk_motorbike/BP_minsk.BP_minsk_C`

## AdminDemoteCommander

权限：kick

描述：卸任指挥官

参数：AdminDemoteCommander <玩家昵称>

示例：`AdminDemoteCommander zhangsan`

## AdminDemoteCommanderById

权限：kick

描述：卸任指挥官

参数：AdminDemoteCommanderById <玩家编号>

示例：`AdminDemoteCommanderById 75`

## AdminDisbandSquad

权限：kick

描述：解散小队

参数：AdminDisbandSquad <阵营编号=[1|2]> <队伍编号>

示例：`AdminDisbandSquad 1 3`

## AdminRemovePlayerFromSquad

权限：kick

描述：将玩家从小队中移除

参数：AdminRemovePlayerFromSquad <玩家昵称>

示例：`AdminRemovePlayerFromSquad zhangsan`

## AdminRemovePlayerFromSquadById

权限：kick

描述：将玩家从小队中移除

参数：AdminRemovePlayerFromSquadById <玩家编号>

示例：`AdminRemovePlayerFromSquad 75`

## AdminWarn

权限：kick

描述：警告玩家

参数：AdminWarn <玩家昵称或SteamID> <警告信息>

示例：`AdminRemovePlayerFromSquad zhangsan message`

## AdminWarnById

权限：kick

描述：警告玩家

参数：AdminWarn <玩家编号> <警告信息>

示例：`AdminRemovePlayerFromSquad 75 message`

## AdminForceNetUpdateOnClientSaturation

权限：debug

描述：意义不明，附官方描述如下。
    `If true, when a connection becomes saturated, all remaining actors that couldn’t complete replication will have ForceNetUpdate called on them `

参数：AdminForceNetUpdateOnClientSaturation <[0|1]>

## AdminProfileServer

权限：debug

描述：在服务器上开始一定时长的分析，记录将会在结束后保存在硬盘上

参数：AdminProfileServer <记录时长> <[0|1]>

## AdminRestartMatch

权限：pause

描述：重新开始对局

参数：AdminRestartMatch

## AdminSetPublicQueueLimit

权限：config

描述：设置服务器最大排队人数

参数：AdminSetPublicQueueLimit <最大排队人数>

示例：`AdminSetPublicQueueLimit 25`

## 参考资料

- [Server Administration - Squad Official Wiki](https://squad.fandom.com/wiki/server_administration)