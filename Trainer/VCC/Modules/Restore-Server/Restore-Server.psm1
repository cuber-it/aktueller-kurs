function Restore-Server {
    param(
        [Parameter(Mandatory)][hashtable] $serverInfos,
		[Parameter(Mandatory)][String] $backupVerz,
        [Parameter(Mandatory)][String] $server,
        [Parameter(Mandatory)][String] $logFile
    )
    Write-Message -logFile $logFile "Es wird ein Recovery fuer den Server $server von $backupVerz eingespielt"
    Write-Message -logFile $logFile "Es wird der Servertyp von $server ermittelt"

	$typ = $serverInfos[$server]

	Write-Message -logFile $logFile "Als Servertyp wurde $typ erkannt"
	Write-Message -logFile $logFile "Die Sicherungen werden nun zurueck gespielt"

    $robocopy, $options = Get-RoboCopyCommand "$backupVerz\$typ\$server" "\\$server\c$\" "*.*"

    Write-Message -logFile $logFile "Kommando: $robocopy $options"

    (&$robocopy $options 2>&1) | Write-Message -logFile $logFile -suppressTime

}
