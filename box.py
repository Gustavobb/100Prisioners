class Box:
    """
    Class Box
    """
    def __init__(self, id, number) -> None:
        """
        Constructor
        """
        self.id = id
        self.number = number
    
    def open_box(self) -> int:
        """
        Get the content of the box
        """
        return self.number