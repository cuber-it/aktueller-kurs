function Restore-Server {
    param(
        [Parameter(Mandatory)][String]$server,
		[Parameter(Mandatory)][System.Collections.Specialized.OrderedDictionary] $iniData
    )
    Write-Message -logFile $logFile "Es wird ein Recovery fuer den Server $server eingespielt"
    Write-Message -logFile $logFile "Es wird der Servertyp von $server ermittelt"

	$typ = $SERVERTYP[$server]

	Write-Message -logFile $logFile "Als Servertyp wurde $typ erkannt"
	Write-Message -logFile $logFile "Die Sicherungen werden nun zurueck gespielt"

	$backupverz = $iniData["Konfiguration"]["BackupVerz"]
    $source = "$backupverz\$typ\$server"
    $destination = "\\$server\c$\"
    $file = "*.*"


    $cmd = Get-RoboCopyCommand $source $destination $file
    Write-Message -logFile $logFile "Kommando: ROBOCOPY $(cmd)"

    $status = Execute-RoboCopyCommand $cmd
	Write-Message -logFile $logFile "Status: "
    Write-Message -logFile $logFile $status -suppressTime
}
