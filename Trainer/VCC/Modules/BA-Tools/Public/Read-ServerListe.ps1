function Read-ServerListe {
	[CmdletBinding()]
    param(
        [String] $serverListePath
    )

    $server_Name2Type = @{}
    $server_Type2Names = @{}

    Write-Message -msg "Inhalte $serverListePath"
    ForEach($entry in (Get-Content $serverListePath | ForEach { Chomp($_) })) {
        if($entry -match "^n\d{7}") {
            $name, $_, $typ =  (($entry -replace "`t"," ") -replace " {2,}"," ").split(" ")
            Write-Message -msg "`t$typ -> $name"
            $server_Name2Type[$name] = $typ

            if(!$server_Type2Names.ContainsKey($typ)) {
                $server_Type2Names[$typ] = @()
            }
            $server_Type2Names[$typ] += $name
        }
    }

    return @{
        "NameToTypes"=$server_Name2Type
        "TypeToNames"=$server_Type2Names
    }
}


#foreach $SRV (@SRV){#
	#if ($SRV =~ /^n\d{7}/){
	#	$SRV =~ s/\t.{9}//i;
	#	@SRV_Teil = split(/ /,$SRV);
	#	print "$SRV_Teil[1]  ->   $SRV_Teil[0]\n";
	#	push(@{$Server{$SRV_Teil[1]}},$SRV_Teil[0]);
	#	$SERVERTYP{$SRV_Teil[0]} = $SRV_Teil[1];
	#}#ENDE if ($SRV =~ /^n\d{7}/)
#}#ENDE foreach $SRV (@SRV)
#}
