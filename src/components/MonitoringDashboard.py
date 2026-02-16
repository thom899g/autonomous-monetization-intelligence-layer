import plotly.express as px

class MonitoringDashboard:
    """Provides real-time monitoring and visualization of metrics."""
    
    def __init__(self):
        self.data = {}
        
    def update_data(self, metric_name: str, value: float) -> None:
        """Update the dashboard with new data."""
        self.data[metric_name] = value
        
    def generate_visualization(self, metric_name: str) -> px.Figure:
        """
        Generate a visualization for a specific metric.
        
        Args:
            metric_name: Name of the metric to visualize.
            
        Returns:
            Figure: Plotly figure object.
        """
        fig = px.line(x=[1, 2, 3