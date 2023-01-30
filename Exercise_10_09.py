class Question:

    # The __init__ method initializes the class attributes
    def __init__(self, question, answer1, answer2, answer3, answer4, answer_number):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__answer_number = answer_number

    # The set_question method sets the question attribute
    def set_question(self, question):
        self.__question = question

    # The set_answer1 method sets the question attribute
    def set_answer1(self, answer1):
        self.__answer1 = answer1

    # The set_answer2 method sets the question attribute
    def set_answer2(self, answer2):
        self.__answer2 = answer2

    # The set_answer3 method sets the question attribute
    def set_answer3(self, answer3):
        self.__answer3 = answer3

    # The set_answer4 method sets the question attribute
    def set_answer4(self, answer4):
        self.__answer4 = answer4

    # The set_answer_number sets the answer_number attribute
    def set_answer_number(self, answer_number):
        self.__answer_number = answer_number

    # The get_question method returns the question attribute
    def get_question(self):
        return self.__question

    # The get_answer1 method returns the answer1 attribute
    def get_answer1(self):
        return self.__answer1

    # The get_answer2 method returns the answer2 attribute
    def get_answer2(self):
        return self.__answer2

    # The get_answer3 method returns the answer3 attribute
    def get_answer3(self):
        return self.__answer3

    # The get_answer4 method returns the answer4 attribute
    def get_answer4(self):
        return self.__answer4

    # The get_answer_number method returns the answer_number attribute
    def get_answer_number(self):
        return self.__answer_number


def main():
    try:
        # Get a list of Question objects
        questions = get_questions()

        # Play the game
        player1_score, player2_score = play_game(questions)

        # Display the winner
        display_winner(player1_score, player2_score)
    except (TypeError, IndexError, IOError, Exception) as e:
        print(e)


# This method returns a list of Question objects
def get_questions():
    # Questions list
    return [[Question('Q: What does "WWW" Stand for? ',
             '1. World Wide Web', '2. West World Woven', '3. Web Worship Wagoneer', '4. Women West Winners', 1)],
            [Question('Q: What is Cynophobia? ',
             '1. Fear of Spiders', '2. Fear of Dolphins', '3. Fear of Spiders', '4. Fear of Bears', 1)],
            [Question('Q: Who Wrote the First Dictionary? ',
             '1. Stephen Hawking', '2. Bill Gates', '3. Robert Cawdrey', '4. Steve Jobs', 3)],
            [Question('Q: What is the Rarest M&M Color? ',
             '1. Red', '2. Brown', '3. Blue', '4. Yellow', 2)],
            [Question('Q: What was the First Soft Drink in Space? ',
             '1. Coca-Cola', '2. Pepsi', '3. Dr. Pepper', '4. Sprite', 1)],
            [Question('Q: Havana is the Capital of What Country? ',
             '1. Cuba', '2. United States', '3. Denmark', '4. Mexico', 1)],
            [Question('Q: Loudest Animal on Earth? ',
             '1. Elephant', '2. Tiger', '3. Sperm Whale', '4. Lion', 3)],
            [Question('Q: How Many Legs does a Spider Have? ',
             '1. 4', '2. 5', '3. 6', '4. 8', 4)],
            [Question('Q: What is the Hottest Planet in the Solar System? ',
             '1. Mars', '2. Earth', '3. Jupiter', '4. Venus', 4)],
            [Question('Q: What is the Nearest Planet to the Sun? ',
             '1. Mars', '2. Earth', '3. Mercury', '4. Pluto', 3)]]


# This function allows the user to play the game
def play_game(questions):
    # Initialize accumulator variables
    player1_score = player2_score = 0

    # Display trivia questions
    turn = 1
    for index in range(0, 10):
        for question in questions[index]:
            print(question.get_question())
            print(question.get_answer1(), '\n', question.get_answer2(), '\n',
                  question.get_answer3(), '\n', question.get_answer4(), sep='')
            if turn % 2 != 0:
                answer = int(input('\nPlayer 1 Turn - Enter your answer: '))
                player1_score = evaluate(answer, question, player1_score)
            else:
                answer = int(input('\nPlayer 2 Turn - Enter your answer: '))
                player2_score = evaluate(answer, question, player2_score)
            print()
            turn += 1

    return player1_score, player2_score


# This function displays the winner or whether there is a tie
def display_winner(score1, score2):
    if score1 > score2:
        print(f'Player 1 Points: {score1}\nPlayer 2 Points: {score2}\nPlayer 1 Wins!')
    elif score2 > score1:
        print(f'Player 1 Points: {score1}\nPlayer 2 Points: {score2}\nPlayer 2 Wins!')
    else:
        print('Tie.')


# This function evaluates the answer given and increases the score if applicable
def evaluate(answer, question, score):
    if answer == question.get_answer_number():
        print('Correct! 1 Point Awarded.')
        score += 1
    else:
        print('Incorrect. No Points Awarded.')

    return score


# Call the main function
if __name__ == '__main__':
    main()
