from plumbum import local

ls = local["ls"]
grep = local["grep"]
print((ls | grep("py")).run())  # list files, then grep for "py"
