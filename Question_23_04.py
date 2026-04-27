# Write out a custom logging class (using logging import) with an instance using singleton design pattern. Now call that logger instance in two or three different classes. To print a just log its doing something.
import logging

class MyLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            logger = logging.getLogger("MyLogger")
            logger.setLevel(logging.INFO)

            if not logger.handlers:
                handler = logging.StreamHandler()
                formatter = logging.Formatter(
                    "%(asctime)s    | %(levelname)s    | %(message)s"
                )
                handler.setFormatter(formatter)
                logger.addHandler(handler)
            
            cls._instance.logger = logger

        return cls._instance
    
    def get_logger(self):
        return self.logger
    

class A:
    def __init__(self):
        self.log = MyLogger().get_logger()

    def do_something(self):
        self.log.info("Class A is doing something")

class B:
    def __init__(self):
        self.log = MyLogger().get_logger()

    def do_something(self):
        self.log.info("Class B is doing something")


a = A()
b = B()

a.do_something()
b.do_something()