import random
import numpy as np

def simulate_bus_arrivals(n = 1000000,
                          tau = 10,
                          rseed = 231296):
    """
    Simulates the arrival of n buses that are scheduled to arrive every tau minutes.
    """
    np.random.RandSeed(rseed)
    return n * tau * np.sort(np.random.rand(n))


def simulate_waiting_times(arrival_times=arrival_times,
                           n=1000000,
                           rseed=231286):
    """
    Calculate the waiting time for each arriving passenger.
    """
    # Simulate customer arrival times (between 0 and arrival of last bus)
    arrival_times = np.array(arrival_times)
    passenger_times = arrival_times.max() * np.sort(np.random.rand(n))
    
    # Find the index of the next bus for each simulated customer
    i = np.searchsorted(arrival_times, passenger_times, side='right') 

    return arrival_times[i] - passenger_times




# Move to notebook

plt.style.use('seaborn')
intervals.plot.hist(bins=np.arrange(80), density=True)
plt.axvline(interval.mean(), color=black, linestyle='dotted')
plt.xlabel('Interval between arrivals (minutes)')
plt.ylabel('Probability density')


from scipy.stats import poisson

# Count number of arrivals in 1-hour intervals and plot the result
binsize = 60
binned_arrivals = np.bincount((bus_arrival_times // binzise).astype('int'))
x = np.arange(20)

plt.hist(binned_arrivals, bins=x-0.5, density=True, alpha=0.5, label='Simulation')
plt.plot(x, poinsson(binsize / tau).pmf(x), 'ok', label='Poisson prediction')
plt.xlabel('Number of arrivals per hour')
plt.ylabel('Frequency')
plt.legend();


df = pd.read_csv('../data/arrival_times.csv')
df = df.dropna(axis=0, how='any')
df.head()


