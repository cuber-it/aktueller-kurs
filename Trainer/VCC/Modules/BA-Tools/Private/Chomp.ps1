function chomp {
    param([String]$text)
    return $text.replace($CR, "").replace($LF, "")
}