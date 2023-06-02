class LottoBude:
    def __init__(self, style="6aus49"):
        self.style = style

        if style == "6aus49":
            self.minNumber = 1
            self.maxNumer = 49
            self.tippCount = 6
            self.tipp = []
        else:
            raise Exception(f"Not yet implemented: {style}")

    def eingabe(self, tipp):
        tipp = tipp.split(",")
        if len(tipp) != self.tippCount:
            raise Exception(f"Invalid Tipp: {len(tipp)} digits")

        for ziffer in tipp:
            ziffer = int(ziffer)
            if ziffer < self.minNumber or ziffer > self.maxNumer:
                raise Exception(f"Invalid Tipp: {ziffer} invalid")
            if ziffer in self.tipp:
                raise Exception(f"InvalidTipp: {ziffer} is more than once in tipp")
            self.tipp.append(ziffer)
        return self.tipp


if __name__ == "__main__":
    l = LottoBude()
    tipp = l.eingabe("1,2,3,4,5,-5")
    print(tipp)
