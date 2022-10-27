function Copy-FileRecursive {
    param(
        [Parameter(Mandatory)][String] $source,
        [Parameter(Mandatory)][String] $destination,
        [Parameter(Mandatory)][String] $filter,
        [String] $logFile
    )

    Write-Message -logFile $logFile "Execute-FileCopyRecursive: $source $destination $filter"

    try {
        $count = (Copy-Item -Path $source -Destination $destination -Filter $filter -Force -Recurse -ErrorAction Stop -PassThru).Count
        $rvalue = "ERFOLG: Kopiervogang erfolgreich abgeschlossen ($count Elemente)"
    } catch {
        $rvalue = "FEHLER: Kopiervorgang abgebrochen ($_)"
    }
    return $rvalue
}

function Copy-File {
    param(
        [Parameter(Mandatory)][String] $source,
        [Parameter(Mandatory)][String] $destination
    )

    if (!(Test-Path -path $destination)) {
        New-Item $destination -Type Directory
    }

    Copy-Item -Path $source -Destination $destination -Force
}
