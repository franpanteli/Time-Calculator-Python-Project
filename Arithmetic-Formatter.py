"""
    -> We are defining a Python function, called `arithmetic_arranger`
    -> The first argument of this function is a list of strings, with operations 
    -> The second arguement of this function is an optional boolean, which instructs it to return the result of these 
        operations 
    -> These are entered into the first argument of the function, in a list 
    -> We want the function to return them in a vertically stacked display 
"""

def arithmetic_arranger(problems, answer=False):

"""
    -> The first argument of the function is a list of the different operations which we want to stack 
    -> If we have too many operations (more than 4 of them) for this first argument, then we want to return an error message
    -> This section of the function checks the number of these arguments, to see if we have too many of them
"""

    if len(problems) > 5:
        return "Error: Too many problems."

# We then define four empty arrays, to store the operations of the first argument in the function in
    first_line, second_line, third_line, fourth_line = [], [], [], []

"""
    Iterating through problems to implement error handling:
        -> The first argument to the function is an array of operations 
        -> Those operations all follow the same basic form <- Some number, ± some other number 
        -> We are iterating through each of those operations listed in the first argument of the function <- This is why 
            we are using a for loop (each of those operations in the list is a `problem`)
        -> And each of those is in that same basic form <- Or we want to make sure that it is 
        -> The basic form is 'number ± other number' 
        -> If this isn't the case, we want to return an error message
        -> So we need the operand to be a ±, and if this isn't we return an error message
        -> This is us implementing the error handling which the question asked for (refer to the project task notes for this)
        -> We have to implement an error handler for each condition that we want the function input to satisfy
        -> Another condition that we are checking in this block is that the operation only contains digits <- In the 
            alternative case, returning another error message
        -> And finally, that the number of digits in the numbers being operating on isn't greater than 4
"""

    for problem in problems:
        pieces = problem.split()
        first, operator, second = pieces

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        third_line.append('-' * width)

        if answer:
            result = str(eval(problem))
            fourth_line.append(result.rjust(width))

"""
    -> The function can take two arguments 
    -> The first is a list, which contains the operators we are rearranging - and the second is an optional boolean (`argument`)
        -> `argument` determines if we want to return the result of these operations, or not 
    -> The first line in this block constructs the result of the function which we want to return if its second argument doesn't
        exist 
    -> In which case, we format the different lines of the function output: 
        -> The first argument of the function follows a certain form 
            -> First number, operand (±), second number
            -> The previous block of code stores these three values in different variables 
            -> We are taking these and formatting them into a vertically stacked output <- This is stored in the `arranged_problems` 
                variable 
        -> We add spaces, then the first variable, then a new line, then etc - to build the function output, in the syntax defined by 
            the project question
        -> One of these elements is the '---' dashes under the operation <- The number of these dashes was determined in the previous block 
            of code - depending on the number of digits being worked with in a given case
    -> Then if the second argument to the function is True (`argument`), we want to add a fourth line to its output - and we want the 
        content of that line to contain the results of the operation
        -> This is what the if block in this section of code does
        -> Printing this out onto its own line, by literally joining a new line, four spaces and the value of the operation 
        -> Provided that the second argument to the function is True <- This argument is optional 
    -> We are storing the formatted operation in a variable called `arranged_problems`
    -> This is what we then return, as a string 
"""

    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    if answer:
        arranged_problems += "\n" + "    ".join(fourth_line)
    return arranged_problems