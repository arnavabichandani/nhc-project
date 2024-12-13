"""
Main Function to run Risk Pipeline
Formatting: Black
"""

import logging
import pandas as pd
from positions_reader import read_pos_file
from risk_calc import RiskCalculator

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main(source_pos_filepath: str):
    """
    Description:
        Main Function to run Risk Pipeline
        Steps - 
            1. Read positions file
            2. Generate risk metrics (gross exposure, factor exposure, var)
            3. Generate CSV containing risk metrics
    """
    # 1. Read positions
    logging.info("Reading CSV position file...")
    positions_df = read_pos_file(filepath=source_pos_filepath)

    # 2. Compute risk metrics
    logging.info("Generating Risk Metrics...")
    try:
        calc = RiskCalculator(positions_df)
        exposure_by_class = calc.aggregate_gross_exposure_by_asset_class()
        total_factor_exposure = calc.compute_total_factor_exposure()
        portfolio_var = calc.compute_portfolio_var(confid_int=0.95)
    except Exception as e:
        logging.critical(f" ======== RISK METRICS COMPUTATION FAILED: {e} ========")

    # 3. Produce output CSV
    logging.info("Producing output CSV: risk_summary.csv...")
    output_rows = []
    for asset_class, exposure in exposure_by_class.items():
        output_rows.append(
            {"Metric": f"{asset_class} Gross Exposure", "Value": exposure}
        )
    output_rows.append(
        {"Metric": "Total Factor Exposure", "Value": total_factor_exposure}
    )
    output_rows.append({"Metric": "Portfolio VaR", "Value": portfolio_var})
    summary_df = pd.DataFrame(output_rows)
    summary_df.to_csv("risk_summary_output.csv", index=False)
    logging.info("Risk summary Data saved to risk_summary.csv")


if __name__ == "__main__":

    # Test
    filepath = (
        "/Users/arnavabichandani/Desktop/Github_AA/nhc-project/positions_sample.csv"
    )
    main(source_pos_filepath=filepath)
