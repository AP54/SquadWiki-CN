import json

fjson = open("finished.json", "r", errors="ignore")
data = json.load(fjson)
faction = {
    "Australian Defence Force": "[ADF](/faction/adf)",
    "Russian Ground Forces": "[RGF](/faction/rgf)",
    "Middle Eastern Alliance": "[MEA](/faction/mea)",
    "British Armed Forces": "[BAF](/faction/baf)",
    "Insurgent Forces": "[INS](/faction/ins)",
    "United States Army": "[USA](/faction/usa)",
    "United States Marine Corps": "[USMC](/faction/usmc)",
    "Canadian Armed Forces": "[CAF](/faction/caf)",
    "Irregular Militia Forces": "[IMF](/faction/imf)",
    "People's Liberation Army": "[PLA](/faction/pla)",
    "PLA Navy Marine Corps": "[PLANMC](/faction/planmc)",
    "Russian Airborne Forces": "[VDV](/faction/vdv)",
    "Turkish Land Forces": "[TLF](/faction/tlf)",
}

weather = {
    "Sunet": "黄昏",
    "Sunrise": "黎明",
    "Sunset": "黄昏",
    "Morning Sunrise": "黎明",
    "Early Morning": "早晨",
    "Stormy": "暴雨",
    "Dusty Mid Day": "正午&扬沙",
    "Early Dawn (Dark)": "凌晨",
    "Dusk": "黄昏",
    "Clear Night": "晴夜",
    "Evening": "傍晚",
    "Partial Clouds Mid Day": "正午&多云",
    "Cloudy Mid Day": "正午&阴天",
    "Mid Day": "正午",
    "Foggy": "大雾",
    "Night": "夜晚",
    "Storm": "暴雨",
    "Sunny Mid Day": "正午",
    None: None,
    "Sand Storm Mid Day": "正午&沙暴",
    "Overcast": "阴天",
    "Sunny Afternoon": "下午&晴天",
    "Rain Storm": "暴雨",
    "Partial Cloudy Mid Day": "正午&多云",
    "Rainstorm": "暴雨",
    "Morning": "早晨",
}
cnt = 0
fmd = open("mapdata.md", "w", errors="ignore", encoding="UTF-8")

for index in range(len(data["Maps"])):
    para_str = ""
    para_str += "### %s\n\n" % (data["Maps"][index]["Name"])
    para_str += "切换代码： `AdminChangeLayer %s`\n\n" % (data["Maps"][index]["rawName"])
    para_str += "预设代码： `AdminSetNextLayer %s`\n\n" % (data["Maps"][index]["rawName"])
    try:
        para_str += "图层大小： %s\n\n" % (data["Maps"][index]["mapSize"])
        para_str += "光照情况： %s\n\n" % (weather[data["Maps"][index].get("lighting")])
        para_str += "旗点数量： %s\n\n" % (data["Maps"][index]["capturePoints"]['points'].get('numberOfPoints',"None"))
        para_str += "双方阵营： %s VS %s\n\n" % (
            faction[data["Maps"][index]["team1"]["faction"]],
            faction[data["Maps"][index]["team2"]["faction"]],
        )
        para_str += "初始票数： %s  -  %s\n\n" % (
            data["Maps"][index]["team1"]["tickets"],
            data["Maps"][index]["team2"]["tickets"],
        )
        vehicles_dict = {}
        teamvehicles = data["Maps"][index]["team1"].get("vehicles")
        para_str += '??? abstract "%s 载具"\n' % (
            faction[data["Maps"][index]["team1"]["faction"]]
        )
        if teamvehicles != None:
            for index_vehicle in teamvehicles:
                if index_vehicle["type"] in vehicles_dict:
                    vehicles_dict[index_vehicle["type"]] = (
                        vehicles_dict[index_vehicle["type"]] + 1
                    )
                else:
                    vehicles_dict[index_vehicle["type"]] = 1
            for output_vehicle in vehicles_dict.keys():
                para_str += "    - %s *%d\n" % (
                    output_vehicle,
                    vehicles_dict[output_vehicle],
                )

        para_str += "\n"
        vehicles_dict = {}
        teamvehicles = data["Maps"][index]["team2"].get("vehicles")
        para_str += '??? abstract "%s载具"\n' % (
            faction[data["Maps"][index]["team2"]["faction"]]
        )
        if teamvehicles != None:
            for index_vehicle in teamvehicles:
                if index_vehicle["type"] in vehicles_dict:
                    vehicles_dict[index_vehicle["type"]] = (
                        vehicles_dict[index_vehicle["type"]] + 1
                    )
                else:
                    vehicles_dict[index_vehicle["type"]] = 1
            for output_vehicle in vehicles_dict.keys():
                para_str += "    - %s *%d\n" % (
                    output_vehicle,
                    vehicles_dict[output_vehicle],
                )
        para_str += "\n\n"
        fmd.write(para_str)
        cnt += 1
    except KeyError:
        print(data["Maps"][index]["rawName"] + "\n")
print(cnt)
fmd.close()

flk = open("maplink.md", "w", errors="ignore")

modelist = [
    "AAS",
    "Destruction",
    "Insurgency",
    "Invasion",
    "RAAS",
    "Seed",
    "Skirmish",
    "TA",
    "Tanks",
    "TC",
    "Training",
]

for gamemode in modelist:
    mode_para = "## %s\n\n" % (gamemode)
    flk.write(mode_para)
    cnt = 0
    for index in range(len(data["Maps"])):
        if data["Maps"][index]["gamemode"] == gamemode:
            try:
                levelname = str(data["Maps"][index]["Name"])
                mapname = (
                    "-".join(str(data["Maps"][index]["mapName"]).split())
                    .lower()
                    .replace("'", "")
                )
                titlelink = "-".join(levelname.split()).lower().replace("'", "")
            except KeyError:
                print(data["Maps"][index]["Name"])
                continue
            try:
                link_str = "- [%s](/Map/%s/#%s)\n\n" % (levelname, mapname, titlelink)
            except TypeError:
                print(data["Maps"][index]["Name"])
                continue
            flk.write(link_str)
            cnt += 1
    modeinfo = "%s:%d\n\n" % (gamemode, cnt)
    print(modeinfo)
    flk.write(modeinfo)
flk.close()
