<#

  Programm zur Sicherung (Backup) und Rücksicherung der PlaSeC-Server (VCC)

  Aufruf des Programms:

	perl Backup_Recovery_VCC.pl -i <ini-Datei>

  Erstellt von Kirsten Dresbach (BAS42) am 11.03.2015


#>
[CmdletBinding()]
param(
    [String] $iniFile = (Join-Path $PSScriptRoot "Backup_Recovery_VCC.ini"),
    [String] $logFile = (Join-Path $PSScriptRoot "$(Get-Date -format 'yyyyyMMdd_HHmmss')_Backup_Recovery_VCC.log"),
    [ValidateSet("backup", "recovery")][String] $aktion = "backup",
    [String] $umgebung = "",
    [String] $server = "",
    [String] $modulepath = (Join-Path $PSScriptRoot "Modules")
)

Set-StrictMode -Version 3.0

#-- IMPORT ----------------------------------------------------------------------
Import-Module PsIni

Import-Module (Join-Path $modulepath "BA-Tools") -DisableNameChecking -Force
Import-Module (Join-Path $modulepath "Copy-File") -DisableNameChecking -Force
Import-Module (Join-Path $modulepath "Restore-Server") -DisableNameChecking -Force
Import-Module (Join-Path $modulepath "Backup-Server") -DisableNameChecking -Force

#-- MAIN --------------------------------------------------
# Steuerflags für backup/recovery True/False
$recovery = !($backup = if($aktion -eq "backup") { $true } else { $false })

if($recovery -and $server -eq "") {
    Write-Message -logFile $logFile "Es wurde die Aktion Recovery ausgewaehlt aber kein Server mit der Option server mitgegeben"
    Write-Message -logFile $logFile "Daher wird das Programm beendet";
	exit(1)
}

$serverListePath = Get-ServerListePath -appPath $PSScriptRoot -umgebung $umgebung
$iniDaten = Get-IniContent $iniFile
$backupVerz = $iniDaten["Konfig"]["BackupVerz"]

$msg =
    "# --------------------------------------------------------------------" + $EOL +
    "#  Programmstart durch: $env:USERNAME in $env:USERDOMAIN" + $EOL +
    "#  auf: $env:COMPUTERNAME" + $EOL +
    "#  Umgebung: $umgebung" + $EOL +
	"#  Server: $server" + $EOL +
    "#  Inidatei: $iniFile" + $EOL +
    "#  Backupverzeichnis: $backupVerz" + $EOL +
    "#  Serverliste: $serverListePath" + $EOL +
    "#  Logfile: $logFile" + $EOL +
    "#  am: $(Get-Zeit)" + $EOL +
    "# --------------------------------------------------------------------" + $EOL
Write-Message -suppressTime -logFile $logFile $msg

Write-Message -logFile $logFile "Serverliste wird eingelesen"
$serverInfos = Read-ServerListe $serverListePath

Write-Verbose $serverInfos["TypeToNames"].Keys
Write-Verbose $serverInfos["NameToTypes"].Keys

if ($backup){
	Backup-Server $serverInfos["TypeToNames"] $iniDaten $logFile
} else {
    Restore-Server $serverInfos["NameToTypes"] $backupVerz $server $logFile
}

Write-Message -logFile $logFile "------------- Verarbeitung beendet ------------"

exit(0)
