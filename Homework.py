"""
Lesson 2: Assignments | Tuples
1. Tuple Mastery in Python
Task 1: Formatting Flight Itineraries
Create a Python function that takes a list of tuples as an argument. 
Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
The function should format and return a string that lists each itinerary. 
For example, if the input is 
"""
flights =[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
"""
the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
"""
print()
def format_itineraries(flights):
    for i, flight in enumerate(flights):
        traveler_name, origin, destination = flight
        print(f"Itinerary {i+1}: {traveler_name} - From {origin} to {destination}")

format_itineraries(flights)
print("\n")
"""
2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. 
Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:
"""
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
"""
Add functionality to insert new books into library.
Ensure that adding a duplicate book is handled appropriately.
"""
def add_book(library, new_book):
    if new_book in library:
        return f"Error: '{new_book[0]}' is already in the library."
    library.append(new_book)
    return(library)

library = add_book(library, ("The Lord of the Rings", "J.R.R. Tolkien"))
print("Add 'Lord of the Rings': \n -->", library ,"\n")

library = add_book(library, ("1984", "George Orwell"))
print("Add '1984': \n -->", library,"\n\n")
"""
3. Python Loops and Tuples in Analytical Applications
Task 1: Stock Market Data Analysis
Problem Statement:
You have been provided with stock market data, where each data point is a tuple containing
a company's stock symbol, the date, and the closing price. 
Your task is to analyze this data to find the average closing price of a specified stock over a given period.

Sample Data:
"""
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0)
]
"""
Create a function to calculate the average closing price of a specific stock symbol over all dates.
Ensure your solution handles cases where the stock symbol does not exist in the data.
"""
def calculate_average_price(stock_data, symbol):
    prices_for_stock_list = [data[2] for data in stock_data if data[0] == symbol]
    return sum(prices_for_stock_list) / len(prices_for_stock_list) if prices_for_stock_list else None

for stock in ["AAPL","MSFT","GOOG"]:
    average_price = calculate_average_price(stock_data, stock)
    print(f"Average closing price of {stock}: {average_price}")

print("\n")
"""
Task 2: Event Attendance Tracker
Apply loops and tuples to track and report on event attendance.

Problem Statement:
Your goal is to manage an attendance system for various events. 
Each attendee's data is stored as a tuple containing their name and the event they attended.

Develop a function to list all attendees of a specific event.
Implement a feature to count the number of attendees for each event.
Example Attendee Data:
"""
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit")
]
def list_names_by_event(attendees, event):
    return [name for name, event_in_list in attendees if event_in_list == event]

def count_per_event(attendees):
    event_dict = {}
    for dummy, event in attendees:
        if event not in event_dict:
            event_dict[event] = 0
        event_dict[event] += 1
    return event_dict

event = "Python Conference"
print(event, "Attendees:", list_names_by_event(attendees, event), "\n")  
print("Count Per Event:", count_per_event(attendees), "\n")  