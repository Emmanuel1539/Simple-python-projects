"""
Author: EKENEDO NZUBE EMMANUEL  

PURPOSE: The purpose of this project is to get year and country that has the lowest and highest and largest drop in life expectancy in the dataset.
        It also allows the user to type in a year of interest, then, find the average life expectancy for that year. 
        Then find the country with the minimum and the one with the maximum life expectancies for that year. 
        An extra deep dive was made to determine the country and year with largest drop in life expectancy  in the dataset.
"""


#Initialize variables for all the cases
lowest_expectancy = 300 #we start checking from the hieghest number
highest_expectancy = -1 # we start checking from the lowest number 
lowest_country = ''
max_country = ''

#Initialize variables for a particular year
interest_year_max = -1
interest_year_min = 300
interest_country_max = ''
interest_country_min = ''
total_life_expectancy = 0
total_num_countries = 0

# Variables to track the largest drop
largest_drop = 0
drop_year = ''
drop_country = ''

# variables to check from the previous year to next year 
prev_life_expectancy = None
prev_year = None
prev_country = None

# request for the user year of interest
interested_year = int(input('Please enter the year of interest: '))


# fetching the csv file name 
with open(r'C:\Users\USER\Desktop\BYU COURSE\BYU ASSOCIATE PROJECTS\BYU PYTHON PROJECT FOLDER\life-expectancy.csv') as file:
    next(file) #to drop the 'header'
    for line in file: #loop through each lines
        clean_line = line.strip() # cleaning the file
        lines = clean_line.split(',') #spliting the lines with comas
       
        country = lines[0]
        code = line[1]
        year = int(lines[2]) #converting year values to integer
        life_expectancy = float(lines[3]) # converting life expectancy values to float
        
        
        #checking for the life expectancies of all cases
        #checking for the min country and year
        if life_expectancy < lowest_expectancy:
            lowest_expectancy = life_expectancy
            lowest_country = country
            min_year = year   
         
        #checking for the max country and year
        if life_expectancy > highest_expectancy:
            highest_expectancy = life_expectancy
            max_country = country
            max_year =  year
            
        
        # checking for life expectancies of a particular year of interest
        if year == interested_year:
        
            #check for the aveerage life expectancy of user's year of interest
            total_life_expectancy += life_expectancy
            total_num_countries += 1
            average_life_expectancy = total_life_expectancy / total_num_countries

            #checking for the max year of interest
            if life_expectancy > interest_year_max: 
                interest_year_max = life_expectancy
                interest_country_max = country
                
            # checking for the min year of interest
            if life_expectancy < interest_year_min:
                interest_year_min = life_expectancy
                interest_country_min = country
                
         # checking for the largest drop in country and year 
        if prev_life_expectancy is not None:
            drop = prev_life_expectancy - life_expectancy
            
            # Checking if the current drop is larger than the previous largest drop
            if drop > largest_drop:
                largest_drop = drop
                drop_year = prev_year
                drop_country = prev_country
                
        prev_life_expectancy = life_expectancy
        prev_year = year
        prev_country = country
            
            
        
print()        
print(f'The country with the lowest life expectancy is: {lowest_country} and lowest life expectancy is: {lowest_expectancy} in {min_year}')
print(f'The country with the highest life expectancy is: {max_country} and highest life expectancy is: {highest_expectancy} in {max_year}')
print()
print(f'The average life expectancy across all countries in {interested_year} is: {average_life_expectancy:.2f}')
print(f'The manximum life expectancy for the year {interested_year} is {interest_year_max} in {interest_country_max}')
print(f'The minimum life expectancy for the year {interested_year} is {interest_year_min} in {interest_country_min}')
print()
print(f"The country with the largest drop in life expectancy is:{drop_country} in {drop_year} with largest drop of {largest_drop:.2f}")

