from filereader import QuestionFileReader
from bot import EscapeBot

# create instance of questionfilereader class
in_file_1 = QuestionFileReader("python-game-file.txt")
# parent_readfile_in_file_1 = in_file_1.read_all()
# print(parent_readfile_in_file_1 )

# parent_line_count = print(in_file_1.line_count())
# print(parent_line_count)

# parent_get_filename = in_file_1.get_filename()
# print(parent_get_filename)

parent_get_filename = in_file_1.set_filename("python-game-file.txt")
# print(parent_get_filename)
# a = __init__ & b = __str__
# print(in_file_1)

# '''c'''
c_dictqs_in_file_1 =in_file_1.all_dictionary_questions()
# print(c_dictqs_in_file_1)

# '''d'''
# d_lines_as_d = in_file_1.lines_as_dictionary([1,3,5])
# print(d_lines_as_d)
# '''e'''
# e_specific_qs = in_file_1.get_dictionary_range([1,3])
# print(e_specific_qs)

# '''f'''
# f_random_qs = in_file_1.random_dicitonary_questions()
# print(f_random_qs)

# '''g'''
# g_except_lines = in_file_1.exclude_dictionary_questions([2,3])
# print(g_except_lines)

# '''h'''
# h_except_range = in_file_1.exclude_dictionary_range([2,6])
# print(h_except_range)

"""MAIN CODE"""
# ------- main code section
# main code function outside the EscapeBot class
def question_and_answer():
    '''
    Function to:
    - get the current question (calling current_question() Method in EscapeBot class)
    - check if user's answer is correct (calling check_answer() Method in EscapeBot class)
    - display feedback (correct/incorrect) (calling display_incorrect()/display_correct() Method in EscapeBot class)
    - decrement lives if was incorrect (calling dectement_lives() Method in EscapeBot class)
    - check if  left
    - if lives left Function calls itself again
    '''
    # display current question to player by calling method inside the EscapeBot class
    python_game.current_question()
    # get user input (answer to displayed question)
    user_in = input("Your answer: ")
    # give the answer to the check_answer method in the EscapeBot class for interpretation, save the result in yesorno variable (True of False)
    yesorno = python_game.check_answer(user_in)
    # if the answer is correct
    if yesorno:
        # call the display_correct() Function inside the EscapeBot class to display the correct message
        python_game.display_correct()
    # if the answer was incorrect
    else: 
        # call the display_incorrect() Function inside the EscapeBot class to display the incorrect message
        python_game.display_incorrect()
        # call the decrement_lives() Function inside the EscapeBot class to decrement the lives of the player
        python_game.decrement_lives()
        # get the remaining lives of the player from inside the EscapeBot classes get_lives() method & save the remaining_lives to the variable 
        remaining_lives = python_game.get_lives()
        # print how many lives remaining
        print(python_game.display_lives())
        # if the player is not out of lives
        if remaining_lives > 0:
            # ask if they want to gamble to gain or lose a life
            another_life = input("Do you take the random risk of gaining your life back or losing another one? If so type in 'y' any other key will continue the game with your current lives.")
            # if they do
            if another_life.lower() == "y":
                # call the method randomly_gain_or_lose() in bot.py
                python_game.randomly_gain_or_lose()
            # the function calls itself again to display the question again
            question_and_answer()
        # if the answer was false and the player is out of lives go back to inplay after question_and_answer was called and check wether all questions have been played & display the termination message at the end

# calls class
# create instance variable 
python_game = EscapeBot("EscapeBot", "Ron", 1, 3, "Thank you for playing Escape Room Game!", "All questions have now been played!")
# print(python_game.get_questions())
# set questions
# set right answer response
python_game.set_correct("This was the right answer.")
# set wrong answer response
python_game.set_incorrect("This was the wrong answer.")
# set the questions to the long set
python_game.set_questions(c_dictqs_in_file_1)
# ask if they want to change
change_questions = str(input("Would you like to change the question set to a smaller one? Put in 'y' to change. Any other key will keep the original, longer set of questions."))
# if they want to change
if change_questions.lower() == "y":
    # get the dictionary containing every second question and assign to variable
    small_question_set = in_file_1.read_all()
    # set the questions to the smaller question set
    python_game.set_questions(small_question_set)
# calls instructions
print(python_game.get_instructions())
# draw the EscapeBot
python_game.draw("----------\n---*--*---\n----||----\n---____---\n----------")
# in_play set to false
in_play = False
# ask user if they want to play
user_in = input("Press Y to continue. Any other key quits the game!")
# if input is y
if user_in.lower() == "y":
    #now in play is true
    in_play = True
# while in play is true
while in_play:
    # save the lives to lives variable
    lives = python_game.get_lives()
    # if lives are left
    if int(lives) > 0:
        # print ten empty lines
        print("\n"*10)
        # call display position to display position
        python_game.display_position()
        # call fucntion question and answer outside the EscapeBot class, in the main code to give it to class to check if the answer was correct
        question_and_answer()
        '''removed commented out code below because it is redundant & unnecessary'''
        # if the user does not want to play anymore
        # if user_in.lower() == "n":
        #     # if end game display lives
        #     print(python_game.display_lives())
        # if the user is still playing
        # if user_in.lower() == "y":
        '''end of commented out redundant code'''
        # +1 position to increment position; is True if no qs left
        no_questions_left = python_game.increment_position()
        # if no questions left
        if no_questions_left == True:
            # finish game if no qs left: methof in EscapeBot class prints message that all questions have been played
            python_game.finished_game()
            # set playing to false to end while loop
            in_play = False
    # if no lives left but questions left
    else:
        # break out of the in_play loop
        break
# print ten empty lines
print("\n"*10)
# print termination_message to user (from method terminate_message() in EscapeBot class)
python_game.terminate_message()    