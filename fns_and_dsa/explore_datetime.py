from datetime import datetime, timedelta

def display_current_datetime():
  """
  This function gets the current date and time, formats it, and prints it.
  """
  current_date = datetime.now()
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current Date and Time: {formatted_datetime}")
  

# Call the function to display the current date and time
display_current_datetime()



def calculate_future_date():
    x = (int(input("Enter the number of days to add to the current date:")))
    future_date = datetime.now() + timedelta(days=x)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date}")

calculate_future_date()
    
    
