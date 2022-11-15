import csv
from datetime import datetime
# Import Statements - Added by Karthika V - Start code
import datetime
import calendar
# Import Statements - Added by Karthika V - End code
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    # Added By Karthika V - Start Code
    # print(temp)
    return f"{temp}{DEGREE_SYBMOL}"
    # Added By Karthika V - End Code


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Added By Karthika V - Start Code
    date_string =""
    if(iso_string !=None):
        date_string =datetime.datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
        year =date_string.strftime("%Y")
        month = date_string.strftime("%m")
        datetime_object = datetime.datetime.strptime(month, "%m")
        month_name = datetime_object.strftime("%B")
        date_d= date_string.strftime("%d")
        day= date_string.strftime('%A')
        date_result = day +" "+date_d+" "+month_name+" "+year
        # print(f"The human readable date is : {date_result}")
        return date_result
    # Added By Karthika V - End Code
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    # Added By Karthika V - Start Code
    temp_in_farenheit = float(temp_in_farenheit)
    # print(f"The tempertaure in Farenheit is : {temp_in_farenheit}")
    temp_in_cel = float((temp_in_farenheit - 32) * 5/9)
    temp_in_celcius = round(temp_in_cel,1)
    # print(f"The tempertaure in Celcius is : {temp_in_celcius}")
    return temp_in_celcius
    # Added by Karthika V - End Code
    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # Added by Karthika V - Start Code
    # print(f"The temperature list to calculate the mean of list is : {weather_data}")
    sum = 0
    mean_list =0
    for i in range(len(weather_data)):
        sum = float(weather_data[i]) +sum
    mean_list = sum/len(weather_data)
    # print(f"The mean value from a list of numbers is : {mean_list}")
    return mean_list
    # Added by Karthika V - End Code
    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # Added by Karthika V - Start Code
    f = open(csv_file,'r')
    with f:
        skip_heading =next(f)
        readMe = csv.reader(f)

        date_data_list =[]

        for i in readMe:
            if not(i):
                # print("Executing Empty Lines")
                continue
            date_data_list.append(i)
            
        # print(date_data_list)
        for n in range(len(date_data_list)):
            num1 = int(date_data_list[n][1])
            num2 = int(date_data_list[n][2])
            date_data_list[n][1] =num1
            date_data_list[n][2]= num2
            
        # print(date_data_list)

    return date_data_list
    # Added by Karthika V - End Code
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    # Added by Karthika V - Start Code
    min_weather_data =0
    min_position = 0
    if(len(weather_data)!= 0):
        min_weather_data =float(weather_data[0])
    else:
        return ()
    for i in range(len(weather_data)):
        if(float(min_weather_data)>=float(weather_data[i])):
            min_weather_data = float(weather_data[i])
            min_position = i

    # print(f"The Minimum weather value from the list is : {min_weather_data} and it position is :{min_position}")
    return min_weather_data, min_position
    # Added by Karthika V - End Code
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    # Added by Karthika V - Start Code
    max_weather_data =0
    max_position = 0
    if(len(weather_data)!= 0):
        max_weather_data =float(weather_data[0])
    else:
        return ()
    for i in range(len(weather_data)):
        if(float(max_weather_data)<=float(weather_data[i])):
            max_weather_data = float(weather_data[i])
            max_position = i

    # print(f"The Maximum weather value from the list is : {max_weather_data} and it position is :{max_position}")
    return max_weather_data,max_position
    # Added by Karthika V - End Code
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Added by Karthika V - Start Code
    
    min_temp_list =[] 
    max_temp_list =[]
    sum_low =0
    sum_high =0
    low_mean_in_f =0 
    high_mean_in_f = 0

    for i in range(len(weather_data)):
        min_temp_list.append(weather_data[i][1])
        max_temp_list.append(weather_data[i][2])

    # Calculating Mean of Minimum temperatures
    for n in range(len(min_temp_list)):
        sum_low = sum_low+min_temp_list[n]
    low_mean_in_f = sum_low/(len(min_temp_list))

    # Calculating Mean of Maximum temperatures
    for k in range(len(max_temp_list)):
        sum_high = sum_high+max_temp_list[k]
    high_mean_in_f = sum_high/(len(max_temp_list))
    
    # Getting the value of Mimimum and Maximum temperatures by calling the respective Functions.
    low_temp_in_f , low_temp_position = find_min(min_temp_list)
    high_temp_in_f, max_temp_position= find_max(max_temp_list)

    # Getting the date for Minimum and Maximum temperature
    for s in range(len(weather_data)):
        if(low_temp_position == s):
            date_for_low_temp = weather_data[s][0]
        if(max_temp_position == s):
            date_for_high_temp =weather_data[s][0]

    # Formatting the date in Human readable format Using convert_date Function call
    format_date_for_low_temp= convert_date(date_for_low_temp)
    format_date_for_high_temp =convert_date(date_for_high_temp)

    # Converting the temperarture from Fahrenheit to Celsius using convert_f_to_c function call.
    low_temp_in_c = convert_f_to_c(low_temp_in_f)
    high_temp_in_c = convert_f_to_c(high_temp_in_f)
    low_mean_in_c = convert_f_to_c(low_mean_in_f)
    high_mean_in_c =convert_f_to_c(high_mean_in_f)

    # Adding the degree Symbol and Letter C for Temperatures using format_temperature Function call.
    formated_low_temp_in_c= format_temperature(low_temp_in_c)
    formated_high_temp_in_c = format_temperature(high_temp_in_c)
    formated_low_mean_in_c = format_temperature(low_mean_in_c)
    formated_high_mean_in_c =format_temperature(high_mean_in_c)

    # Processing the date to be printed.
    first_line = f"{len(weather_data)} Day Overview\n"
    second_line = f" The lowest temperature will be {formated_low_temp_in_c}, and will occur on {format_date_for_low_temp}.\n"
    third_line = f" The highest temperature will be {formated_high_temp_in_c}, and will occur on {format_date_for_high_temp}.\n"
    fourth_line =f" The average low this week is {formated_low_mean_in_c}.\n"
    fifth_line = f" The average high this week is {formated_high_mean_in_c}.\n"

    # Processing summary Data message.
    summary_data = f"{first_line} {second_line} {third_line} {fourth_line} {fifth_line}"
    
    return summary_data
    # Added by Karthika V - End Code
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Added by Karthika V - Start Code
    daily_summary_data =""

    for i in weather_data:
        # Formatted Date element
        format_date = convert_date(i[0])

        # Format Min Temperature
        format_min_temp = convert_f_to_c(i[1])
        format_min_temp_in_c = format_temperature(format_min_temp)

        # Format Max Temperature
        format_max_temp = convert_f_to_c(i[2])
        format_max_temp_in_c = format_temperature(format_max_temp)

        # Processing the daily summary data
        single_summary_data = f"---- {format_date} ----\n  Minimum Temperature: {format_min_temp_in_c}\n  Maximum Temperature: {format_max_temp_in_c}\n\n"
        daily_summary_data = daily_summary_data + single_summary_data

    # print(daily_summary_data)
    return daily_summary_data
    # Added by Karthika V - End Code
    pass
