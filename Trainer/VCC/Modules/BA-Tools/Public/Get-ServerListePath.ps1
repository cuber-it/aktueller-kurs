function Get-ServerListePath {
    param(
        [String] $umgebung,
        [String] $appPath
    )
    if($umgebung -imatch "edst"){
        $txtFile = "_QUTest-e_Liste.txt"
    } elseif ($umgebung -imatch "idst"){
        $txtFile = "_QUTest-i_Liste.txt"
    } else {
        $txtFile = "_QUTest-d_Liste.txt"
    }
    return Join-Path $appPath $txtFile
}
