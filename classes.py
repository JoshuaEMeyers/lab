class Television:
    """
    Class to represent the Television objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state of TV.
        """
        self.__Tv_Volume: int = Television.MIN_VOLUME
        self.__Tv_Channel: int = Television.MIN_CHANNEL
        self.__Tv_Status: bool = False

    def power(self) -> None:
        """
        Method to turn the TV on/off
        """
        if self.__Tv_Status is False:
            self.__Tv_Status = True
        else:
            self.__Tv_Status = False

    def channel_up(self) -> None:
        """
        Method to turn the TV channel up
        """
        if self.__Tv_Status is True:
            self.__Tv_Channel = self.__Tv_Channel + 1
            if self.__Tv_Channel > Television.MAX_CHANNEL:
                self.__Tv_Channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to turn the TV channel down
        """
        if self.__Tv_Status is True:
            self.__Tv_Channel = self.__Tv_Channel - 1
            if self.__Tv_Channel < Television.MIN_CHANNEL:
                self.__Tv_Channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to turn the TV volume up
        """
        if self.__Tv_Status is True:
            self.__Tv_Volume = self.__Tv_Volume + 1
            if self.__Tv_Volume > Television.MAX_VOLUME:
                self.__Tv_Volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
       Method to turn the TV volume down
        """
        if self.__Tv_Status is True:
            self.__Tv_Volume = self.__Tv_Volume - 1
            if self.__Tv_Volume < Television.MIN_VOLUME:
                self.__Tv_Volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to display the TV status of power, channel and volume
        """
        return f'TV status: Is on = {self.__Tv_Status}, Channel = {self.__Tv_Channel}, Volume = {self.__Tv_Volume}'
