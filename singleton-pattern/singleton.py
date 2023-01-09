class Singleton:
    __instance__ = None

    def __init__(self) -> None:
        # This is constructor

        if Singleton.__instance__ is None:
            Singleton.__instance__ = self
        else:
            raise Exception("We can not create another class")