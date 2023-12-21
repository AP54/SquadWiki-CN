# SQUAD HOTFIX 7.0.1 RELEASE NOTES

> 页面贡献者：Offworld Industries
> 
> 原文章：[SQUAD HOTFIX 7.0.1 RELEASE NOTES](https://joinsquad.com/2023/12/14/squad-hotfix-7-0-1-release-notes/)
>
> 发布时间：2023/12/14

Squad Hotfix 7.0.1 is now live! Here are the extensive list of the changes:

## SYSTEM & GAMEPLAY UPDATES

- Adjusted TLF LAT 02 and LAT 03 kit inventory as follows:

    LAT 2:

      MPT76 + HNA

      RPG7 HEAT x2

      RPG7 Frag x2

    LAT 3:

      MPT76 + A940

      HAR66 x2

      Frag Grenade x1

- Adjusted the TLF SOR-109T SMG recoil to be less aggressive and more controllable in full-auto for short-range use.

## GENERAL BUG FIXES

- Fixed an issue where the TLF ACV-15 Open Top M2 and MG3 APC’s required a crewman for the driver.

- Fixed an issue with TLF being able to have two AR MG3+Irons kit roles in a squad, should now only be able to have 1 in a squad. This is unlocked when the squad reaches 3 squad members.

- Fixed missing text on the TLF LAT 01 RPG-7 v2 kit on the loadout screen.

- Fixed an issue with the RGF AK74M 1P78 scope which looked darker/more saturated/shinier than the rest of the weapon.

- Fixed an exploit where players could uncap their input on a joystick or steering wheel enabling them to zoom across the map in a vehicle at ludicrous speeds.

- Fixed an issue where Shoulders would look deformed when performing emotes with smaller weapons equipped.

- Fixed an issue where Armpits would look deformed during animations.

- Fixed an issue where the TLF Rally Point was accidentally using the ADF Rally Point when equipped in hands.

- Fixed an issue in the Infantry Tutorial where an NPC soldier would be T posing when they needed to be crouching.

- Fixed some client side log spam relating to Weapon Skins.

- Fixed an issue where Find Match was not working properly.

- Fixed an issue where you were unable to use Admin commands on a locally open map after disconnecting from a server.

- Fixed an issue where failed pings to servers would show -1000. This has been changed to 9999.

- Fixed an issue where filtering by Ping would not properly filter found results

      Fixed a Crash related to Alt Tabbing with DLSS enabled.

## MAP UPDATES & BUG FIXES

- Fixed an issue on Belaya RAAS v1 Where the PLANMC could place infinite HASCO bunkers with no resource cost.

- Fixed an issue on Belaya RAAS v1 where the description was incorrect.

- Fixed an issue where Yehorivka Invasion v5 was incorrectly labeled as v4.

- Fix an issue on Yehorivka Invasion v5 where the TLF ACV-15 would not spawn in.

## KNOWN ISSUES

- The Server Browser may refresh itself after an initial delay. We’re still investigating the underlying cause of this.

- Server Browser Filtering by Ping will not result in fetching only servers under that ping. It will instead filter the servers you already have in your current server browser view to that ping limit. Refreshing your server browser will fetch new results but could produce less results. This is due to a limitation with the amount of sessions EOS allows us to retrieve per call.

- Server Browser Filtering in general is done on results after they have been fetched. Epic Online Services will send its session results in whichever order it decides which is outside of our control. We consider this to be a significant issue and are doing our best to resolve this in a future update. Due to it happening after the results have been received, you may not be able to find a server you are looking for immediately and will need to click the Refresh Button a few times.

OFFWORLD OUT.