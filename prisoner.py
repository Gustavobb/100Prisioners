import random

class Prisoner:
    """
    Class Box
    """
    def __init__(self, id, number_of_tries) -> None:
        """
        Constructor
        """
        self.id = id
        self.box_idx = self.id
        self.boxes = []
        self.number_of_tries = number_of_tries

    def choose_random_box(self) -> bool:
        """
        Choose a random box
        """
        idx = random.randint(0, len(self.boxes) - 1)
        box = self.boxes[idx]
        self.boxes.pop(idx)
        return box.open_box() == self.id

    def choose_box_with_strategy(self) -> bool:
        """
        Choose a box with the strategy described in the readme
        """
        box_number = self.boxes[self.box_idx].open_box()
        if box_number == self.id:
            return True
        
        self.box_idx = box_number;

    def try_to_find_box(self, boxes) -> int:
        """
        Try to find the box
        """
        self.box_idx = self.id
        self.boxes = boxes

        for i in range(self.number_of_tries):
            if self.choose_box():
                return 1

        return 0

    def set_strategy(self, use_strategy) -> None:
        """
        Set the strategy
        """
        self.choose_box = self.choose_box_with_strategy if use_strategy else self.choose_random_box