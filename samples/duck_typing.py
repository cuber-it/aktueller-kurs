class Duck:
    def speak(self) -> str:
        return "Quak"


class Robot:
    def speak(self) -> str:
        return "Beep"


def talk(thing) -> None:
    print(thing.speak())    # kein Typcheck, nur: hat es speak()?


for t in (Duck(), Robot()):
    talk(t)
