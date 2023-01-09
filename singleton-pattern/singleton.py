class Singleton:
    __instance__ = None

    def __init__(self) -> None:
        # This is constructor

        if Singleton.__instance__ is None:
            Singleton.__instance__ = self
        else:
            raise Exception("We can not create another class")

        
    @staticmethod
    def get_instance():
        # we defined a static method to fetch instance
        if not Singleton.__instance__:
            Singleton()
        return Singleton.__instance__
        

# Creating an object
single = Singleton()
print(single)

same_single = Singleton.get_instance()
print(same_single)

another_single = Singleton.get_instance()
print(another_single)

new_sinle = Singleton()
print(new_sinle)
