from boxes import Boxes
from prisoners import Prisoners

def ask_default(question: str, default: int) -> int:
    """
    Ask a question and return the answer.
    If the answer is not given, return the default.
    """
    answer = input(question + "(press enter for default: " + str(default) + ") ")
    return int(answer) if answer.isnumeric() else default

def simulate(prisoners: list, number_of_iterations: int) -> None:
    """
    Simulate the 100 prisoners algorithm with the given number of iterations.
    """
    success_count = 0
    for i in range(number_of_iterations):
        success_count += prisoners.start_choosing_boxes()
        print("\nIteration " + str(i + 1) + ": " + str(success_count) + " success out of " + str(number_of_iterations) + " iterations")
    
    print("\nSuccess rate: " + str(success_count / number_of_iterations * 100) + "%")

def main() -> int:
    """
    Main function
    """
    print("\nStart of program.")
    number_of_iterations = ask_default("How many iterations? ", 1)
    use_strategy = ask_default("Do you want to use the strategy? (y -> 1 / n -> 0) ", 1) == 1
    algorithm_multiplier = ask_default("By how much do you want to multiply the number of prisoners / boxes? ", 1)
    
    number_of_prisoners = 100 * algorithm_multiplier
    number_of_boxes = number_of_prisoners
    prisoners = Prisoners(number_of_boxes, number_of_prisoners, use_strategy)

    simulate(prisoners, number_of_iterations)
    print("\nSimulation made with " + str(number_of_iterations) + " iterations with " + str(number_of_prisoners) + " prisoners and " + str(number_of_boxes) + " boxes, using strategy: " + str(bool(use_strategy)))
    print("\nEnd of program.")
    return 0

if __name__ == "__main__":
    main();
    exit(0);