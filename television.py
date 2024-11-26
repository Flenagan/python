class Television:
    """
    A class that provides variables for some of the functions of the TV.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self)-> None:
        """
        Sets the TV default settings based on Class Television variables.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self)-> None:
        """
        Turns TV ON or OFF through boolean value swapping.
        """
        self.__status = not self.__status

    def mute(self)-> None:
        """
        Mutes or unmutes the TV through boolean value swapping.
        """
        if self.__status == True:

            self.__muted = not self.__muted

    def channel_up(self)-> None:
        """
        If TV is powered on, increment by 1.
        Loops back to MIN_CHANNEL, if current position is equal to MAX_CHANNEL.
        """
        if self.__status == True:

            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self)-> None:
        """
        If TV is powered on, decrement by 1.
        Loops back to MAX_CHANNEL, if current position is equal to MIN_CHANNEL.
        """
        if self.__status == True:

            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self)-> None:
        """
        If TV is on: unmute TV and increment by 1.
        """
        if self.__status == True:

            if self.__muted == True:
                self.__muted = False

            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self)-> None:
        """
        If TV is on decrement volume by 1 and unmute the TV.
        """
        if self.__status == True:

            if self.__muted == True:
                self.__muted = False

            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns string of information about the status of the TV
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


