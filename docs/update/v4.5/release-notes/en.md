# Squad Update v4.5 Release Notes

> 页面贡献者：Offworld Industries
> 
> 原文章：[SQUAD UPDATE V4.5 RELEASE NOTES](https://joinsquad.com/2023/05/23/squad-update-v4-5-release-notes/)
>
> 发布时间：2023/05/23

## Features

- Added more content for the newly improved Militia faction:

    - M16A2 Rifle
    - BMP-2 (no ATGM)
    - UB-32 Rocket Artillery Emplacement

## System & Gameplay Updates

- Switching to or reloading a coaxial vehicle weapon no longer causes the main gun to unload
- Commander artillery map markers have been updated to make the danger and corresponding radius of the artillery clearer to players. The actual radius and density of artillery strikes has not changed.
    - Map markers for artillery now appear in red color instead of yellow
    - An inner radius will display where artillery rounds have a chance of impacting
    - An outer radius will display how far away the artillery rounds’ damage radius can extend to
- AAVP, FV432 RWS, M113 TLAV, and MTLB 6MA APCs no longer require players to equip a crew role in order to use the driver and gunner seats
- Reduced the respawn timer for the T-62 MBT from 20 minutes to 15 minutes
- Increased the downward aiming angle of the ZiS3
- Reduced construction point cost for several fortifications and emplacements:
    - Conventional Forces:
        - HASCO Wall – from 300 to 150
        - HASCO Single – from 100 to 50
        - HASCO Bunker – from 250 to 150
        - HASCO HMG Bunker – from 350 to 200
        - HMG Emplacement – from 200 to 150
        - Indirect Fire Shelter – from 350 to 300
        - Razorwire – from 20 to 15
        - Sandbag Wall – from  40 to 25
        - Sandbag Wall + Firing Ports – from 40 to 25
    - Irregular Forces:
        - Irregular Wall – from 100 to 60
        - Irregular Sandbag Wall – from 20 to 10
        - Irregular Sandbag Wall + Firing Ports – from 20 to 10
- Made adjustments to the inventories of the CAF and BAF engineer roles:
  - CAF Engineer:
    - Changed C7A2 + C79A2 (4 mags) to C8A3 + C79A2 (5 mags)
    - Increased smoke grenades from 2 to 4
    - Increased razor wire from 1 to 2
    - Increased sandbags from 1 to 2
  - BAF Engineer:
    - Changed L85A2 + SUSAT (4 mags) to L85A2 + Elcan (6 mags)
    - Increased smoke grenades from 2 to 4
    - Increased razor wire from 1 to 2
    - Increased sandbags from 1 to 2
- When you’re part of a fireteam, your Fireteam leader will now have a marker that appears above them (similar to the existing Squad Leader markers)
-     Added a splash screen with server rules that appears when joining a server and added a rules tab to the deployment screen (Enter key by default) that allows players to review rules during a match more easily.
- The end of the match screen now has Add To Favorite button, so you can add a server as a favorite without leaving the game.
- Added a “Recently Played” badge to Find Match results and the server browser
- Added a “Max Ping” filter to the server browser
- Server cards layout has been updated
- Added info tooltips for Playstyle and Experience tags in the server browser
- Empty servers no longer appear when using the Find Match feature
- Added a visual indication (checkmark) of whether a player has customized their server browser filters or not
- Added HUD markers to the compass in the tutorial
- Added sound effects for soldier ragdoll impacts and scraping based on physical surface
- Added a setting to hide the “player connected” and “player disconnected” messages on the HUD
- Players can now select and copy the game version displayed on the main menu to allow for easier bug reporting

## General Bug Fixes

- Improved the post-processing effect on the main menu
- Interact widgets now appear as intended even when soldiers are in front of or ragdolled near the item
- Fixed a bug that awarded teams 80 points for destroying an objective in Insurgency instead of the intended 50
- Fixed a bug that prevented players inside of vehicles from being killed or ejected from their vehicle while inside a restriction zone
- Fixed a bug that could cause exploitable visual and gameplay issues when a player entered a vehicle in a certain way
- Operating the ZiS3 field gun emplacement without aiming down sights no longer causes camera issues
- Fixed a bug that caused the reload animation for emplacements to break if a user exited an emplacement midway through a reload
- Fixed an issue that caused smoke launchers to fire more canisters than intended
- Fixed several visual issues with the US Army soldier uniforms
- Weapons on the BMP-1 now have the correct switch and reload sounds
- Using the UAV camera no longer causes soldiers to appear to stutter while moving
- When joining a faction, the Objective mode pop up will no longer cover up the deployment tutorial
- Fixed several bugs related to the server browser UI
- The mute and unmute buttons on the Music Player now behave as intended
- Added missing Simplified Chinese translations
- Fixed a bug that prevented icons like the red exclamation mark from appearing alongside relevant notifications
- Fixed a visual issue FV510 IFV and FV520 CTAS40 IFV left track disappears at a certain range
- The BAF ammo box visuals now show the NLAW instead of the AT4
- Fixed gunshot sounds to USMC M16A4 Rifle

## Map Updates & Bug Fixes

- General

    > Fixed minor visual issues on Al Basrah, Anvil, Black Coast, Harju, Manicouagan, Mutaha, and Narva

- Belaya

    > Fixed an issue that allowed players to walk through walls in a certain location
    >
    > Adjusted the sheds at F3-6-4 so that players no longer have to crouch to enter them

- Goose Bay

    > Increased the restriction zone size for both teams on Seed v1

- Gorodok

    > Players can no longer vault through windows with bars on them in certain locations

- Manicouagan

    > Players can no longer see and shoot through the floor in a certain spot at the Dam Outlet

- Mutaha

    > Increased the restriction zone size for both teams on Seed v1
    >
    > Improved the minimap on Seed v1
    >
    > RGF main base trucks can now resupply as intended on Seed v1
    >
    > Fixed an issue that prevented the T72S from spawning in the MEA main rearm zone on Tanks v1

- Yehorivka

    > Fixed a bug that prevented players from falling through the barn roof properly

## SDK Updates & Bug Fixes

- Updated mod SDK to v4.5