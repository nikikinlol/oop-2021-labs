class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance

a = Singleton()
b = Singleton()

print(a is b)
print(id(a), id(b))