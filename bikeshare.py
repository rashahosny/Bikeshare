#the used pages are:
#https://www.geeksforgeeks.org
#https://pandas.pydata.org/pandas-docs
#
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Define the lists that hold months and days

months=['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all' , 'monday', 'tuesday', 'wensday', 'thrusday', 'friday', 'saterday', 'sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop   to handle invalid inputs
    
    while True:
        cities = ["chicago", "new york city", "washington"]
        city_selection = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city_selection in cities:
            city=CITY_DATA[city_selection.lower()]
            break
        
    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in months:
        month_name = input('Please select a month from the following (january, february, march, april, may, june) or just print "all"\n')
        if month_name.lower() in months:
            #get name of the month to analyze data and set it to month variable.
            month=month_name.lower()
        else:
            #set an error message to the user that we were not able to get the name of the month and the loop will continue.
            print("Sorry we were not able to get the name of the month to analyze data, Please select a month from the following (january, february, march, april, may, june) or just print 'all'.\n")  
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in days:
        day_name = input('Please enter the required day (monday, tuesday, wensday, thrusday, friday, saterday, sunday) or just print "all"\n')
        if day_name.lower() in days:
           #get name of the day to analyze data and set it to month variable.
            day = day_name.lower()
        else:
            #set an error message to the user that we were not able to get the name of the day and the loop will continue.
            print("Sorry we were not able to get the name of the day to analyze data, Please enter the required day (monday, tuesday, wensday, thrusday, friday, saterday, sunday) or just print 'all'.\n")    
    print('-'*40)
        
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour']= df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df
 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print("The most common month from the requested data is: " , common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print("The most common day from the requested data is: " , common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()
    print("The most common hour from the requested data is: " , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print("The most common Start Station for this city is: " , common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print("The most common Start Station for this city is: " , common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination=(df['Start Station']+df['End Station']).mode()
    print('the most frequent combination of start station and end station trip is: ', str(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print ('the total duration time is : '+str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print ('the average duration time is : '+str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df.get('User Type').value_counts()
    print('the counts of user types is: \n', user_type)
    
    # TO DO: Display counts of gender
    if 'Gender' in df['Gender']:
        gender=df['Gender'].count()
        print('the counts of gender is: ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthdate =df['Birth Year'].min()
        recent_birthdate =df['Birth Year'].max()
        common_birthdate =df['Birth Year'].mode()
        print('The earliest birth date is: {}, the recent birth date is: {} and the most common birth date is: {}'.format(earliest_birthdate, recent_birthdate, common_birthdate))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        test_answer = input ('Do you want to display 5 lines of raw data? please press y or n')
        while test_answer=='y':
            raws= df.head()
            print (raws)
            test_answer = input ('Do you want to display 5 lines of raw data? please press y or n')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




