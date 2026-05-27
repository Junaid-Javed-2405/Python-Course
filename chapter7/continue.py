for i in range(1,11):
    if(i==6):
        continue # skip this statement when i is equal to 6 and continue with the next iteration of the loop. The continue statement can be used in both for and while loops. When the continue statement is executed, the rest of the code inside the loop will be skipped for the current iteration and the loop will continue with the next iteration. If there are nested loops, the continue statement will only affect the innermost loop in which it is present. 
    else:
        print(i)