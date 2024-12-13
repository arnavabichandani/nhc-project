"""
NHC Risk Calcs file
Formatting: Black
"""

import logging
import pandas as pd



# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class RiskCalculator:
    """
    Description:
        Class to perform calcs. for multiple risk metrics
    """

    def __init__(self, positions: pd.DataFrame):
        if positions is None or positions.empty:
            logging.error("pos df is empty -> Risk Computation Failed!")
            raise ValueError("Positions df empty!")
        self.positions = positions.copy()

    def aggregate_gross_exposure_by_asset_class(self) -> pd.Series:
        """
        Description:
            Method to agg. gross exposure by asset class
        Returns:
            pd.Series
        """
        logging.info("Aggregating gross exposure by asset class...")
        if (
            "asset_class" not in self.positions.columns
            or "notional" not in self.positions.columns
        ):
            logging.error("Required cols 'asset_class' OR 'notional' not found in df.")
            raise ValueError("Missing required cols for exposure calc...")
        exposure = self.positions.groupby("asset_class")["notional"].sum()
        logging.debug(f"Aggregated exposures by asset class: {exposure.to_dict()}")
        return exposure

    def compute_total_factor_exposure(self) -> float:
        """
        Description:
            Method to get total factor exposure for portfolio
        Returns:
            float
        """
        logging.info("Computing total factor-based exposure at portfolio level...")
        if (
            "notional" not in self.positions.columns
            or "risk_factor_weight" not in self.positions.columns
        ):
            logging.error(
                "Required cols 'notional' OR 'risk_factor_weight' not found in df."
            )
            raise ValueError("Missing required cols for factor exposure calc...")
        self.positions["factor_exposure"] = (
            self.positions["notional"] * self.positions["risk_factor_weight"]
        )
        total_factor_exposure = self.positions["factor_exposure"].sum()
        logging.debug(f"Total factor exposure: {total_factor_exposure}")
        # NOTE: No assumptions on ccy in current version.
        return total_factor_exposure

    def compute_portfolio_var(self, confid_int: float = 0.99) -> float:
        """
        Description:
            Method to calculate Portfolio level VaR
            NOTE: 
                - default val. for confid_int = 0.99 (3sigma VaR)
                - Simple calc. included since we do not have covar. 
                    matrix or historical prices for given sec. 
        Returns:
            float   
        """
        logging.info(
            f"Computing Portfolio VaR at {confid_int*100}% confidence interval..."
        )
        if "notional" not in self.positions.columns:
            logging.error("'notional' column missing for VaR calculation.")
            raise ValueError("Missing 'notional' column for VaR calculation.")
        if confid_int <= 0 or confid_int >= 1:
            logging.error(
                "Confidence interval must be between 0 and 1 (e.g., 0.95 for 95%)."
            )
            raise ValueError("Invalid confidence interval. Must be between 0 and 1.")
        total_notional = self.positions["notional"].sum()
        var_estimate = round(total_notional * (1 - confid_int), 0)
        logging.debug(
            f"Total $ Notional: {total_notional}, Computed $VaR {confid_int}: {var_estimate}"
        )
        return var_estimate
