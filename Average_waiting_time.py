# Approach
# Initialize Variables:

# current_time to track the chef's current available time.
# total_waiting_time to accumulate the waiting times of all customers.
# Process Each Customer:

# For each customer, if they arrive after the chef is available, update the chef's current_time to the customer's arrival time.
# Compute the time the chef will finish the current customer's order and update current_time.
# Calculate the waiting time for the current customer and add it to total_waiting_time.
# Calculate Average:

# After processing all customers, divide total_waiting_time by the number of customers to get the average waiting time.
# Return the Result:

# Return the computed average waiting time.
# Complexity
# Time complexity: (O(n))

# We iterate through the list of customers exactly once, performing constant time operations for each customer.
# Space complexity: (O(1))

# We use a fixed amount of extra space regardless of the input size.
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        
        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            current_time += time
            total_waiting_time += (current_time - arrival)
        
        return total_waiting_time / len(customers)
