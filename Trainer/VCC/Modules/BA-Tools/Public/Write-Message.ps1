function Write-Message {
    param(
        [Parameter(Mandatory)][String[]] $msg,
        [Switch] $suppressTime,
        [String] $logFile = ""
    )
    $msg | ForEach-Object {
        if(!$suppressTime) {
            $_ = "$(Get-Zeit) $_"
        }
        if($logFile -ne "") {
            $_ | Out-File -FilePath $logFile -Append
        }
        $_ | Write-Host
    }
}
