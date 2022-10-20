

function Run-RoboCopy {
    param(
        $source,
        $destination,
        $file
    )
    # `C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n`;
	$cmd = Get-RoboCopyCommand $source $destination $file
    Write-Message -logFile $logFile "Kommando: ROBOCOPY $cmd"
    $status = Execute-RoboCopyCommand $cmd
    Write-Message -logFile $logFile "Status: "
    Write-Message -logFile $logFile $status -suppressTime
}

function Prepare-Dateien {
    param(

    )
}

function Backup-Server {
    param (
        [Parameter(Mandatory)][String] $serverListePath,
		[Parameter(Mandatory)][System.Collections.Specialized.OrderedDictionary] $iniData
    )


    Write-Message -logFile $logFile "Es wird das Backup fuer alle Server gestaretet"
    Write-Message -logFile $logFile "Serverliste wird eingelesen"

    $serverListen = Read-ServerListe $serverListePath
    $tempTypes = @('VCC-Core-ERMS', 'VCC-Services', 'VCC-IVR-Interaction', 'VCC-Web', 'VCC-Supplement')

    Write-Host $serverListen["TypeToNames"].Keys
    Write-Host $serverListen["NameToTypes"].Keys

    ForEach($tempType in $tempTypes) {
		Write-Message -logFile $logFile "#########Es wird der Typ $tempType bearbeitet#########"

		ForEach($tempSrv in ($serverListe["TypeToNames"][$tempType])){
			Write-Message -logFile $logFile $EOL +  "Jetzt wird der Server $tempSrv bearbeitet" + $EOL

		# 	ForEach($dateien in Get-INIKeyList($ini, $tempType)) {
		# 		$einzel = Get-IniValue $ini $tempType $dateien" "*.*"
		# 		$DATEIEN =~ s/C:/\\\\$TEMP_SRV\\C\$/i;
		# 		$DATEIEN =~s /\&/$TEMP_SRV/i;
		# 		switch -Regex ($dateien) {
		# 			"\+" {

		# 			}
		# 			"\#" {

		# 			}
		# 			"Regfile" {

		# 			}
		# 			default {

		# 			}
		# 		}
		# 		if($dateien =~ /\+/){
		# 			Write-Message -logFile $logFile "Sonderbehandlung wegen Mandantenordner\n";

		# 			@TMP_VERZ = split(/\+/,$DATEIEN);
		# 			$dir = "$TMP_VERZ[0]";
		# 			chomp(@TMP_VERZ_Mandant = `cmd /c dir "$dir*" /B /s`);
		# 			ForEach($tmpVerz_Mandant in $tmpVerzeichnisse_Mandant){
		# 				$dateien = $TMP_VERZ_Mandant . $TMP_VERZ[1];
		# 				$unterverzeichnis = $DATEIEN;
		# 				$unterverzeichnis =~s /C\$\\//i;
		# 				$unterverzeichnis =~s /\\\\$TEMP_SRV//i;

		# 				if(!(Test-Path $dateien)) {
		# 					# `C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n`;
		# 					Run-RoboCopy
		# 				}
		# 			}#ENDE foreach  $TMP_VERZ_Mandant (@TMP_VERZ_Mandant)
		# 		}elsif($DATEIEN =~ /\#/){
		# 			Write-Message -logFile $logFile "Sonderbehandlung wegen InstanceID-Ordner\n";

		# 			@TMP_VERZ = split(/\#/,$DATEIEN);
		# 			$dir = "$TMP_VERZ[0]";
		# 			chomp(@TMP_VERZ_InstanceID = `cmd /c dir "$dir*" /B /a:D`);
		# 			foreach  $TMP_VERZ_InstanceID (@TMP_VERZ_InstanceID){
		# 				$DATEIEN = $TMP_VERZ[0] . $TMP_VERZ_InstanceID . $TMP_VERZ[1];
		# 				if ($DATEIEN =~ /\%/){
		# 					Write-Message -logFile $logFile "zweite Instance-ID ermitteln\n";

		# 					@TMP_VERZ2 = split(/\%/,$DATEIEN);
		# 					$dir = "$TMP_VERZ2[0]";
		# 					chomp(@TMP_VERZ_InstanceID2 = `cmd /c dir "$dir*" /B /a:D`);
		# 					# $status = "<<<DEBUG>>>>\nDATEIEN: $DATEIEN\nIDs:@TMP_VERZ_InstanceID2\nREST: $TMP_VERZ2[1]\n<<<DEBUG>>>>\n";
		# 					# &druck();
		# 					foreach  $TMP_VERZ_InstanceID2 (@TMP_VERZ_InstanceID2){
		# 						$DATEIEN = $dir . $TMP_VERZ_InstanceID2 . $TMP_VERZ2[1];
		# 					}
		# 				}
		# 				$unterverzeichnis = $DATEIEN;
		# 				$unterverzeichnis =~s /C\$\\//i;
		# 				$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
		# 				if(!(Test-Path $DATEIEN)) {
		# 					# C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
		# 					Run-RoboCopy
		# 				}
		# 			}
		# 		}elsif ($DATEIEN =~ /Regfile/){
		# 			Write-Message -logFile $logFile "Es wird ein Regfile gesichert\n";

		# 			$reg = `cmd /c reg query \\\\$TEMP_SRV\\$einzel /s`;
		# 			Write-Message -logFile $logFile $reg;

		# 			$reg_dat = "$backupverz\\$TEMP_TYP\\$TEMP_SRV"."_reg.txt";
		# 			open (REG, ">$reg_dat");
		# 			print REG "$reg";
		# 			close (REG);
		# 		}else{
		# 			$unterverzeichnis = $DATEIEN;
		# 			$unterverzeichnis =~s /C\$\\//i;
		# 			$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
		# 			$unterverzeichnis =~s /\&\$TEMP_SRV//i;
		# 			if(!(Test-Path $DATEIEN)) {
		# 				# "C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
		# 				Run-RoboCopy
		# 			}
		# 		}
		# 	}
		}
	}
}
