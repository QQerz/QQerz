class Car:

    def __init__(self, title, model, weight, engine, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.engine = engine
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'Output {self.title}  {self.model} with engine {self.engine} started!')

    def stop_engine(self):
        print(f'Output {self.title}  {self.model} with engine {self.engine} stoped!')

    def info(self):
        print(f'Some characteristics: weight={self.weight}, hp={self.hp}, nm={self.nm}, max_speed={self.max_speed}.')


bmw = Car('bmw', 'e39', 1550, 'm62', 600, 750, 247, 'black')
bmw.start_engine()
bmw.stop_engine()
bmw.info()
