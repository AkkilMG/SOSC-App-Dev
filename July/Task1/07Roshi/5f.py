def print_pattern(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end=" ")
        for k in range(i + 1):
            print("*", end=" ")
        print()
print_pattern(4)


"""OutPut:
      * 
    * * 
  * * * 
* * * *  """