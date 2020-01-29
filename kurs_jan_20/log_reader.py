import log_tools

def weiterverarbeitung(log):
    pass

roh = log_tools.read_log("SampleLog.log")
neu = log_tools.prepare_log(roh)

weiterverarbeitung(neu)

log_tools.write_log("CleanLog.log", neu)