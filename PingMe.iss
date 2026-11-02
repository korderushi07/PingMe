#define MyAppName "PingMe"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "PingMe"
#define MyAppExeName "PingMe.exe"

[Setup]
AppId={{A83C2F71-6D91-4B5E-9F12-7C8A41D63B20}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\PingMe
DefaultGroupName=PingMe
UninstallDisplayIcon={app}\{#MyAppExeName}
OutputDir=installer
OutputBaseFilename=PingMe-Setup-v0.1.0
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Files]
Source: "dist\PingMe\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\PingMe"; Filename: "{app}\PingMe.exe"
Name: "{autodesktop}\PingMe"; Filename: "{app}\PingMe.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\PingMe.exe"; Description: "Launch PingMe"; Flags: postinstall nowait skipifsilent
