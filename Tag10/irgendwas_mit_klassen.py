class Daten:
    def get_attr(self):
        # If attr does not exist, getattr will return None
        return getattr(self, 'attr', None)



d = Daten()
d.write(open("daten.txt"))
