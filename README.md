# nhc-project

RISK ANALYTICS PIPELINE 

## Overview
This project provides a simple, modular risk analytics pipeline for a portfolio of positions. Given a CSV file containing positions and their associated attributes, the pipeline computes several key risk metrics, including:
- Gross Exposure by Asset Class
- Total Portfolio Factor-Based Exposure
- Portfolio Value-at-Risk (VaR)
The resulting metrics are output to a CSV file for easy consumption by risk managers or other stakeholders.

## Features
Positions File Reading:
A dedicated function (read_pos_file) to parse the positions CSV, perform validation, and ensure that all required columns are present. This ensures data consistency and reduces the risk of errors when running computations.

## Modular Risk Calculations:
The RiskCalculator class encapsulates all risk-related calculations, making the code more maintainable and extensible. Current calculations include:
- Aggregate gross exposure by asset class.
- Total Portfolio factor-based exposure.
- Parametric VaR calculation (placeholder or more sophisticated if additional data is provided such as cov. matric or historical pricing data).

## Logging and Error Handling:
The code uses Python’s built-in logging module with a debug-level configuration. This provides visibility into the pipeline’s internal states, making it easier to troubleshoot issues.

## Configurable VaR Confidence Intervals:
The VaR calculation allows specifying a confidence interval as a decimal (e.g., 0.95 for 95%), giving users flexibility in determining their preferred risk thresholds.

## Output Reporting:
After computations, a summary CSV (risk_summary_ouput.csv) is produced, containing the computed metrics. This can easily be integrated into downstream reporting systems or dashboards.

## Project Structure
1. Reads the positions file.
2. Instantiates RiskCalculator and computes the metrics.
3. Generates the output CSV file containing the summary of risk metrics.
requirements.txt: Lists the Python dependencies needed [pandas, logging].

## Potential Modifications to Risk Metrics
- Generating a better VaR measure using primary data so we can amend other potential parameters such as - half life, lookback period, var type (historical, parametric, Monte-Carlo)
    - Contribution / Incremental VaR for underlying components of portfolio
- Generating factor specifics (type of factor)
- Performance Metrics (Sharpe, Calmar, Sortino, Drawdown measures, Kelly Criterion etc.)
    - Check (quantstats lib.)
- Expected Shortfall
- Stress Loss (Shocks applied to net exposure & gross-net)
- VaR % AUM / % Risk Capital
NOTE: This report also is dependent on the desired output by the investment team and top mangement.
- Correlations (within portfolio & vs other indices)
- Tracking error
- Beta
- Liquidity risk measures
- Hit ratios / Best & Worst 1m / Rolling Avg. etc. 