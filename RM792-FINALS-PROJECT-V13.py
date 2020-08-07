import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("----------------------------------------------------------------------------------------")

print ("   ---   QUEENS COLLEGE   ---   RM 792   ---   SUMMER 2020   ---   Final Project   ---   Tage N Singh\n\n")

print(" This project is designed to demonstrate the principles taught in the RM 792 class \n")

print(" The features of the program include : \n")

print(" 1 - The use of 3 Data Sources, 2 of which are located on Github and are accessed over the internet when the program is Executed \n")

print(" 2 - The use of 2 Lists, 2 digit state codes and state names. The state name is published upon the selection of the 2 digit state code \n")

print(" 3 - The use of an integer based list of years that is verified within the  list and then used to pull data from the web data source\n")

print(" 4 - The use of while statements to validate user inputs and prevent inaccurate input data\n")

print(" 5 - ThE use of Matplotlib to extract data from the web source and print line graphs depending on the user inputs\n")

print(" ALL DATA USED FOR THIS PROJECT IS SOURCED FROM THE PUBLIC DOMAIN\n")

print("\n\n")

print("----------------------------------------------------------------------------\n")

print ("     -----     PRESS RETURN TO EXECUTE THE PROGRAM !     -----     ")
input()

# - local file install dfgeneral = pd.read_csv (r'C:\Users\tsingh\OneDrive\Documents\Education\CUNY - Risk Management\RM792-SUMMER-2020\projects\RM792-Final\Project-Data-Final.csv',header = 0)

dfgeneral = pd.read_csv (r'https://raw.githubusercontent.com/tagensingh/RM792-FINAL/master/Project-Data-Final.csv',header = 0)

dfgeneral2 = pd.read_csv (r'https://raw.githubusercontent.com/tagensingh/RM792-FINAL/master/Project-Data-Final.csv',header = 0)

dfgeneral3 = pd.read_csv (r'https://raw.githubusercontent.com/tagensingh/RM792-FINAL/master/median-hh-inc.csv',header = 0)

stcode = ("AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY")

statename = ("Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming")

yearcheck = [1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988]


print("THIS PROJECT EXAMINES THE RELATIONSHIP BETWEEN US BIRTHS AND GDP FROM 1969 TO 1988", "\n")

print(" -- The datafile for this project is located on github for demonstration purposes -- ")

state = input("Enter a state Code     :     ").upper()

# To manage the correct input for the state code input

while state.upper() not in stcode:

    state = input("Enter a 2 digit state Code -OR X to EXIT    :     ").upper()

    if state == 'x':
        break
    elif state =='X':
        break
    elif state.upper() in stcode:

        continue

indexstcode = stcode.index(state.upper())

#print(indexstcode)

year = input("What Year from the Dataset - '1969 - 1988'     :     ")
yearin = int(year)

# -  Check input data type -print(type(year))

# - Check input conversion datat type -print(type(yearin))

# To manage the correct input for the year input
while yearin not in yearcheck:

    year = input("Enter a 4 digit year between 1969 and 1988 or X to EXIT     :     ")
    yearin = int(year)
    if year == 'x':
        break
    elif year =="X":
        break
    elif yearin in yearcheck:

        continue

print("\n\n")

print("----------------------------------------------------------")

print ("Press return to view the structure of the Dataset")
input()

print(" The Dataset from the imported .csv is as follows - A Sample","\n")

print(dfgeneral.head(3),"\n\n")

print("----------------------------------------------------------")

print ("Press return to view the State and Date Information")

input()

if state.upper() == 'DC':

    print(" Your Inquiry is for the :",(statename[indexstcode]),"in the Year :", yearin,"\n\n")

else:

    print(" Your Inquiry is for the state of :",(statename[indexstcode]),"in the Year :", yearin,"\n\n")



statename_actual = (statename[indexstcode])

statebirths = state+"-Births"

stategdp = state+"-GDP"

# The Following lines is for testing the outputs

#print("------------------------------")

#print(statebirths)

#print(stategdp)

#print(yearin)

#print("------------------------------------")

# -  End of Test Outputs lines


# -  Setting up the process for printing the records specific for the State and Year

dfgeneral.set_index("Year", inplace=True)

# -    Works ---print(dfgeneral.loc[yearin, [statebirths,stategdp]])

statebirths_f = dfgeneral.loc[yearin, [statebirths]]

statebirths_actual = (int(statebirths_f))

usbirths_f = dfgeneral.loc[yearin, ['US-Births']]

usbirths_actual = (int(usbirths_f))

statebirths_percent = (statebirths_actual * 100/usbirths_actual)

stategdp_f = dfgeneral.loc[yearin, [stategdp]]

stategdp_actual = (float(stategdp_f)*1000)

usgdp_f = dfgeneral.loc[yearin, ['US-GDP']]

usgdp_actual = (float(usgdp_f)*1000)

stategdp_percent = (stategdp_actual * 100/usgdp_actual)


print("----------------------------------------------------------")

print ("Press return to view the results of your Inquiry")
input()

print("Births for ",statename_actual,"in",year,":", '{:,.0f}'.format(statebirths_actual),"\n")

print("Births for the United States in",year,":", '{:,.0f}'.format(usbirths_actual)," - ",statename_actual," was ",'{:,.2f} %'.format(statebirths_percent)," of the US total births""\n\n\n")

print(" All GDP data are quoted in 2020 Dollars \n")

print("GDP for ",statename_actual,"in",year,":", '$ {:,.0f}'.format(stategdp_actual),"\n")

print("GDP for the United States in",year,":", '$ {:,.0f}'.format(usgdp_actual)," - ",statename_actual," contributed ",'{:,.2f} %'.format(stategdp_percent)," to the US total GDP""\n")

##  --  The following is a plot of the Births for the period 1969 to 1988
print("\n\n")

print ("Press return to view the Graph of Births in the State in question for the 20 year perion 1969 - 1988")

input()

plt.plot(dfgeneral2['Year'], dfgeneral2[statebirths], color='red', marker='o')
plt.title("Births for "+statename_actual+" 1969 to 1988", fontsize=14)
plt.xlabel('Year', fontsize=6)
#plt.set_xticklabels(plt.xlabel.astype(int))
plt.ylabel("# of New Babies", fontsize=6)
plt.grid(True)
plt.show()

print("\n\n")


print ("Press return to view the Graph of the GDP of the State in question for the 20 year perion 1969 - 1988")
input()

##  --  The following is a plot of the state GDP for the period 1969 to 1988

plt.plot(dfgeneral2['Year'], dfgeneral2[stategdp], color='green', marker='*')
plt.title("GDP for "+statename_actual+" 1969 to 1988", fontsize=14)
plt.xlabel('Year', fontsize=6)
plt.ylabel("GDP", fontsize=6)
plt.grid(True)
plt.show()

print("\n\n")

print ("Press return to view the Graph of the Median Household Income for the 20 year perion 1969 - 1988")
input()

##  --  The following is a plot of the state GDP for the period 1969 to 1988

plt.plot(dfgeneral3['Year'], dfgeneral3['Median_HH_Inc'], color='blue', marker='s')
plt.title("Median Household income for 1969 to 1988 - Inflation Adjusted 2019", fontsize=14)
plt.xlabel('Year', fontsize=6)
plt.ylabel("Median HH Income", fontsize=6)
plt.grid(True)
plt.show()

print("\n\n")

print(" This ends the project for RM 792 - Queens College - CUNY  ---  Tage N Singh")



