#Get public and private function definition files.
$Private = @( Get-ChildItem -Path $PSScriptRoot\Private\*.ps1 -ErrorAction SilentlyContinue )
$Public  = @( Get-ChildItem -Path $PSScriptRoot\Public\*.ps1 -ErrorAction SilentlyContinue )

#Dot source the files
Foreach($import in @($Public + $Private))
{
    Try
    {
        . $import.fullname
    }
    Catch
    {
        Write-Error -Message "Failed to import function $($import.fullname): $_"
    }
}

# Here I might...
    # Read in or create an initial config file and variable
    # Export Public functions ($Public.BaseName) for WIP modules
    # Set variables visible to the module and its functions only

Set-Variable LF -Option Constant -Value "`n"
Set-Variable CR -Option Constant -Value "`r"
Set-Variable EOL -Option Constant -Value "`n"

# Vorbereitete Hilfsvariablen aka Konstanten
Export-ModuleMember -Variable LF
Export-ModuleMember -Variable CR
Export-ModuleMember -Variable EOL

# Alle in Public liegenden Funktionalitäten exportieren
$Public | ForEach { Export-ModuleMember -Function $_.Basename }
