# 公共命令

> 页面贡献者：桀氓AlbertWensley

本文详细介绍了 Squad 游戏中命令控制台（ ++tilde++ 键打开）的所有公共命令，建议各位玩家学习了解。

**当 Squad 发生不可预料的错误时，这些命令可能会很有用。**

## ChangeTeams

描述：切换阵营

参数：ChangeTeams

## ChangeTeamsWithId

描述：切换阵营（阵营 id 为 0 时效果与 [ChangeTeams](#changeteams)相同

参数：ChangeTeamsWithId <阵营id>

示例：`ChangeTeamsWithId 0`

## ChatAll

描述：公共频道发送信息

参数：ChatAll <信息>

示例：`ChatAll msg`

## ChatToTeam

描述：阵营频道发送信息

参数：ChatToTeam <信息>

示例：`ChatToTeam msg`

## ChatToSquad

描述：小队频道发送信息

参数：ChatToSquad <信息>

示例：`ChatToSquad msg`

## CreateRallyPoint 

描述：部署小队集结点（俗称“队包”）

参数：CreateRallyPoint

## CreateSquad

描述：创建小队

参数：CreateSquad <小队名称>

示例：`CreateSquad MBT`

## DisableUI

描述：关闭 UI

参数：DisableUI

## DisconnectToMenu

描述：离开服务器

参数：DisconnectToMenu

## GiveUp

描述：放弃等待（倒地后使用此命令以重新部署）

参数：GiveUp

## HighResShot

描述：指定分辨率截取屏幕，文件将位于`C:\Users\[username]\AppData\Local\SquadGame\Saved\Screenshots\WindowsNoEditor `

参数：HighResShot <分辨率或乘数>

示例：`HighResShot 4`

## JoinSquadWithName

描述：加入指定名称的小队

参数：JoinSquadWithName <小队名称>

示例：`JoinSquadWithName MBT`

## JoinSquadWithId

描述：加入指定编号的小队

参数：JoinSquadWithId <小队编号>

示例：`JoinSquadWithId 5`

## LeaveSquad

描述：离开小队

参数：LeaveSquad

## ListCommands

描述：列出所有命令

参数：ListCommands <1>|<0>

示例：`ListCommands 1`

## ListPermittedCommands

描述：列出允许执行的所有命令

参数：ListPermittedCommands <1>|<0>

示例：`ListPermittedCommands 1`

## ListSquads

描述：列出本阵营中所有小队

参数：ListSquads

## r.setres

描述：改变分辨率

参数：r.setres <分辨率>

示例：`r.setres 1920x1080`

## Respawn

描述：重新部署

参数：Respawn

## RecordHeatmap

意义不明，在此引用官方描述。

>Takes a resolution in meters a heatmap of stat data for the map, requires stat unit to be turned on.

> `RecordHeatmap <XStepSize> <YStepSize> <HeightOffset> <bUseRawValues [0|1]> <PositionWaitTime> <FileName>`

## SetHudWidgetsEnabled

描述：设置 HUD 小组件的可见性

参数：SetHudWidgetsEnabled <1>|<0>

示例：`SetHudWidgetsEnabled 0`

## ShowCommandInfo

描述：显示命令信息

参数：ShowCommandInfo <命令>

示例：`ShowCommandInfo Respawn`

## ShowNextMap

描述：显示下张地图

参数：ShowNextMap

## SLInviteMember

描述：邀请玩家进入小队

参数：SLInviteMember <玩家昵称>

示例：`SLInviteMember zhangsan`

## stat FPS

描述：显示帧率

参数：stat FPS

## stat Unit

描述：显示游戏、渲染和 GPU 时间

参数：stat Unit

## stat UnitGraph

描述：显示游戏、渲染和 GPU 时间图

参数：stat UnitGraph

## 参考资料

- [Server Administration - Squad Official Wiki](https://squad.fandom.com/wiki/server_administration)