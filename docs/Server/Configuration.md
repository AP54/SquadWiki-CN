# 服务器配置

> 文章作者：桀氓AlbertWensley

本文将详细介绍 Squad 服务器的安装流程。

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

## Admins.cfg

此文件用于配置服务器管理员，对其的修改会在下一场游戏开始后生效。

```cfg title="默认配置" linenums="1"
/////////////////////////////////////////////////////////////////////////////////////////////
//// Valid access levels are as follows													 
////		startvote - not used														 
////		changemap																	 
////		pause - Pause server gameplay												 
////		cheat - Use server cheat commands											 
////		private	- Password protect server											 
////		balance	- Group Ignores server team balance										 
////		chat - Admin chat and Server broadcast										 
////		kick																		 
////		ban																		  	 
////		config - Change server config												 
////		cameraman - Admin spectate mode												 
////		immune - Cannot be kicked / banned										 
////		manageserver - Shutdown server												 
////		featuretest - Any features added for testing by dev team					 
////		reserve - Reserve slot														 
////		demos - Record Demos on the server side via admin commands										 
////		clientdemos - Record Demos on the client side via commands or the replay UI.
////		debug - show admin stats command and other debugging info		
////		teamchange - No timer limits on team change			 
////		forceteamchange - Can issue the ForceTeamChange command
////		canseeadminchat - This group can see the admin chat and teamkill/admin-join notifications
/////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////
//		The Format for adding groups is:
//	Group=<Group Name>:<Permission 1>,<Permission 2>,<Permission 3>
//
//		For example:
//	Group=MyGroup: pause, demos, changemap
//
//		The groups below are the defaults, add to or change them as needed:
/////////////////////////////////////////////////////////////////////////////////////////////

Group=Admin:kick,ban,changemap
Group=Moderator:kick,ban

/////////////////////////////////////////////////////////////////////////////////////////////
//		The format for adding admins is:
//	Admin=<Steam ID #>:<Group Name>
//
//		For example:
//	Admin=123456:Admin		// Adam the admin
//	Admin=654321:Moderator	// Molly the moderator
//
//  Add your own below:
/////////////////////////////////////////////////////////////////////////////////////////////
```

`Admins.cfg` 共分为两个部分。

首先是管理员权限组的声明，形如 `Group=Admin:kick,ban,changemap`；

其次是管理员的声明，形如 `Admin=76561198123456789:Admin // 张三`。

### 管理员权限组

#### 格式

- `Group=<Group Name>:<Permission 1>,<Permission 2>,<Permission 3>`

- `Group=<权限组名>:<权限 1>,<权限 2>,<权限 3>`

#### 示例

- `Group=Admin:kick,ban,changemap,reserve,cameraman`

- `Group=VIP:reserve`

#### 解释

- 组名仅支持英文与数字，不支持中文。

- 权限组的权限由 **:** 后的权限标识决定，以逗号隔开，各权限标识的英文解释见默认配置中 1~24 行，中文解释见本维基[控制命令简介](/Command)页面。

### 管理员

#### 格式

- `Admin=<Steam ID #>:<Group Name>`

- `Admin=<SteamID64>:<权限组名>`

#### 示例

- `Admin=76561198123456789:Admin // 张三`

- `Admin=76561198987654321:VIP // 李四`

#### 解释

- 管理员的声明必须放在管理员权限组的声明之后。

- Steam账户的 64ID 可以在 [STEAMID I/O](https://steamid.io/lookup) 查询。

- 管理员声明支持以 '//' 开头的行内注释（注释支持中文），即一行中 '//' 后面的部分不会被认为是配置的一部分，可用于标识管理员身份。


## Bans.cfg

此文件用于记录封禁用户，对其的修改会在下一场游戏开始后生效。

默认的 `Bans.cfg` 为空文件。

### 格式

- `<banned player steamid>:<unix timestamp of ban expiration>`

- `<admin nickname> [SteamID <admin steamid>] Banned:<banned player steamid>:<unix timestamp of ban expiration> //<ban comment>`

- `<被封禁的 SteamID64>:<封禁截止 UNIX 时间戳>`

- `<管理员昵称> [SteamID <管理员 SteamID64>] Banned:<被封禁的 SteamID64>:<封禁截止 UNIX 时间戳> //<封禁注释>`

### 示例

```cfg
John [SteamID 76561198000000000] Banned:76561198000000001:0 //Permanent ban for cheating
John [SteamID 76561198000000000] Banned:76561198000000002:1623366856 //Team killing
76561198000000003:0 //Manually added ban
76561198000000004:0
```

### 解释

- “封禁截止 UNIX 时间戳” 一项填 “0” 即为永久封禁。

- 每行仅允许存在一条封禁记录。

- 手动添加封禁后，请务必保证文件的最后留有至少一行空行。

- 封禁记录中仅有“被封禁的 SteamID64”和“封禁截止 UNIX 时间戳”是必要的。

- [UNIX 时间戳转换为北京时间]（https://c.runoob.com/front-end/852/）