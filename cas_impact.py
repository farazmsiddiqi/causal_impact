import yfinance as yf
from causalimpact import CausalImpact

# init
start_date = '2018-01-02'
end_date = '2018-09-02'
pre_start = '2018-03-02'
pre_end = '2018-05-02'
post_start = '2018-05-08'
post_end = '2018-08-07'
stocks = ["ETH-USD", "JPM", "PYPL", "BAC", "MS", "GS"]
pre_period = [pre_start, pre_end]
post_period = [post_start, post_end]

# get data, clean data
dataset = yf.download(stocks,
                      start=start_date,
                      end=end_date,
                      interval= '1d')
dataset = dataset.iloc[:, :6]
dataset.columns = dataset.columns.droplevel()
dataset = dataset.dropna()

# Create a CausalImpact object
ci = CausalImpact(dataset[stocks], pre_period, post_period)

# Print the summary of results
print(ci.summary())

# Plot the results
ci.plot()
