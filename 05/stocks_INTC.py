import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

def load_history_data(fname: str) -> np.ndarray:
    from_strdate = lambda x: np.datetime64(datetime.strptime(x.strip('"'), '%Y-%m-%d'))
    from_strnum = lambda x: float(x.strip('"'))
    from_strnumm = lambda x: float(x.strip('"').strip('M')) * 1_000_000

    names = ("Date", "Open", "High", "Low", "Close", "Adj Close", "Volume")
    converters = {
        "Date": from_strdate,
        "Open": from_strnum,
        "High": from_strnum,
        "Low": from_strnum,
        "Close": from_strnum,
        "Adj Close": from_strnum,
        "Volume": from_strnumm
    }

    data = np.genfromtxt(fname, delimiter=",", encoding="utf-8", skip_header=1, names=names,
                         dtype=[("Date", 'datetime64[D]'),
                                ("Open", np.float64),
                                ("High", np.float64),
                                ("Low", np.float64),
                                ("Close", np.float64),
                                ("Adj Close", np.float64),
                                ("Volume", np.float64)],
                         converters=converters)
    return data

def plot_history_data(data: np.ndarray, n=100) -> None:
    plt.style.use('dark_background')
    # Plot the high and low values per last n days (array is reversed in time)
    fig, ax = plt.subplots()
    date, highs, lows = data['Date'][:n], data['High'][:n], data['Low'][:n]
    
    ax.plot(date, highs, c='red', alpha=0.5)
    ax.plot(date, lows, c='blue', alpha=0.5)
    plt.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title(f"Stock high and low prices per {n} days", fontsize=18)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Price (USD)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.grid()
    plt.show()

def main() -> None:
    fname = '/home/max/ppi-labs/05/data/INTC.csv'
    data = load_history_data(fname)
    plot_history_data(data)

if __name__ == "__main__":
    main()
