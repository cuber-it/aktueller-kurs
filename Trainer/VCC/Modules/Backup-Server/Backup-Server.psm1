Set-StrictMode -Version 3.0

$SERVER_TYPES = @('VCC-Core-ERMS', 'VCC-Services', 'VCC-IVR-Interaction', 'VCC-Web', 'VCC-Supplement')
$FOR_TESTING = ".\Server\"

function Backup-Server {
    param (
        [Parameter(Mandatory)][HashTable] $serverInfos,
		[Parameter(Mandatory)][System.Collections.Specialized.OrderedDictionary] $iniData,
		[Parameter(Mandatory)][String] $logFile
    )

    Write-Message -logFile $logFile "Es wird das Backup fuer alle Server gestartet"

    ForEach($serverType in $SERVER_TYPES) {
		Write-Message -logFile $logFile "######### Es wird der Typ $serverType bearbeitet#########"
	 	ForEach($server in ($serverInfos[$serverType])){
	 		Write-Message -logFile $logFile "Jetzt wird der Server $server bearbeitet"
			ForEach($item in $iniData.$serverType.GetEnumerator()) {
				ForEach($filter in $item.value.split(" ")) {
					$quelle = "$FOR_TESTING\$server\" + $item.key + "\" + $item.value
					$ziel = $iniData.Konfig.BackupVerz + "\" + $serverType + "\" + $server + "\"
					Get-ChildItem $quelle | ForEach {
						Copy-File $_ (Join-Path $ziel $_.DirectoryName)
					}
				}


				#$filter = $item.value.split(" ")
				#Execute-FileCopyRecursive $quelle $ziel $filter $logFile
			}
	# 		ForEach($datei in $iniData[$tempType].Keys) {
	# 			switch -Regex ($datei) {
	# 	 			"\+" {
	# 					Write-Host "1 $datei"
	# 	 			}
	# 	 			"\#" {
	# 					Write-Host "2 $datei"
	# 	 			}
	# 	 			"Regfile" {
	# 					Write-Host "3 $datei"
	# 	 			}
	# 				 "\%" {
	# 					Write-Host "4 $datei"
	# 	 			}
	# 				 "\&" {
	# 					Write-Host "5 $datei"
	# 	 			}
	# 	 			default {
	# 					Write-Host "D $datei"
	# 	 			}
	# 	 		}
	# 		}
	# 	# 		if($dateien =~ /\+/){
	# 	# 			Write-Message -logFile $logFile "Sonderbehandlung wegen Mandantenordner\n";

	# 	# 			@TMP_VERZ = split(/\+/,$DATEIEN);
	# 	# 			$dir = "$TMP_VERZ[0]";
	# 	# 			chomp(@TMP_VERZ_Mandant = `cmd /c dir "$dir*" /B /s`);
	# 	# 			ForEach($tmpVerz_Mandant in $tmpVerzeichnisse_Mandant){
	# 	# 				$dateien = $TMP_VERZ_Mandant . $TMP_VERZ[1];
	# 	# 				$unterverzeichnis = $DATEIEN;
	# 	# 				$unterverzeichnis =~s /C\$\\//i;
	# 	# 				$unterverzeichnis =~s /\\\\$TEMP_SRV//i;

	# 	# 				if(!(Test-Path $dateien)) {
	# 	# 					# `C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n`;
	# 	# 					Run-RoboCopy
	# 	# 				}
	# 	# 			}#ENDE foreach  $TMP_VERZ_Mandant (@TMP_VERZ_Mandant)
	# 	# 		}elsif($DATEIEN =~ /\#/){
	# 	# 			Write-Message -logFile $logFile "Sonderbehandlung wegen InstanceID-Ordner\n";

	# 	# 			@TMP_VERZ = split(/\#/,$DATEIEN);
	# 	# 			$dir = "$TMP_VERZ[0]";
	# 	# 			chomp(@TMP_VERZ_InstanceID = `cmd /c dir "$dir*" /B /a:D`);
	# 	# 			foreach  $TMP_VERZ_InstanceID (@TMP_VERZ_InstanceID){
	# 	# 				$DATEIEN = $TMP_VERZ[0] . $TMP_VERZ_InstanceID . $TMP_VERZ[1];
	# 	# 				if ($DATEIEN =~ /\%/){
	# 	# 					Write-Message -logFile $logFile "zweite Instance-ID ermitteln\n";

	# 	# 					@TMP_VERZ2 = split(/\%/,$DATEIEN);
	# 	# 					$dir = "$TMP_VERZ2[0]";
	# 	# 					chomp(@TMP_VERZ_InstanceID2 = `cmd /c dir "$dir*" /B /a:D`);
	# 	# 					# $status = "<<<DEBUG>>>>\nDATEIEN: $DATEIEN\nIDs:@TMP_VERZ_InstanceID2\nREST: $TMP_VERZ2[1]\n<<<DEBUG>>>>\n";
	# 	# 					# &druck();
	# 	# 					foreach  $TMP_VERZ_InstanceID2 (@TMP_VERZ_InstanceID2){
	# 	# 						$DATEIEN = $dir . $TMP_VERZ_InstanceID2 . $TMP_VERZ2[1];
	# 	# 					}
	# 	# 				}
	# 	# 				$unterverzeichnis = $DATEIEN;
	# 	# 				$unterverzeichnis =~s /C\$\\//i;
	# 	# 				$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
	# 	# 				if(!(Test-Path $DATEIEN)) {
	# 	# 					# C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
	# 	# 					Run-RoboCopy
	# 	# 				}
	# 	# 			}
	# 	# 		}elsif ($DATEIEN =~ /Regfile/){
	# 	# 			Write-Message -logFile $logFile "Es wird ein Regfile gesichert\n";

	# 	# 			$reg = `cmd /c reg query \\\\$TEMP_SRV\\$einzel /s`;
	# 	# 			Write-Message -logFile $logFile $reg;

	# 	# 			$reg_dat = "$backupverz\\$TEMP_TYP\\$TEMP_SRV"."_reg.txt";
	# 	# 			open (REG, ">$reg_dat");
	# 	# 			print REG "$reg";
	# 	# 			close (REG);
	# 	# 		}else{
	# 	# 			$unterverzeichnis = $DATEIEN;
	# 	# 			$unterverzeichnis =~s /C\$\\//i;
	# 	# 			$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
	# 	# 			$unterverzeichnis =~s /\&\$TEMP_SRV//i;
	# 	# 			if(!(Test-Path $DATEIEN)) {
	# 	# 				# "C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
	# 	# 				Run-RoboCopy
	# 	# 			}
	# 	# 		}
	# 	 	}
	 	}
	}
}
