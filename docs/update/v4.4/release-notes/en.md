# SQUAD UPDATE V4.4 RELEASE NOTES

> 页面贡献者：Offworld Industries
> 
> posted on April 18, 2023

Squad 4.4 will bring a few new map layers, new server tags, and will mainly focus on bug fixes, quality of life improvements, and optimizations to the game.

We have added four new map layers and updated one existing map layer:

- Black Coast RAAS v2 – USMC vs IMF (Update)
- Goose Bay Seed v1 — USMC vs PLA 
- Manicouagan RAAS v8 — USA vs IMF
- Manicouagan RAAS v9 — RGF vs IMF
- Mutaha Tanks v1 — MEA vs PLA
 

## SYSTEM & GAMEPLAY UPDATES

- Added the Significance Manager* to Squad

_*See the bottom of the patch notes for more information_

- Standardized faction naming conventions

    AUS -> ADF

    GB -> BAF

    MIL -> IMF

    RUS -> RGF

    This update will cause any mods that rely on these faction templates to fail until the mod is recooked with the new updates

- Made adjustments to Militia kit role inventories
- IMF Marksman 01 – Added 1x deployable Infantry Camo Netting
- IMF Saboteur 01 – Switched primary weapon to AKS74U with 45rnd banana mag
- Server Tagging – Servers can now be tagged with “Rule Tags”
- Rule tags appear on the server preview card and allow server owners to describe the rules that apply to playing on that server. Server owners can learn more about this feature here: [[URL LINK]](https://squad.fandom.com/wiki/server_configuration#rule_list)
- Server Tagging – Added automatic language detection
- The game will automatically detect your language based on your Steam settings and apply that to the quick play feature. If you have already changed your language setting in Squad, this will not impact you
- Full servers with queues will no longer appear while using the quick play feature
- Added the RKG-3 Anti Tank Grenade to the INS Raider kit role inventory
- Removed landmines from the BAF and CAF Engineer kit roles
- Reduced the number of frag grenades in the LAT 02 kit role inventory from two to one for the ADF, BAF, CAF, MEA, RGF, USA, and USMC factions
- Added a deployable camouflage net to the INS marksman kit role inventory
- Reduced recoil energy on the PLA ZBD04A IFV main cannon
- Increased the firing rate of the BM21 Grad Rocket Artillery Truck from 0.5 to 0.25 and the air burst from 1m to 2m
- Increased FOB bleed out time to 75 seconds and decreased the health required for a FOB to stop bleeding to 50 hp
- Configured both sides of the IMF Camo Net Wall to be semi-transparent when in very close proximity
- Swapped the ACOG M2 Tripod/Bunker with a new Iron Sight M2 Tripod/Bunker Emplacement on all CAF and ADF map layers
- Players no longer suffer a speed penalty when dragging a body
- Increased the max range for HAB disable

HAB spawn disable range has been increased to 90 meters. When players enter the proximity of an enemy HAB, its spawnpoint will become disabled based on the scale of players and range to the enemy HAB:

    2 players at 20 meters

    3 players at 30 meters

    4 players at 40 meters

    5 players at 50 meters

    6 players at 60 meters

    7 players at 70 meters

    8 players at 80 meters

    9 players at 90 meters

- The M1937 mortar emplacement is now easier to enter
- Added an AutoScroll feature to the main menu UI
- The emote keybind can now be set separately from the zeroing keybind
- Players can now activate their most recently played emote or gesture by pressing the emote key (vs. holding it to open up the radial menu)

## GENERAL BUG FIXES
- Fixed a client crash
- Made several improvements to the performance of the main menu
- Fixed a bug that could prevent players from reconnecting after being disconnected from a queue
- Fixed an issue that could cause server tags to appear smaller than intended in the Server Details panel
- IMF Dirt Crates can no longer be stacked on top of one another
- Players can no longer build on top of the IMF Observation Tower
- The IMF Hull Down Fortification can no longer be stacked on top of itself
- Fixed a bug that caused the IMF Infantry kit role to be able to place 4 camouflage nettings instead of the intended 3
- Fixed an issue that caused country codes to be translated incorrectly
- The MT-LB PKT APC is now correctly labelled on layers where it is present
- Emplacements can no longer be placed inside rocks
- Fixed an issue that caused the plastic shell of the IED detonator phone to disappear at certain angles
- Fixed a bug that caused the IMF Modern Technical to appear white instead of camouflaged when wrecked
- 30-40mm HE rounds now have their intended impact sound effects instead of sounding like grenades
- The IMF Saboteur kit role description has been corrected to reflect that the role is not equipped with IEDs
- Fixed a bug that could cause some helicopters to be instantly destroyed upon spawning
- Fixed an issue that could cause the rearm icon on the driver HUD of the BM21 Grad Rocket Artillery Truck to flash sporadically and not display correctly when rearming
- Fixed a consistency error relating to tags in the server.cfg
- The wreck of the Ural ZU23 Anti-Air Truck now appears as intended
- Fixed a bug that caused the defending team in a match of Insurgency to lose 11 tickets when an objective is destroyed
- Players on a defending team will now hear the intended voiceover when a point is neutralized
- Quick play filter settings now save when closing the settings menu with any input
- The quick play feature will no longer show the server a player is currently connected to
- Fixed a color distortion that appeared when operating the IMF ZiS3 Field Gun
- The PLA HAT launcher’s 3rd person equip animation now appears as intended
- Fixed an issue where the wrapped sleeves on a US Army soldier’s uniform would clip into their arms during certain weapon-holding animations
- Fixed an issue where the arms of US Army Soldiers would look strange during weapon switch animations 
- Fixed an issue where textures in the UI could appear corrupted when changing servers
- Fixed an issue where players were unable to switch teams directly upon starting a server
- The “Press F to drag soldier” prompt should now always reliably appear when dragging a body is an option
 

## MAP UPDATES & BUG FIXES

### General

- Reduced the Mortar limit to 1 per FOB on Chora, Kokan, Logar, and Sumari
- Players now take appropriate fall damage when jumping into the water on flooded map layers

### Anvil

- Players can no longer go outside of the drawn map boundary on AAS v2

### Belaya

- Fixed an issue that caused players to see an unending loading screen after switching to AAS v2

### Fallujah

- Fixed an issue that caused vehicles to explode when driving into a certain area

### Goose Bay

- Adjusted the name of a few gameplay layers for consistency
### Manicouagan

- Removed the IMF faction’s ability to place the ZIS3 Emplacement on Seed v1
- Made several improvements to the minimap

### Mutaha

- The Seed v1 map location has been moved so that the entire match now takes place on the central island with no river crossings in play. This will provide a more streamlined experience for more relaxed play during seeding.
- The ticket legend on Seed v1 has been updated with the correct information regarding seed mode
- Fixed an issue that caused the ground on Sunny lighting layers to appear white in places

### Skorpo

- Fixed an issue that caused HAB camo netting to sometimes display the incorrect landscape color for users that disconnect and reconnect to a server

### Tallil Outskirts

- Made several optimization improvements
- Updated minimap to show tunnel entrances but not the tunnels themselves
- Fixed an issue where metal beams at the hangar had no projectile collisions and played no VFX when weapons hit by a weapon
- Closed a gap in a wall at I4-7-2
 
## SDK UPDATES & BUG FIXES
- Updated mod SDK to v4.4
- Updated mod versioning to v4.4. This should not cause any incompatibility issues.
- Fixed an issue where pak files were not being generated properly resulting in all data being chunked into one file

*The Significance Manager provides a framework for us to determine if an object is significant to you. It does this by comparing objects inside of your field of view and ranking them based on criteria we define (such as distance to you). The engine then determines the significance of the objects based on those rules and updates the tick rate of each of those objects. Previously, objects like players or vehicles that were behind you would continue to tick even if you could not see them. Objects that are not in your field of view or have been ranked to have no significance will no longer tick. We’ve already noticed some performance improvements from our current integration and we’ll continue to iterate on this system in future updates. If you want to learn more, you can read Epic’s documentation on the feature [here](https://docs.unrealengine.com/4.27/en-us/testingandoptimization/performanceandprofiling/significancemanager/).

OFFWORLD OUT.