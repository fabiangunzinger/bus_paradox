import random
import numpy as np

def simulate_bus_arrivals(n = 1000000,
                          tau = 10,
                          rseed = 231296):
    """
    Simulates the arrival of n buses that are scheduled to arrive every tau minutes.
    """
    np.random.RandomState(rseed)
    return n * tau * np.sort(np.random.rand(n))


def simulate_wait_times(arrival_times,
                           n=1000000,
                             rseed=231286):
    """
    Calculate the waiting time for each arriving passenger.
    """
    # Simulate customer arrival times (between 0 and arrival of last bus)
    np.random.RandomState(rseed)
    arrival_times = np.array(arrival_times)
    passenger_times = arrival_times.max() * np.sort(np.random.rand(n))
    
    # Find the index of the next bus for each simulated customer
    i = np.searchsorted(arrival_times, passenger_times, side='right') 

    return arrival_times[i] - passenger_times