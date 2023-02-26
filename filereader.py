# Student Number: 121722211
# create Parent class
class FileReader:
    '''
    No changes in this class!!!
    '''
    # create initialiser
    def __init__(self, filename):
        # create private instance variable of file name
        self.__filename = filename
        # print that instance was created
        print("instance of FileReader class created!")
    
    def read_all(self):
        '''
        Method to read all the lines from the file with the filename
        '''
        # try to run this code(part of exception/error handling)
        try:
            # open the file and assign it as a variable
            file_1 = open(self.__filename)
                # read all lines from the file and assign to variable lines
            lines = file_1.readlines()
                # close the file
            file_1.close()
                # return the lines of the file
            return lines
            # exception of error handling
        except:
        # print error message if something went wrong and file could not be opened (i.e. does not exist/wrong name/not in right folder)
            print("file not opened. Terminating method")
        # and return false
            return False

    def line_count(self):
        '''
        Method use all lines from the file and count how many there are and return this value
        '''
        # call method read_all to get all lines in file
        lines = self.read_all()
        # take the length of the lines in order to get the amount of lines in the file
        line_amount = len(lines)
        # return the variable holding the number of lines in the file
        return line_amount   

    def get_filename(self):
        '''
        Method to get and return the filename, which is a private variable in __init__
        '''
        return self.__filename

    def set_filename(self, new_filename):
        '''
        Method to set the filename (setter) and assign it to the privte variable 
        '''
        self.__filename = new_filename 

# create childs class QuestionFileReader of FileReader
class QuestionFileReader(FileReader):
    # method overriding from parent class
    def __init__(self, filename):
        '''
        Method to inherit the variables given to the parent class
        '''
        # import the variables and methods from the parent class 
        super().__init__(filename)
        # get filename from method in parent class (uses inheritance, extending upon parent class __init__)
        self.filename = super().get_filename()
        # pass

    def __str__(self):
        '''
        Method to create string representation: object is printed to the screen
        contains reader-friendly information concerning the object’s instance: 
        filename and description of what the class does
        '''
        # create sting representation string
        str_rep = "The file read is: " + self.filename + ". This class formats the file content into a nested dictionary, that can be used as the question, stimulus and answer package for the escape bot."
        #return the string representation string
        return str_rep
        #pass
    
    def to_dictionary(self, wanted_questions:list):    
        '''
        Method to turn a list (wanted_questions) into the dictionary format
        '''
        # create readall_dict dictionary to hold the questions in a nested dictionary format (this is the outer dictionary)
        readall_dict = {}
        # loop through the readall list keeping the index and package
        for index, package in enumerate(wanted_questions):
            # create subdict for creating nested dictionary
            subdict = {}
            # key is index+1 because first question is 1 not 0
            key = index+1
            #  question is 0 index in current index with subkey "question"
            subdict["question"] = package[0]
            # stimulus is 1 index in current index with subkey "stimulus"
            subdict["stimulus"] = package[1]
            # answer is rest of the line with subkey "answers"
            subdict["answers"] = package[2::]
            # add subdict with key to readall_dict
            readall_dict[key] = subdict
        # return the created dictionary 
        return readall_dict

    def read_all(self):
        '''
        Method to read all the lines from the file with the filename
        Method overrides read_all method in parent class
        Call every_second_question method to get dictionary of every second question
        Return the dictionary
        '''
        # read all lines using inheritance
        all_questions = super().read_all()
        # extend upon parent class by calling every_second_question method
        every_second_q = self.every_second_question(all_questions)
        # return the dictionary of every second question questionset
        return every_second_q

    def every_second_question(self, all_questions:list):
        '''
        Method to:
        - get every second question 
        - Call a method to turn it into a dictionary
        - Return the dictionary of questions, stimuli and answers
        '''
        # remove the first line and keep every second line in the list
        all_questions = all_questions[1::2]
        # create new list for all second questions 
        new_all_questions = []
        # loop over the items in the list
        for item in all_questions:
            # remove line breaks
            item = item.strip("\n")
            # split the line contents at the comma
            item = item.split(",")
            # append the question to the list
            new_all_questions.append(item)
        # assign the new_all_questions containing every second question to all_questions
        all_questions = new_all_questions
        # call the to_dictionary method to turn the list to a dictionary and store it in a variable
        dictionary_questions = self.to_dictionary(all_questions)
        # return the dictionary questions
        return dictionary_questions


    def all_dictionary_questions(self):
        '''
        Method to call the self.readall() in parent class because reading again would be redundant 
        - converts this content to the nested dictionary format
        - returns the nested dictionary contents.
        '''
        # try to run this code
        try:
            # call the read_file() method from the parent class, and store the content from the returned result into a variable. (uses inheritance)
            readall = super().read_all()
            # remove the first line (it only includes specifications on the content of the following lines)
            readall = readall[1::]
            # create list 
            new_readall = []
            # split the values in the lines 
            for item in readall:
                # remove line breaks
                item = item.strip("\n")
                # split the line contents at the comma
                item = item.split(",")
                # append the item to the list
                new_readall.append(item)
            #call the to_dictionary function 
            readall_dict = self.to_dictionary(new_readall)
            # return the created dictionary 
            return readall_dict
            # pass
        # add exception handling if something else goes wrong
        except:
            # return error message
            return "Oops. Something went wrong."

    def lines_as_dictionary(self, line_nums_list:list[int]):
        '''
        Method to return the questions, stimuli and answers in the dictionary format specified in line_nums_list
        This method accepts the following parameters:
        • line_nums_list (list: int): an integer list, containing line numbers to obtain from the file.
        • The list may be of any length greater than or equal to 1. 
        • assumed that all line numbers in the list are contained in the file and there are no duplicate line numbers listed.
        '''
        # get the question, stimulus, answer packages dictionary from all_dictionary_questions method
        all_questions = self.all_dictionary_questions()
        # create returndicitonary
        returndict = {}
        # create new key
        new_key = 1
        # try to run this code
        try:
            # loop over the line_nums_list
            for line_num in line_nums_list:
                # add line_num as key to returndict and value at key line_num from all_quesitons 
                returndict[new_key] = all_questions[line_num]
                # increment new_key
                new_key += 1
            #return returndict
            return returndict
        # create exception handling in case something goes wrong 
        except:
            # print error message
            print("line_nums_list is not a variable in line with the assumptions for this method.")
            # return empty returndict
            return returndict
        # pass

    def get_dictionary_range(self, ran:list[int]):
        '''
        Method to read from range of values provided in ran from the file from 
        returns questions, stimuli and answers in the dictionary format
        parameter ran contains a list of two integer values (first value = starting value (inclusive of this value) & last value = ending value(inclusive of this value))
        Even though it was specified that no int in ran should be smaller than 0, since line 0 in the file is never 
        used because the format in which question, stimulus and answers are provided at are defined there 
        --> the starting value may never be 0 
        thus it starts from line 1 where actual questions, stimuli and answers are stored
        '''
        # try to run this code
        try: 
            # get length of file (amount of file numbers) from parent class (uses ineritace)
            lengthOfFile = self.line_count()
            # check that parameters are integers; check if more than 2 vals in list; check if first val higher than second; check if any val negative; if val largar than lines in file
            if not all(type(line) is int for line in ran) or (len(ran) != 2) or (ran[0] > ran[1]) or (ran[0] <= 0 or ran[1] <= 0) or (ran[0] > lengthOfFile or ran[1] > lengthOfFile):
                # return that the formatting is wrong and say what to check for
                return "ran parameter is in the wrong format. Check that only two values are in the list, the starting value is smaller than ending value, the values in the list are integers, the line numbers are not smaller than 1 and do not exceed the number of lines in the file." 
            
            # if in correct format return the lines in dictionary format in dictionary format
            # get the questions in the file in dictionary format
            all_questions = self.all_dictionary_questions()
            # create returndictionary
            returndict = {}
            # create new key
            new_key = 1
            # loop over the all_questions dictionary
            for key, val in all_questions.items():
                # if key within range provided (inclusive of first and last value)
                if key >= (ran[0]) and key <= (ran[1]):
                    # add key and value to returndict
                    returndict[new_key] = val
                    # increment new_key
                    new_key += 1
            # return returndict
            return returndict
        # exception handling
        except:
            return "Oops. Something went wrong."
        # pass

    def random_dicitonary_questions(self):
        '''
        Method to read the questions from a random line range (between a start value and a stop 
        value, inclusive of both)
        It is not read from the dile but inheritance is used since thus it would be redundant code
        Even though it was not specified like this: 1 and not 0 is chosen to be the first line number,
        since line 0 in the file is never used because the format in which question, stimulus and answers are provided at are defined there 
        --> the starting value may never be 0 
        '''
        # try to run this code
        try: 
            # import random to get random line numbers
            import random
            # create empty list to store start and end value in
            lines = []
            # assign line_count to filelength variable; line count retreived from line_count method in parent variable (uses inheritance)
            # adding counting again would make the code redundant
            filelength = self.line_count()
            # set counter to 0
            i = 0
            # loop twice to create two line numbers
            while i < 2:
                # create random line number using random.randint; filelength-1 because it includes line 0 which we do not use 
                random_line_number = random.randint(1, filelength-1)
                # no duplicate questions
                if random_line_number not in lines: 
                    # append random line to lines dictionary
                    lines.append(random_line_number)
                    # increment i 
                    i+=1
            # get dictionary questions from other method in child class: reading and converting again would add redundance
            all_questions = self.all_dictionary_questions()
            # create returndicitonary
            return_dict = {}
            # set start to smaller value = start line
            min_random_lines = min(lines)
            # j is the keys for the range of qustions, starting at 1
            j = 1
            # values = list(all_questions.values)
            while min_random_lines <= max(lines):
                # adds the question package with the new key to the return dictionary
                return_dict[j] = all_questions[min_random_lines]
                # increment i
                min_random_lines +=1
                # increment j (key)
                j+=1
            # return the return_dict
            return(return_dict)
            # pass
        # add exception handling in case something else goes wrong
        except:
            # return error message
            return "Oops. Something went wrong."


    def exclude_dictionary_questions(self, line_nums_list:list): 
        '''
        line_nums_list (list): the list of line numbers to exclude from the questions.
        Method to return the questions, simuli, and associated answers, in the file in the dictionary  format.
        Assumed: all line numbers in the list are contained in the file and there are no duplicate 
        line numbers listed.
        '''
        # try to run this code
        try:
            # get dictionary for all questions from method in parent class
            all_questions = self.all_dictionary_questions()
            # create new key
            new_key = 1
            # loop over the list of lines to be excluded
            for line_num in line_nums_list:
                # delete the question at the line number specified line number 1 is question 1
                del all_questions[line_num]
            # create return dictionary
            return_questions = {}
            # loop over remaining questions
            for item in all_questions.values():
                # add the qustion to the return dictionary
                return_questions[new_key] = item
                # increment new_key
                new_key +=1
            # return the questions
            return return_questions 
            # pass
        #exception handling
        except:
            # return error message if something went wrong
            return "Oops. Something went wrong."

    def exclude_dictionary_range(self,questions_range:list[int]): 
        '''
        Even though it was not specified like this: 1 and not 0 is chosen to be the first line number,
        since line 0 in the file is never used because the format in which question, stimulus and answers are provided at are defined there 
        --> the starting value may never be 0 
        questions_range (list): two item integer list, containing the range of questions numbers to exclude (inclusive of both values)
        return questions, stimuli and associated answers that are not excluded
        error handling in this question, including:
        • Making sure that questions_range is of type list and that it only contains integers
        • The line numbers provided in the list are available in the file
        '''
        # try to run this code
        try: 
            # get dictionary for all questions from method in parent class
            all_questions = self.all_dictionary_questions()
            # get length of file using parent class (uses inheritance)
            lengthOfFile = self.line_count()
            # make sure that questions_range of type list and that it only contains ints and line nums provided have to be available in file 
            if not all(type(line_no) is int for line_no in questions_range) or (len(questions_range) != 2) or (questions_range[0] not in all_questions.keys() or questions_range[1] not in all_questions.keys()):
                # return error message
                return "The range of question numbers is in the wrong format. Check that it is a list of two integers, within the number of questions: %s." % (lengthOfFile-1)
            else: 
                # create returndict
                returndict = {}
                # create new_key
                new_key = 1
                # loop over the all_questions dictionary
                for key, val in all_questions.items():
                    # if key within range provided 
                    if not key >= (questions_range[0]) or not key <= (questions_range[1]):
                        # add key and value to returndict
                        returndict[new_key] = val
                        # increment new_key
                        new_key += 1
                # return returndict
                return returndict
        # exception handling in case something else goes wrong
        except:
            # return error message
            return "Oops. SOmething went wrong."

# in_file_1 = QuestionFileReader("python-game-file.txt")
# small_question_set = in_file_1.read_all()
# print(small_question_set)