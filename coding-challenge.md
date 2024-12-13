# Coding Challenge: Portfolio Risk Pipeline

## Background

The goal of this challenge is to build a simple risk analytics pipeline. The source of the pipeline is csv files, and the output is a CSV file containing a collection of statistics to be used by the Head of Risk to evaluate the risk of our portfolio.

## Deliverable

Submit a folder or git repository containing all source code and any related files needed to run your solution.

## Requirements

1. Python object to read a CSV file of positions.  

2. A Python object (or objects) to run the following calculations:  
   - Aggregate gross exposure by asset class (e.g., Equities, Fixed Income, FX, Commodities).  
   - Compute a simple factor-based risk metric. For example, assume each position has an associated "risk factor weight" column. You could produce a "Total Factor Exposure" by summing `Position Notional * Risk Factor Weight`.  
   - Implement a simple portfolio VaR calculation (this can be a stub or a rough approximation, e.g., 1% of total notional as a placeholder). The exact methodology is less important than how you structure the computation.

3. Produce an output CSV that summarizes:  
     - Total gross exposure per asset class.  
     - Total factor-based exposure for the entire portfolio.  
     - A simple VaR estimate for the entire portfolio.

4. Include any necessary environment definition files (e.g., requirements.txt, pyproject.toml) required to run this code.

## Sample Data

`positions_sample.csv`:
```
portfolio_id,asset_class,security_id,notional,risk_factor_weight
PM1,Equities,AMZN,1000000,1.2
PM1,Equities,AAPL,500000,1.0
PM1,Fixed Income,US10Y,2000000,0.8
PM1,FX,EURUSD,3000000,1.5
PM1,Commodities,WTI,1500000,1.1
PM2,Equities,GOOGL,800000,1.3
PM2,Equities,MSFT,1000000,1.1
PM2,FX,GBPUSD,1200000,1.4
PM2,Fixed Income,US30Y,2500000,0.9
PM2,Commodities,GOLD,2000000,1.2
PM3,Equities,TSLA,700000,1.1
PM3,Equities,JNJ,600000,1.0
PM3,Fixed Income,GER10Y,1800000,0.85
PM3,FX,USDJPY,1500000,1.3
PM3,Commodities,Brent,1000000,1.2
```

## Evaluation Criteria

- How comfortable would we feel maintaining, debugging, and running this code in production?
- For possible follow-up discussion: The solution must meet the requirements, but we're equally interested in how you architected the solution and why. What are the design choices that you rejected? If you had more time, how might you change the design? What risk stats would you add to, or remove from, the output CSV and why?

## Hints

- The use of any and all developer tools, including AI-based tools (like Claude.ai or ChatGPT), is welcomed.
- The use of additional user-defined objects to support the output is encouraged to support a modular and extensible design.
