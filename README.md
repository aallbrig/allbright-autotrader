# Allbright Autotrader
What if I can build an auto trader. Woah.

### Getting Started
```bash
python3 -m virtualenv venv
# Activate virtual environment
source venv/bin/activate
# Deactivate virtual environment
source venv/bin/deactivate

pip3 install -r requirements.txt
```

### DX (Developer Experience)

Documentation
- Backtrader (python library) for historic trade data: https://www.backtrader.com/docu/
- Yahoo Finance (website) for financial data (e.g. for things like https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch)
 
```bash
# Sync facts from fact fact_providers into offline cache
python3 main.py job-sync-facts -i ./data/STOCKS.txt
# Based on stock/facts, simulate trading strategies on historic data (aka backtading)
python3 main.py job-simulate-historic-trading -i ./data/STOCKS.txt
# Based on simulations, trading decisions should be executed
python3 main.py job-execute-trading-strategy -i ./data/STOCKS.txt

# Run all tests
python3 -m unittest
```

