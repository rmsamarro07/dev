def initialize_half_diamond(center_count):
    #initialize the upper part of the diamond
    for upper_asterisk in range(0, center_count, 1): # 
        for j in range(0, upper_asterisk + 1): #
            print("*", end = "")
        print("")

    #initialize the lower part of the diamond
    for lower_asterisk in range(1, center_count, 1):
        for j in range(lower_asterisk, center_count, 1):
            print("*", end = "")
        print("")

center_count = 6
initialize_half_diamond(center_count)
