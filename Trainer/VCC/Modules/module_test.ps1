Import-Module "E:\Workspaces\ucuber\PowerShell\VCC\Modules\BA-Tools" -DisableNameChecking -Force
Import-Module "E:\Workspaces\ucuber\PowerShell\VCC\Modules\Execute-RoboCopy" -DisableNameChecking -Force

Write-Message "Hey"
Write-Message -msg "Hey${EOL}Ho"
Write-Message @("a", "b", "c") -suppressTime

function X {
    function Y {
        Write-Host "Y"
    }
    Y

}

X
