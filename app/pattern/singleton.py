

class Singleton(type):
    def __init__(self, name, bases, dic):
        self.__instance = None
        super().__init__(name, bases, dic)

        def __call__(cls, *args, **kwargs):
            if cls.__instance:
                return cls.__instance
            else:
                init_instance = cls.__new__(cls)
                init_instance.__init__(*args, **kwargs)
                cls.__instance = init_instance
                return cls.__instace