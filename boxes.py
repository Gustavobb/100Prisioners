from box import Box
import random

class Boxes:
    """
    Class Box
    """
    def __init__(self, number_of_boxes) -> None:
        """
        Constructor
        """
        self.boxes = []
        self.number_of_boxes = number_of_boxes
        self.number_of_boxes_list = [i for i in range(0, self.number_of_boxes)]
    
    def add_box(self, box) -> None:
        """
        Add a box to the list
        """
        self.boxes.append(box)
    
    def construct_boxes_database(self) -> None:
        """
        Construct the boxes database
        """
        self.boxes = []
        random.shuffle(self.number_of_boxes_list)

        for i in range(self.number_of_boxes):
            self.add_box(Box(i, self.number_of_boxes_list[i]))