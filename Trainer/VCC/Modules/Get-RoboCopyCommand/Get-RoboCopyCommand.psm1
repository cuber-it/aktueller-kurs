$ROBOCOPY = "C:\Windows\System32\Robocopy.exe"

function Get-RoboCopyCommand {
    param(
        [Parameter(Mandatory)][String] $source,
        [Parameter(Mandatory)][String] $destination,
        [Parameter(Mandatory)][String] $files,
        [String] $options = "/COPY:DAT /E /NP /R:3 /W:3"
    )

    return @($ROBOCOPY, $source, $destination, $files) + $options.split(" ")
}
