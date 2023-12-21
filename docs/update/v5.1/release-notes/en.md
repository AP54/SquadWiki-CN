# SQUAD HOTFIX 5.1 RELEASE NOTES

> 页面贡献者：Offworld Industries
> 
> 原文章：[SQUAD HOTFIX 5.1 RELEASE NOTES](https://joinsquad.com/2023/07/25/squad-update-v5-1-release-notes/)
>
> 发布时间：2023/07/25

We have updated our Pacific Proving Grounds map, added one new map layer, and introduced updates for several existing map layers:

## PACIFIC PROVING GROUNDS V2
Pacific Proving Grounds v2 is an expanded version of the Pacific Proving Grounds map with brand-new islands and gameplay areas to discover.

### PPGv2 Map Layers
- Seed v1 – USMC vs PLANMC
- AAS v1 – USMC vs PLANMC
- AAS v2 – ADF vs PLA

## NEW & UPDATED MAP LAYERS
### Added one new map layer:

- Yehorivka Invasion v4 – VDV vs IMF (New)
 

### Replaced RGF with VDV on the following map layers:

- Black Coast Seed v1 – USMC vs VDV (New flag layout)
- Mutaha Seed v1 – USMC vs VDV
- Tallil Outskirts Seed v2 – CAF vs VDV (New restriction zones)
 

### Replaced RGF with PLANMC on the following map layer:

- Goose Bay Skirmish v1 – CAF vs PLANMC
 

### Replaced PLANMC with PLAAGF on the following map layers:

- Gorodok RAAS v6 – USMC vs PLAAGF
- Harju RAAS v4 – CAF vs PLAAGF
- Manicouagan AAS v4 – USMC vs PLAAGF
- Manicouagan RAAS v13 – CAF vs PLAAGF
- Manicouagan RAAS v15 – USMC vs PLAAGF
- Skorpo RAAS v4 – USMC vs PLAAGF

## SYSTEM & GAMEPLAY UPDATES
 
- The BM21 Grad Rocket Artillery Truck projectiles will now deal 2 types of damage with the same warhead:
– Fragmentation Damage (1m-35m): Good for attacking infantry and light-skinned vehicles. Cannot go through walls.
– Explosive Damage: (1m-10m): Good for attacking vehicles and deployables. Can go through walls.
- Added an open-top PKM variant of the BTR-D APC for the VDV faction, this is currently limited to only a few map layers
- The ZTD05 now has woodland camo on PLAAGF map layers
- Vehicles with a QJY88 MMG will no longer overheat
- The commander PKT RWS on the VDV Sprut SDM1 MGS no longer overheats
- Reduced the respawn timer for the BAF FV510 and FV510 UA IFV from 15 to 10 minutes
- VDV LAT roles have been adjusted to match their intended kit setups:

VDV LAT 01:

    AK12 + 1P87 Reflex Sight
    RPG7v2 + Magnified Optic (2 HEAT rockets)
    RPG7v2 + Magnified Optic (2 frag rockets)

VDV LAT 02:
    
    AK12 + 1P78 Magnified Optic
    RPG7 + Irons (1 HEAT rocket)
    RPG7 + Irons (2 frag rockets)

- Players can now cancel looped emotes by pressing the emote key
- Full-body emotes will now be automatically cancelled when a player leaves the main base area
- Players must now be crouched or prone to use the Pushups emote
- Swapping deployables during the deployable placing animation no longer prevents players from using emotes
- Added SFX to the Star Jump / Jumping Jacks emote
- The keybinds mentioned in the text on the Customize screen will now change to match any custom keybinds that have been set
- Updated the loading screen
- Using foregrips on the AK12 Rifle now slightly reduces the weapon’s recoil
- Updated various images for Discord rich presence integration
- Implemented a debug command (DebugPrintCustomOptions) that can print all the server’s custom options to the console
- Implemented debug commands that allow admins to add/set/remove custom options: AdminSetCustomOption [key value] and AdminRemoveCustomOption [key value]
- The PLANMC and VDV factions are now commented out on the ExcludedFactions.cfg

## GENERAL BUG FIXES

- Fixed a client crash related to applying damage to players
- Fixed a client crash related to changing display settings
- Fixed a bug that prevented the Salute emote from working properly while playing as an INS soldier
- Fixed a bug that allowed players to place deployables in unintended locations, such as floating in the air
- Fixed the water shields on VDV and PLANMC amphibious vehicles to now deploy properly when they enter the water
- Fixed a bug that exposed the CAF Leopard 2A6 MBT’s engine, allowing it to be destroyed by small arms
- Fixed a bug with Commander airstrike SFX cutting out just before the strike occurs
- Fixed mismatched armor values that prevented the VDV Sprut SDM1 MSG, VDV BMD04 IFV, PLANMC Z8J Helicopter, and ZBD2000 vehicles from properly taking damage
- Fixed a bug with the PLANMC’s deployable HMG Bunker being able to rotate outside of the bounds of its opening
- Fixed a bug that caused the ASVAL, AK12, M16A1 and M16A2 rifles to roll continuously on the ground when dropped by a dead player
- Fixed a bug where a player who was switching teams while placing a deployable, would leave behind an invisible copy of the deployable they were placing
- Fixed the reticle on the BAF Woodland FV107 Scimitar to only display a circle (no range markings) when not zoomed in
- Fixed a bug that caused the IMF BM21 Grad Rocket Artillery Truck’s projectile radial damage to be inconsistent
- Fixed broken water splash effects on the VDV BMD-4M IFV
- Fixed the ZTD05 MGS vehicle card list to correctly show the ticket cost (10)
- Fixed a bug that caused the vehicle list to show the availability of single-use vehicles as “1” even when there was more than one available
- Fixed an issue that caused the desert variant of the VDV BTR-DG Kord to show woodland camo when wrecked
- Fixed an issue that caused the woodland camo variant of the PLANMC ZSD05 Amphibious Logi to show the blue digital camo when wrecked
- Fixed a visual issue that caused the nose of the all VDV BMD vehicles to be pointed at too high of an angle when in water
- Fixed a small visual issue with the splash image for the VDV faction
- Fixed a minor issue with players clipping into the gun barrels on the PLANMC ZBL08 IFV, ZBD05 IFV, ZBL08 HJ73C IFV, and ZBD05 HJ73C IFV by going prone while on top of them
- Fixed clipping player viewpoint when standing on the BMD-1M IFV’s gun barrel
- Fixed a visual issue that could make some VDV vehicle tracks look strange up close
- Fixed a bug with the vehicle list that prevented the icon for the PLAAGF ZTD05 MGS from appearing correctly
- Fixed the item selection menu text and icon for the VDV AK12 GP25+1P78
- Fixed a bug that prevented the “Recently Played” badge text from appearing correctly in Simplified Chinese
- Fixed a bug that could prevent custom server options set via ServerConfig/CustomOptions.cfg from properly replicating to clients

## MAP UPDATES & BUG FIXES

### General

Added RGF team image and description to Skorpo RAAS v2 and Yehorivka RAAS v03
- The PLA helicopter on Goose Bay RAAS v2 and Manicouagan RAAS v14 has been changed to the intended Z8-G instead of the Z8-J
- PLANMC and PLAAGF unit symbols and faction descriptions should now match correctly on all layers that use them

### Anvil

AAS v1 – Fixed a bug that could cause a PLA ZSD05 APC to spawn at an angle that rendered it unusable

### Black Coast

Players can no longer clip through the rooftop of a house near the train station
Invasion v5 – PLANMC RHIBs can no longer have their engines started before the end of the staging phase on Invasion v5

### Harju

*RAAS v1 – Updated the vehicle layout for both teams:*


USMC:
    
    1x Transport (6min initial delay)
    
    1x M939 Logi
    
    1x AAVC Logi
    
    2x M1151 M2
    
    2x AAVP
    
    2x LAV25
    
    2x UH1Y (10min initial delay)

RGF:

    1x Transport (6min initial delay)

    1x Kamaz Logi

    1x MTLB Logi

    2x Tigr KORD

    2x BTR82A

    1x BMP2

    2x Mi8 (10min initial delay)

- Players can no longer see and shoot through a rock near the Wheat Farm

### Manicouagan

- Updated layer names for RAAS v01 to v09 with a zero to better support alphabetical name sorting

- Invasion v9 – USMC boats now spawn correctly

- RAAS v14 – Fixed the PLA ZTD05 MGS appearing with blue camo while all other vehicles are woodland

### Narva

- Destruction v1 – Fixed a bug that caused various objective caches at the Quarry to spawn in the air

- Invasion v3 – The Shopping Center is no longer mislabeled as the Old Hospital

- RAAS v2 – Fixed an issue where one of the buildings in the Dog Park Apartments area had no lighting

- RAAS v7 – Updated the RGF vehicle layout to include two Tigr KORDs instead of a Tigr RWS and a BTR80

### Skorpo

- RAAS v2 – Replaced USA with BAF

## SDK UPDATES & BUG FIXES

- Updated mod SDK to v5.1

- File names for Pacific Proving Grounds USMC vs RGF now use RGF instead of RUS

- Tallil Outskirts TC v1’s asset name has been updated to Tallil_TC_v1 to meet the standard of the rest of the Tallil layers

OFFWORLD OUT.