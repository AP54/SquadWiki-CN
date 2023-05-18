SET /p STEAMCMD=SteamCMD_install_dir:
SET /p INSTALL_DIR=SDS_install_dir:
%STEAMCMD% +@ShutdownOnFailedCommand 1 +@NoPromptForPassword 1 +force_install_dir %INATALL_DIR% +login anonymous +app_update 403240 validate +quit
pause