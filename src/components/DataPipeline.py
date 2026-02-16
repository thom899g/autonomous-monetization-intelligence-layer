from typing import Dict, Optional
import pandas as pd

class DataPipeline:
    """Manages data collection and preprocessing for optimization."""
    
    def __init__(self):
        self.sources = []
        
    def add_data_source(self, source):
        """Add a new data source to the pipeline."""
        self.sources.append(source)
        
    def process_data(self) -> pd.DataFrame:
        """
        Collect and process data from all sources.
        
        Returns:
            DataFrame: Processed dataset ready for analysis.
        """
        try:
            dfs = [source.fetch() for source in self.sources]
            concatenated = pd.concat(dfs, axis=0)
            processed = self._preprocess_data(concatenated)
            return processed
        except Exception as e:
            logging.error(f"Data processing failed: {str(e)}")
            raise
            
    def _preprocess_data(self, data):
        """Preprocess the raw dataset."""
        # Basic cleaning and transformation logic here
        return data.dropna()