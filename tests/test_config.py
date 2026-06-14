import pytest
import os
import yaml
from src.config import load_config

def test_load_config_reads_yaml_correctly(tmp_path):
    config_dir = tmp_path / "src"
    config_dir.mkdir()
    config_file = tmp_path / "config.yaml"
    
    mock_data = {
        "simulation": {"initial_portfolio": 10000, "initial_shares": 0},
        "data": {"ticker": "SPY"}
    }
    
    with open(config_file, "w") as f:
        yaml.dump(mock_data, f)
        
    import src.config
    src.config.__file__ = os.path.join(str(config_dir), "config.py")
    
    result = load_config()
    assert result["simulation"]["initial_portfolio"] == 10000
    assert result["data"]["ticker"] == "SPY"