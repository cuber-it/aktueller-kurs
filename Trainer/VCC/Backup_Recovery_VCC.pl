# --------------------------------------------------------------------
#
#  Programm zur Sicherung (Backup) und R�cksicherung der PlaSeC-Server (VCC)
#
#  Aufruf des Programms:
#
#	perl Backup_Recovery_VCC.pl -i <ini-Datei>
#
#  Erstellt von Kirsten Dresbach (BAS42) am 11.03.2015
#
# --------------------------------------------------------------------
use Getopt::Std;
use FindBin;
use lib $FindBin::Bin;
use LibINI;
use Win32::TieRegistry;
use Time::localtime;
use Time::Local;

@TEMP_TYP = ('VCC-Core-ERMS', 'VCC-Services', 'VCC-IVR-Interaction', 'VCC-Web', 'VCC-Supplement');
$ini = "";
$server = "";

$skript="Backup_Recovery_VCC.pl";
my $AppPath=$FindBin::Bin;
$AppPath=~s/\//\\/g;
$log =$AppPath."\\Backup_Recovery_VCC.log";

open (LOG, ">>$log");

my( $options ) = 'i:s:u:brd';
# --------------------------------------------------------------------
#  Kommandozeile auswerten
# --------------------------------------------------------------------
getopts( $options ) || &Usage();
$ini = $opt_i if( $opt_i );
$debug = "TRUE" if( $opt_d );
$backup = "TRUE" if( $opt_b );
$recovery = "TRUE" if( $opt_r );
$umgebung = $opt_u if( $opt_u );
$server = $opt_s if( $opt_s );

$backupverz = &INIValueGet( $ini, "Konfig", "Backup", "$AppPath\\Backup" );

$computer = $ENV{COMPUTERNAME};
$user = $ENV{USERNAME};
$userdom = $ENV{USERDOMAIN};

if ($ini eq ""){$ini = $AppPath. "\\Backup_Recovery_VCC.ini"};
if ($umgebung =~ /edst/i){
	$server_liste = $AppPath. "\\_QUTest-e_Liste.txt";
}elsif ($umgebung =~ /idst/i){
	$server_liste = $AppPath. "\\_QUTest-i_Liste.txt";
}else{
	$server_liste = $AppPath. "\\_QUTest-d_Liste.txt";
}#ENDE if ($umgebung =~ /edst/i)


$zeit = &Zeit("NURZEIT");
$status = "# --------------------------------------------------------------------\n";
&druck();
$status = "#  Programmstart durch: $user in $userdom\n";
&druck;
$status = "#  auf: $computer\n";
&druck();
$status = "#  inidatei: $ini\n";
&druck();
$status = "#  Backupverzeichnis: $backupverz\n";
&druck();
$status = "#  Serverliste: $server_liste\n";
&druck();
$status = "#  am: $zeit\n";
&druck();
$status = "# --------------------------------------------------------------------\n\n";
&druck();

$status = "Serverliste wird eingelesen\n";
&druck();
open (SRV, "$server_liste");
chomp(@SRV=<SRV>);
close (SRV);

foreach $SRV (@SRV){
	if ($SRV =~ /^n\d{7}/){
		$SRV =~ s/\t.{9}//i;
		@SRV_Teil = split(/ /,$SRV);
		print "$SRV_Teil[1]  ->   $SRV_Teil[0]\n";
		push(@{$Server{$SRV_Teil[1]}},$SRV_Teil[0]);
		$SERVERTYP{$SRV_Teil[0]} = $SRV_Teil[1];
	}#ENDE if ($SRV =~ /^n\d{7}/)
}#ENDE foreach $SRV (@SRV)

if ($backup eq "TRUE"){
	$status = "Es wird das Backup f�r alle Server gestaretet\n";
	&druck();
	&backup();
}elsif ($recovery eq "TRUE"){
	if ($server eq ""){
		$status = "Es wurde die Aktion Recovery ausgew�hlt aber kein Server mit der Option -s mitgegeben\n";
		&druck();
	}else{
		$status = "Es wird ein Recovery f�r den Server $server eingespielt\n";
		&druck();
		&recovery();
	}#ENDE if ($server eq "")
}else{
	$status = "Es wurde keine Aktion ausgew�hlt. Daher wird das Programm beendet\n";
	&druck();
}#ENDE if ($backup eq "TRUE")


$zeit = &Zeit("NURZEIT");
$status = "\n# --------------------------------------------------------------------\n";
&druck();
$status = "# ENDE um $zeit\n";
&druck();
$status = "# --------------------------------------------------------------------\n";
&druck();


sub backup(){
	foreach $TEMP_TYP (@TEMP_TYP){
		$status = "\n#########Es wird der Typ $TEMP_TYP bearbeitet#########\n";
		&druck();
		foreach $TEMP_SRV (@{$Server{$TEMP_TYP}}){
			$status = "\nJetzt wird der Server $TEMP_SRV bearbeitet\n";
			&druck();
			@DATEIEN = INIKeyListGet( $ini, $TEMP_TYP );
			foreach $DATEIEN (@DATEIEN){
				$einzel = &INIValueGet( $ini, "$TEMP_TYP", "$DATEIEN", "*.*" );
				$DATEIEN =~ s/C:/\\\\$TEMP_SRV\\C\$/i;
				$DATEIEN =~s /\&/$TEMP_SRV/i;
				if ($DATEIEN =~ /\+/){
					$status = "Sonderbehandlung wegen Mandantenordner\n";
					&druck();
					@TMP_VERZ = split(/\+/,$DATEIEN);
					$dir = "$TMP_VERZ[0]";
					chomp(@TMP_VERZ_Mandant = `cmd /c dir "$dir*" /B /s`);
					foreach  $TMP_VERZ_Mandant (@TMP_VERZ_Mandant){
						$DATEIEN = $TMP_VERZ_Mandant . $TMP_VERZ[1];
						$unterverzeichnis = $DATEIEN;
						$unterverzeichnis =~s /C\$\\//i;
						$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
						unless (-e $DATEIEN){next;}
						$status = "C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
						&druck();
						$status = `C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n`;
						&druck();
					}#ENDE foreach  $TMP_VERZ_Mandant (@TMP_VERZ_Mandant)
				}elsif($DATEIEN =~ /\#/){
					$status = "Sonderbehandlung wegen InstanceID-Ordner\n";
					&druck();
					@TMP_VERZ = split(/\#/,$DATEIEN);
					$dir = "$TMP_VERZ[0]";
					chomp(@TMP_VERZ_InstanceID = `cmd /c dir "$dir*" /B /a:D`);
					foreach  $TMP_VERZ_InstanceID (@TMP_VERZ_InstanceID){
						$DATEIEN = $TMP_VERZ[0] . $TMP_VERZ_InstanceID . $TMP_VERZ[1];
						if ($DATEIEN =~ /\%/){
							$status = "zweite Instance-ID ermitteln\n";
							&druck();
							@TMP_VERZ2 = split(/\%/,$DATEIEN);
							$dir = "$TMP_VERZ2[0]";
							chomp(@TMP_VERZ_InstanceID2 = `cmd /c dir "$dir*" /B /a:D`);
							# $status = "<<<DEBUG>>>>\nDATEIEN: $DATEIEN\nIDs:@TMP_VERZ_InstanceID2\nREST: $TMP_VERZ2[1]\n<<<DEBUG>>>>\n";
							# &druck();
							foreach  $TMP_VERZ_InstanceID2 (@TMP_VERZ_InstanceID2){
								$DATEIEN = $dir . $TMP_VERZ_InstanceID2 . $TMP_VERZ2[1];
							}#ENDE foreach  $TMP_VERZ_InstanceID (@TMP_VERZ_InstanceID)
						}#ENDE if ($TMP_VERZ[2] ne "")
						unless (-e $DATEIEN){next;}
						$unterverzeichnis = $DATEIEN;
						$unterverzeichnis =~s /C\$\\//i;
						$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
						$status = "C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
						&druck();
						$status = `C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n`;
						&druck();
					}#ENDE foreach  $TMP_VERZ_Mandant (@TMP_VERZ_Mandant)
				}elsif ($DATEIEN =~ /Regfile/){
					$status = "Es wird ein Regfile gesichert\n";
					&druck();
					$reg = `cmd /c reg query \\\\$TEMP_SRV\\$einzel /s`;
					$status = $reg;
					&druck();
					$reg_dat = "$backupverz\\$TEMP_TYP\\$TEMP_SRV"."_reg.txt";
					open (REG, ">$reg_dat");
					print REG "$reg";
					close (REG);
				}else{
					$unterverzeichnis = $DATEIEN;
					$unterverzeichnis =~s /C\$\\//i;
					$unterverzeichnis =~s /\\\\$TEMP_SRV//i;
					$unterverzeichnis =~s /\&\$TEMP_SRV//i;
					unless (-e $DATEIEN){next;}
					$status = "C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n";
					&druck();
					$status = `C:\\Windows\\System32\\Robocopy.exe \"$DATEIEN\" \"$backupverz\\$TEMP_TYP\\$TEMP_SRV$unterverzeichnis\" $einzel /COPY:DAT /PURGE /NP /R:3 /W:3\n`;
					&druck();
				}#ENDE if ($DATEIEN =~ /MANDANT/)
			}#ENDE foreach $paket (@instreihenfolge)
		}#ENDE foreach $TEMP_SRV (@{$Server{VCC-Core-ERMS}})
	}#ENDE foreach $TEMP_TYP (@TEMP_TYP){
}#ENDE sub backup(){

sub recovery(){
	$status = "Es wird der Servertyp von $server ermittelt\n";
	&druck();
	$typ = $SERVERTYP{$server};
	$status = "Als Servertyp wurde $typ erkannt\n";
	&druck();
	$status = "Die Sicherungen werden nun zur�ck gespielt\n";
	&druck();
	$status = "C:\\Windows\\System32\\Robocopy.exe \"$backupverz\\$typ\\$server\" \"\\\\$server\\c\$\" *.* /COPY:DAT /E /NP /R:3 /W:3\n";
	&druck();
	$status = `C:\\Windows\\System32\\Robocopy.exe \"$backupverz\\$typ\\$server\" \"\\\\$server\\c\$\" *.* /COPY:DAT /E /NP /R:3 /W:3`;
	&druck();
}#ENDE sub recovery()

# --------------------------------------------------------------------
#  Unterprogramm zur Ausgabe der Aktuellen Systemzeit
# --------------------------------------------------------------------
sub Zeit(){
 $uebergabe = shift;
 my $akt = localtime(time);
 $Monat = sprintf("%02d",$akt->mon + 1);
 $Monatstag = sprintf("%02d",$akt->mday);
 $Stunden = sprintf("%02d",$akt->hour);
 $Minuten = sprintf("%02d",$akt->min);
 $Sekunden = sprintf("%02d",$akt->sec);
 $Jahr = sprintf("%04d",$akt->year + 1900);
 if ($uebergabe ne "NURZEIT" &! $uebergabe eq "plus"){
	print LOG "$Monatstag.$Monat.$Jahr $Stunden:$Minuten:$Sekunden    ";
 }elsif ($uebergabe eq "plus"){
	$Minuten = $Minuten + 1;
	if ($Minuten >= 60){
		$Minuten = $Minuten - 60;
		$Stunden = $Stunden + 1;
	}#ENDE if ($Minuten >= 60)
	$Minuten = sprintf("%02d",$Minuten);
	$Stunden = sprintf("%02d", $Stunden);
	return "$Stunden:$Minuten:$Sekunden";
 }#ENDE if ($uebergabe eq "plus")
 return "$Monatstag.$Monat.$Jahr $Stunden:$Minuten:$Sekunden";
}#ENDE sub Zeit()

#--------------------------------------------------------------------
#  Unterprogramm zum "Drucken" der Statusmeldungen
# --------------------------------------------------------------------
sub druck() {
	print $status;
	&Zeit();
	print LOG $status;
}
