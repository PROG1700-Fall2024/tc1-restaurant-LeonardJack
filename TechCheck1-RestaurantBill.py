#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    billAmt = float(input("Enter your bill amount: ")) #takes in bill amount

    billTax = billAmt * 0.15                  #calculation for tax
    billTip = billAmt * 0.20                    #calculation for tip
    billTotal = billAmt + billTax + billTip     #calculation for total

    print("The original bill amount is: {0:.2f}\nYour tax is:  {1:.2f}\nYour tip is: {2:.2f}\nYour total is: {3:.2f}".format(billAmt, billTax, billTip, billTotal))



    # YOUR CODE ENDS HERE

main()