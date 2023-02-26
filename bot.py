# StudentNumber: 121722211
import random
class EscapeBot:

    # dictionaries in dictionary
    # class instance, not instance variable, so that the EscapeBot has a default question and answer sheet. 
    # It can be overwritten by using the set_questions() Method and will be used for following instances (changed if change to pony questions and then call excape bot again: get pony questions!)

    # __main__ methods
    def __init__(self, gametype, name, position, lives, goodbye, finisher):
        '''
        __init__ constructer method to initialise instance variables 
        instance variables created for increased level of reuse
        variables for method used to increase level of reuse: ie. things like name and type are not hardcoded, thus can be changed
        gametype for the type of game this EscapeBot is used fot
        name of the robot
        position of the player
        goodbye message
        amount of lives the player starts with
        '''
        # created game type instance variable so it does not always have to be a python escapebot
        self.gametype = gametype
        # robot name as instance variable, so the names can vary (code reusability)
        self.name = name
        # position of player (instance variable, so that it can be changes throughout the game and different games can start at different positions)
        self.position = position
        # goodbye message: instance variable so it can be set according to the game one wants to play
        self.goodbye = goodbye
        # all quations have been played message as instance variable so it can be changed
        self.finisher = finisher
        # lives of player so that differnt games can start with different amounts of lives
        self.lives = lives
        # game instructions moved to __init__ because they are only called at the beginning
        # game instructions as instance variable, so that they can be changed using set_instructions but the "blueprint" exists
        self.game_instructions = "Hello! My name is %s the %s! I am on a mission.\nI must retrieve the key to open this safe in front of me!\nBut only you can help me...\nYou must help me get the answers to these questions correct before I run out of lives.\nOnly then will I be able to retrieve the key to open the safe!\n " % (self.name, self.gametype)
        # set instance variable with default for correct answer message so it is changeable in set_correct()
        self.correct = "Your answer was correct!"
        # set instance variable with default for correct answer message so it is changeable in set_incorrect()
        self.incorrect = "Your answer was incorrect!"
    def __str__(self):
        '''
        String representation method
        '''
        # user-friendly representation of the bot's name and the game type
        botinfo = "Hi, my name is %s! I am of type %s." % (self.name, self.gametype)
        # return the string
        return botinfo
    
    # main methods
    def draw(self, display:str):
        '''
        Method to draw robot to console window
        display is a string that is the robot in keyboard characters
        not hard coded, so that looks of robot can be adjusted depending on what their name, type,... is
        added to give the robot a look
        '''
        if type(display) == str:
            print(display)
        else: 
            print("Could not display bot face. Bot face has to be represented as type string.")

    def display_name(self):
        '''
        Method to display the name of the robot
        It is not hard coded anymore, so that the robots name can change
        '''
        print("Hi, my name is %s the robot!" % self.name)
    
    def increment_position(self):
        '''
        Method to increment the players position
        gets number of questions and checks based on position wether all questions have been answered
        '''
        # get keys of the questions
        keysOfQuestions = EscapeBot.questions.keys()
        # determine how many quesitons there are (keys of the dictionary)
        numberofquestions = len(keysOfQuestions)
        # increment the players position (will now be one more than the last answered question: will turn 2 after q1 was answered)
        self.position = self.position + 1
        # if the position is greater than the number of playable questions
        # 5 changed to numberofquestions because the number of questions asked might vary from bot to bot
        if self.position > numberofquestions:
            # decrement position if it is too high
            self.position = self.position - 1
            # return TRUE: no questions left
            return True
        # if not all questions played
        else:
            # return that not all questions have been played
            return False
    
    def decrement_lives(self):
        '''
        Method to decrement lives if the answer was wrong
        Returns whether lives left
        '''
        # decrement self.lives
        self.lives -= 1
        # if lives left, assuming the game ends when 0 lives are left
        if self.lives > 0:
            # return True that lives left
            return True
        # if no lives left (lives = 0)
        else:
            # return lives left is False
            return False
        
    def increase_lives(self):
        '''
        Method to increase lives if randomly gains a life
        '''
        self.lives += 1

    def randomly_gain_or_lose(self):
        '''
        Method to randomly decide wether the user loses or gains a life
        '''
        # create random booolean
        random_number = bool(random.randint(0,1))
        # if 1 = True
        if random_number:
            # increment lives
            self.increase_lives()
            # print winner message
            print("Congrats, you gained a life! \n You now have: " + str(self.lives) + " lives.")
        # if 0 = False
        else:
            # take another life
            self.decrement_lives()
            # if lives left after losing one again
            if self.lives > 0:
                # print loser message but tell them that they can continue playing
                print("Loser! You lost another one, but life goes on! \n You now have: " + str(self.lives) + " lives")
            # if now has 0 lives
            else:
                # print loser message and tell them that the game is over
                print("Loser! You lost another one, life doesn't go on! \n You're out of lives.")

    def current_question(self):
        '''
        added to present the questions to the user
        Method to return the current question and possible answers
        Gets keys of each question based on key names (i.e."question" -> no matter order of quesiton, answer, stimulus in question package)
        '''
        # import random for answer order generation
        import random
        
        # get question package (quesion, stimulus, answer)
        questionpackage = EscapeBot.questions[self.position]
        # extract question with key name
        question = questionpackage["question"]
        # extract stimulus with key name
        stimulus = questionpackage["stimulus"]
        # extract answers with key name
        answers = questionpackage["answers"]
        # create a list for the shuffled answers
        shuffled_ans = list(answers)
        # shuffle the answers list
        random.shuffle(shuffled_ans)
        # get amount of possible answers
        len_retans = len(shuffled_ans)
        # set counter to 1
        counter = 1
        # create returnanswers string
        returnanswers = ""
        # loop over the answers
        for answer in shuffled_ans:
            # if not the last answer in list
            if counter < len_retans: 
                # add the possible answer and a comma to the returnanswers string
                returnanswers += str(answer) + ", "
            # if the last answer in list
            else:
                # add the possible answer and a full stop to the returnanswers string
                returnanswers += str(answer) + "."
            # increment counter
            counter +=1
        # print the quesrin, stimulus, answer prompt
        print(self.name, "wants to know...\n" + question +"\n>>>" , stimulus, "\nPossible answers are:\n" + returnanswers, "\n\n" + "Whats your guess? Type the full answer.")
    
    # getters and setters 
    
    def get_botname(self):
        '''
        Method to get robot name and return it
        '''
        return self.name
    
    def set_botname(self,new_name):
        '''
        Method to set new botname
        '''
        self.name = new_name
    
    def display_position(self):
        '''
        Method to print the current position of the player
        '''
        # print positon: string representation and instance variable used to enhance code reusability (can be used for all positions)
        print("You are now at position %s " % self.position)
    
    def get_goodbye(self):
        '''
        Method to get goodbye message
        '''
        return self.goodbye
    
    def set_goodbye(self, new_goodbye):
        '''
        Method to set goodbye method
        '''
        self.goodbye = new_goodbye


    def get_instructions(self):
        '''
        Method to get instructions instance variable and return it
        instructions are a instance variable, so they can be changed using set_instructions
        '''
        return self.game_instructions

    def set_instructions(self, new_instructions):
        '''
        Method to read and set instructions in the instance variable self.game_instructions
        '''
        self.game_instructions = new_instructions
    
    def get_lives(self):
        '''
        Method to return lives the player has left
        '''
        # return instance variable, so it is not hard coded since amount of lives can change during the game
        return self.lives
    
    def display_lives(self):
        '''
        Method to return lives in user-freindly format
        Method to display the lives the player has left
        Uses self.lives instance variable to create flexibility (the amount of lives left can change during the game)
        '''
        # return instance variable, so it is not hard coded since amount of lives can change during the game
        return "You have %s live(s) remaining." % (self.lives)

    def reset(self):
        '''
        Method/added to reset the current question position to 1
        hardcoded because instructions allow
        '''
        self.position = 1

    def get_questions(self):
        '''
        Method to get the qustions since there is a default, so the programmer can decide if they want to keep them or not
        Returns the questions class veriable
        '''
        # questionpackage is the questions class variable
        questionpackages = EscapeBot.questions
        # create returnstring
        packagestring = ""
        # loop over all questionpackages
        for item in questionpackages.items():
            # add each questionpackage as a string to returnstring and add a new line
            packagestring += str(item) +  "\n" 
        # return packagestring
        return packagestring    

    def set_questions(self, new_questions):
        '''
        Method to set new questions -> overwrites the class variable
        left like it was because it is flexible and correct
        '''
        # check if the parameter is a dictionary
        if type(new_questions) != dict:
            # if not print error message
            print("Questions must be of type dictionary (nested). Questions not reset.")
            # return to exit the set_questions method
            return
        # if type of the parameter is dictionary, check for the nested dictionaries
        for key in new_questions:
            # if the key of the quetions are not digits
            if str(key).isdigit() == False:
                # print error message
                print("Questions are not in the correct format. Questions not reset")
                # return to exit the set_questions method
                return
            # if the questions are numbered with digits
            else:
                # assign the each question package to keys
                keys = new_questions[key]
                # if the type of the nested dictionary is not dictionary
                if type(keys) != dict:
                    # print error message
                    print("Questions must be of type dictionary (nested). Questions not reset.")
                    # return to exit the set_questions method
                    return
                # if each question does not contain 3 keys (question, stimulus, answer)
                if len(keys) != 3:
                    # print error message
                    print("Questions are not in the correct format. Questions not reset")
                    # return to exit the set_questions method
                    return -1
                # if the keys of each question are not called question, answers and stimulus
                if "question" not in keys and "answers" not in keys and "stimulus" not in keys:
                    # print error message
                    print("Questions are not in the correct format. Questions not reset")
                    # return to exit the set_questions method
                    return
        # only if types of parameter and nested dictionaries and their contents are according to the format reset the questions
        EscapeBot.questions = new_questions
        # if questions reset print success message
        print("questions reset!")    


    
    # answer interpretation
    def check_answer(self, response:str):
        '''
        Method/created to to interpret the input question 
        Called from function in main code 
        Interprestation is not case sensitive and is not dependent on free space
        true_or_false set to True if the userinput was the correct answer
        '''
        # remove space/ line breaks in answers
        response = response.strip().strip("\n").strip("")
        # turn the response into lowercase so the interpretation is not case sensitive
        response = response.lower()
        # get the question, stimulus and answer at the current position
        questionpackage = EscapeBot.questions[self.position]
        # get the answer from the questionpackage
        answers = questionpackage["answers"]
        # the correct answer is the one saved at index 0
        correctanswer = answers[0]
        # make response and answer match
        correctanswer = correctanswer.lower()
        # set response to being false
        true_or_false = False
        # if the response if correct
        if response == correctanswer:
            # set true_or_false to true
            true_or_false = True
        # return wether answer was correct
        return true_or_false
    
    def display_correct(self):
        '''
        Method to print that the input answer was correct
        Simple answer is hardcoded because it can be used for all games if the answer was correct
        '''
        # print message, that it was correct
        print(self.correct)
    
    def set_correct(self, new_correct):
        '''
        Method to set new incorrect message to add flexibility
        '''
        self.correct = new_correct
    
    def set_incorrect(self, new_incorrect):
        '''
        Method to set new incorrect message to add flexibility
        '''
        self.incorrect = new_incorrect

    def display_incorrect(self):
        '''
        Method to print that the input answer was incorrect
        Simple answer is hardcoded because it can be used for all games if the answer was incorrect
        '''
        # print message, that it was false
        print(self.incorrect)

    def reveal_answer(self):
        '''
        Method to reveal the answer
        use instance variables and string representation, to increase code reausability: can be sued for all answers in the answerset and correct answer is unique to that question/answer 
        '''
        # correct answer is the first answer in the possible answers list
        correct_answer = EscapeBot.questions[self.position]["answers"][0]
        # print message as string
        print("The correct answer is: %s" % correct_answer)
        
    # terminators
    def finished_game(self):
        '''
        Method to print that all questions have been played
        printed only if all questions have been displayed
        Removed hard coded version and introduced instance variable 
        '''
        print(self.finisher)

    def terminate_message(self):
        '''
        Method to print the goodbye message, printed no matter whether all questions were answered (no matter if last question correct or incorrect)
        Left how it was because it uses an instance variable, that has to be given to __init__ when creating an instance of the class
        '''
        print(self.goodbye)

