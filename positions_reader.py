'''
NHC Position Reader
Formatting: Black
'''

import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_pos_file(filepath: str) -> pd.DataFrame:
    """
        Description:
            Function to read & parse csv file of positions
        Returns:
            pd.DataFrame
        """
    pos_fl = pd.read_csv(filepath, header=None)
    if pos_fl is None:
        logging.error("Positions file empty **")
    logging.info("Parsing raw positions file....")
    clean_pos = pos_fl[0].str.split(",", expand=True)
    clean_pos.columns = clean_pos.iloc[0]
    clean_pos = clean_pos.drop(clean_pos.index[0]).reset_index(drop=True)
    logging.debug("Handling col types...")
    clean_pos["notional"] = pd.to_numeric(clean_pos["notional"], errors="coerce")
    clean_pos["risk_factor_weight"] = pd.to_numeric(
        clean_pos["risk_factor_weight"], errors="coerce"
    )
    logging.info("Checking correct cols...")
    input_req_cols = {
        "portfolio_id",
        "asset_class",
        "security_id",
        "notional",
        "risk_factor_weight",
    }
    if not input_req_cols.issubset(clean_pos.columns):
        missing = input_req_cols - set(clean_pos.columns)
        raise ValueError(f"Missing required cols in pos. file: {missing}")
    return clean_pos


if __name__ == "__main__":

    # Test
    df_test = read_pos_file(
        filepath="/Users/arnavabichandani/Downloads/positions_sample.csv"
    )
