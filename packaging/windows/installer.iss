#define MyAppName "RAG Finance"
#define MyAppVersion "1.0.0"
#define MyAppExeName "RAG-Finance.exe"

[Setup]
AppId={{A83E621E-4B76-47A1-BA9A-D074C4F78D7B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\RAG Finance
DefaultGroupName=RAG Finance
UninstallDisplayIcon={app}\{#MyAppExeName}
OutputDir=..\..\dist\installer
OutputBaseFilename=RAG-Finance-Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "..\..\dist\RAG-Finance\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\RAG Finance"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\RAG Finance"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch RAG Finance"; Flags: nowait postinstall skipifsilent
