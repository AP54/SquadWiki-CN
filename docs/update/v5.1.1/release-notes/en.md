# SQUAD HOTFIX 5.1.1 RELEASE NOTES

> 页面贡献者：Offworld Industries
> 
> 原文章：[SQUAD HOTFIX 5.1.1 RELEASE NOTES](https://joinsquad.com/2023/08/03/squad-hotfix-5-1-1-release-notes/)
>
> 发布时间：2023/08/03

Squad 5.1.1 hotfix is now deployed, here is the list of the fixes addressed in the update:

## **General Bug Fixes**

- Server performance improvements

## **Map Updates & Bug Fixes**

## Pacific Proving Grounds v2

- Fixed an issue that prevented grass foliage from appearing on all PPG v2 layers
- Fixed a bug that caused map markers placed on the deployment screen to show up in a place different than where the player clicked while placing them
- Players can no longer clip into rock meshes

## **Server Performance**
- Addressed an issue where Server Performance was impacted due to replicating more often than it needed to. Replicating an actor would cause all replicated properties of that actor to replicate again, regardless if it needed to or not.
- Fixed an issue where server side animation ticks weren’t being throttled as intended, causing the server to spend more time handling incoming move requests than intended.

OFFWORLD OUT.