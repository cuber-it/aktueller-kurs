class TextDatei:
    def __init__(self, file_name, auto_init=False):
        self.datei_name = file_name
        if auto_init == True:
            self.read_file()

    def read_file(self):
        with open(self.datei_name, "r", encoding="utf-8") as f:
            self.datei_inhalt = f.readlines()

    def get_text(self):
        return self.datei_inhalt

    def set_datei_name(self, file_name):
        self.datei_name = file_name
        self.datei_inhalt = None



#------------------------------------------------------------------
andere_datei = TextDatei("./lottogame.py", True)

thesaurus_datei = TextDatei("../tag-2/openthesaurus.txt")
thesaurus_datei.read_file()

sample_log_datei = TextDatei("../tag-1/neudaten.log")
sample_log_datei.read_file()

print(len(andere_datei.get_text()))
print(len(thesaurus_datei.get_text()))
print(len(sample_log_datei.get_text()))





