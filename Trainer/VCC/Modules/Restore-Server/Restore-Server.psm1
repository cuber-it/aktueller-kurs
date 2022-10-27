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

    $status = Copy-FileRecursive "$backupVerz\$typ\$server" "\\$server\c$\" "*.*" -logFile $logFile
    Write-Message -logFile $logFile "Ergebnis: $status"
}
