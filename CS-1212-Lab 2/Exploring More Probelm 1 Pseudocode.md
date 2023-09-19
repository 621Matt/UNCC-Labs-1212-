Begin Block

Display(Please enter the number of teachers and apples.)
Input (teacher = User entered number)
Input (apple = User entered number)

IF apple >= teacher THEN
    OUTPUT 
        apple_for_teacher = apple // teacher
        remainder = apple % teacher
        Display(Each teacher gets, apple_for_teacher, apples)
        Display(Apples left in basket: remainder)
ELSE 
    OUTPUT
        Display(Not enough apples to evenly distribute.)

End Block