# Programming-lab exercise n. 1 of Friday 10 November 2023
# --------------------------------------------------------
#
# Write a function that gets two strings representing filenames input_file and output_file.
# The input_file contains several rows with numbers separated by whitespaces and tabs.
# The function must write in output_file the averages of the numbers found in every row,
# in the same order and return the maximum computed average.

# Example: if input_file has the following content:
# 1 5 7
# 3 1.4 12
#
# the function has to return the value 5.466666666666666 
# and write the following lines in output_file:
# 4.333333333333333
# 5.466666666666666

# SOLUTION

def average_file(input_file , output_file):

    #First of all we read all the lines of the input file
    with open(input_file, "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()
    
    # Then we transform the contents of each row
    # into a list of the numbers (float) it contains
    numbers_list = [list(map(float,line.split())) for line in lines]

    # We create a list that contains the average of each list of line numbers
    #averages_list = [sum(line)/len(line) for line in numbers_list]
    averages_list = []
    for line in numbers_list:
        average = sum(line)/len(line)
        if average.is_integer():
            average = int(average)
        averages_list.append(average)

    # We print each media on one line of the output file
    # Note that using lists preserves the order
    # and list-average correspondence
    with open(output_file, "w", encoding="utf-8") as f_out:
        for average in averages_list[:-1]:
            print(average, file=f_out)
        print (averages_list[-1], end = "", file=f_out)

    # The function returns the maximum of the list of averages
    return max(averages_list)

if __name__ == "__main__":
    test_dict = {
        "test01.txt":"test01_out.txt",
        "test02.txt":"test02_out.txt"
    }
    for input_file, output_file in test_dict.items():
        m = average_file(input_file, output_file)
        print(input_file,  "-->", output_file,": ", m)