import pytest
from unittest.mock import patch
import pandas as pd
from src.data.data import get_spy_data

@patch("src.data.data.yf.download")
def test_get_spy_data_extracts_close_prices(mock_download):
    mock_df = pd.DataFrame({"Close": [200.0, 201.0, 202.0]})
    mock_download.return_value = mock_df
    
    result = get_spy_data("SPY", "2015-01-01", "2015-01-05")
    
    assert result == [200.0, 201.0, 202.0]