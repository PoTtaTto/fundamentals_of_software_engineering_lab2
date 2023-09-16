import uuid
import enum


class EvaluateLevel(enum.Enum):
    EXCELLENT = 'excellent mark'
    GOOD = 'good mark'
    NOT_BAD = 'not bad mark'
    AWFUL = 'awful mark'


class Car:
    def __init__(self, is_for_training: bool, max_speed: float):
        self.is_for_training = is_for_training
        self.max_speed = max_speed

    def __repr__(self):
        if self.is_for_training:
            return f'Training car with max speed - {self.max_speed}km/h'
        else:
            return f'Normal car with max speed - {self.max_speed}'


class Driver:
    def __init__(self, driving_skill: float):
        self.id = str(uuid.uuid4())
        self.driving_skill = driving_skill


class HiringManagement:
    @staticmethod
    def evaluate(driver: Driver) -> (str, EvaluateLevel, Car):
        if driver.driving_skill >= 100:
            return driver.id, EvaluateLevel.EXCELLENT, Car(is_for_training=False, max_speed=220.5)
        elif driver.driving_skill >= 60:
            return driver.id, EvaluateLevel.GOOD, Car(is_for_training=False, max_speed=160.4)
        elif driver.driving_skill >= 20:
            return driver.id, EvaluateLevel.NOT_BAD, Car(is_for_training=True, max_speed=90)
        else:
            return driver.id, EvaluateLevel.AWFUL, Car(is_for_training=True, max_speed=47.8)

