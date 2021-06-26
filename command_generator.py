import random
from enum import Enum


class RandomId:
    __IDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    def __call__(self) -> str:
        return random.choice(self.__IDS)


class RandomDirection:
    __DIRECTIONS = ['forward', 'backward']
    def __call__(self) -> str:
        return random.choice(self.__DIRECTIONS)


class RandomSpeed:
    __SPEED_VALUES = ['one', 'two', 'three', 'four', 'five']
    def __call__(self) -> str:
        return random.choice(self.__SPEED_VALUES)


class Commands(Enum):
    PREFIX = 'pkm'
    TRAIN = 'train'
    DIRECTION = 'direction'
    SPEED = 'speed'
    START = 'start'
    STOP = 'stop'
    STOP_ALL = 'stop all'


class CommandGenerator:
    def __init__(self) -> None:
        self.__id = RandomId()
        self.__direction = RandomDirection()
        self.__speed = RandomSpeed()

    def __call__(self) -> str:
        choice = random.randint(0, 9)
        if choice < 5:
            return self.__get_start_command()
        elif choice < 8:
            return self.__get_stop_command()
        else:
            return self.__get_stop_all_command()

    def __get_start_command(self) -> str:
        command = self.__get_random_train()
        if random.choice([True, False]):
            command = ' '.join([command, self.__get_random_direction(), self.__get_random_speed()])
        else:
            command = ' '.join([command, self.__get_random_speed(), self.__get_random_direction()])
        return ' '.join([command, Commands.START.value])

    def __get_stop_command(self) -> str:
        return ' '.join([self.__get_random_train(), Commands.STOP.value])

    def __get_stop_all_command(self) -> str:
        return ' '.join([Commands.PREFIX.value, Commands.STOP_ALL.value])

    def __get_random_train(self) -> str:
        return ' '.join([Commands.PREFIX.value, Commands.TRAIN.value, self.__id()])

    def __get_random_direction(self) -> str:
        return ' '.join([Commands.DIRECTION.value, self.__direction()])

    def __get_random_speed(self) -> str:
        return ' '.join([Commands.SPEED.value, self.__speed()])
