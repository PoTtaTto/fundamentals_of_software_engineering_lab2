class Car:
    def __init__(self, is_for_training: bool, max_speed: float):
        self.is_for_training = is_for_training
        self.max_speed = max_speed

    def __repr__(self):
        if self.is_for_training:
            return f'Training car with max speed - {self.max_speed}km/h'
        else:
            return f'Normal car with max speed - {self.max_speed}'