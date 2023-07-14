import random

class LottoBude:
    ziehung = []
    tipp = []
    result = []

    def play(self):
        self.ziehung = random.sample(range(1,50), 6)
        self.result = list(set(self.tipp).intersection(set(self.ziehung)))
        return self

    def enter_tipp(self, tipp, delim="."):
        self.tipp = [int(zahl) for zahl in tipp.split(delim)]
        return self

    def fetch_result(self):
        return self.tipp, self.ziehung, self.result

if __name__ == "__main__":
    l = LottoBude()
    l.enter_tipp("1.2.3.4.5.6")
    l.play()
    print(l.fetch_result())
