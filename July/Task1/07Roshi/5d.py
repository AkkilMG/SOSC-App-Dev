def print_pattern(rows):
    for i in range(rows):
        for j in range(i):
            print(" ", end="")

        for k in range(rows - i):
            print("* ", end="")
        print()
print_pattern(4)


"""OutPut:
* * * * 
 * * * 
  * * 
   *   """