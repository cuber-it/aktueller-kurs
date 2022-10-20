function Get-Zeit {
    param(
        [String]$operation
    )
    $date = Get-Date

    if($operation -eq "plus") {
        $date = $date.AddMinutes(1).ToString("HH:mm:dd")
    } elseif($operation -eq "log") {
        $date = $date.ToString("yyyyMMdd-HHmm")
    } else {
        $date = $date.ToString("dd.MM.yyyy HH:mm:ss")
    }
    return $date
}