function Write-Message {
    [CmdletBinding()]
    param(
        [Parameter(ValueFromPipeline)][String] $msg,
        [Switch] $suppressTime,
        [String] $logFile = ""
    )
    process {
        if(!$suppressTime) {
            $msg = "$(Get-Zeit) $msg"
        }
        if($logFile -ne "") {
            $msg | Out-File -FilePath $logFile -Append
        }
        $msg | Write-Host
    }
}
