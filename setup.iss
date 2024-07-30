[Setup]
AppName=SafeFromYT
AppVersion=0.1
DefaultDirName={pf}\SafeFromYT
DefaultGroupName=SafeFromYT
OutputBaseFilename=SafeFromYT_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "build\exe.win-amd64-3.12\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SafeFromYT"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,SafeFromYT}"; Flags: nowait postinstall skipifsilent

