from prisoner import Prisoner
from boxes import Boxes

class Prisoners:
    """
    Class Prisoners
    """
    def __init__(self, number_of_boxes, number_of_prisoners, use_strategy) -> None:
        """
        Constructor
        """
        self.prisoners = []
        self.boxes = Boxes(number_of_boxes)
        self.number_of_prisoners = number_of_prisoners
        self.use_strategy = use_strategy
        self.construct_prisoners_database()
    
    def construct_prisoners_database(self) -> None:
        """
        Construct the prisoners database
        """
        number_of_tries = int(self.number_of_prisoners / 2)

        for i in range(self.number_of_prisoners):
            prisoner = Prisoner(i, number_of_tries)
            prisoner.set_strategy(self.use_strategy)
            self.prisoners.append(prisoner)
    
    def start_choosing_boxes(self) -> int:
        """
        Start choosing boxes
        """
        self.boxes.construct_boxes_database()
        boxes = self.boxes.boxes

        success_count = 0
        for prisoner in self.prisoners:
            success_count += prisoner.try_to_find_box(boxes.copy())
        
        print(str(success_count) + " out of " + str(self.number_of_prisoners) + " prisoners found the box")
        return 1 if success_count == self.number_of_prisoners else 0