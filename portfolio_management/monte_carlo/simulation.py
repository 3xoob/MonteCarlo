import numpy as np

class MonteCarloSimulation:
    def __init__(self, returns, initial_investment=1, weights=None):
        self.returns = returns
        self.mean = returns.mean()
        self.covariance = returns.cov()
        self.initial_investment = initial_investment
        num_assets = len(self.mean)
        
        # Initialize weights
        if weights is None:
            self.weights = np.ones(num_assets) / num_assets
        else:
            self.weights = np.array(weights)
        
        # Ensure weights have the correct shape (1D array)
        if self.weights.shape != (num_assets,):
            raise ValueError(f"Shape mismatch: Expected weights of shape ({num_assets},), got {self.weights.shape}")

    def run_simulation(self, num_simulations, time_horizon):
        all_cumulative_returns = np.zeros((time_horizon, num_simulations))
        final_portfolio_values = np.zeros(num_simulations)
        
        for sim in range(num_simulations):
            # Generate multivariate normal random returns for each day in the time horizon
            simulated_returns = np.random.multivariate_normal(self.mean, self.covariance, time_horizon)
            
            # Calculate cumulative returns for each asset
            cumulative_returns = np.cumprod(1 + simulated_returns, axis=0)
            
            # Ensure self.weights is properly reshaped as (num_assets,)
            if self.weights.ndim == 2:
                self.weights = self.weights.flatten()
                
            # Calculate portfolio cumulative returns
            try:
                portfolio_cumulative_returns = np.dot(cumulative_returns, self.weights)
            except ValueError as e:
                print(f"Error during dot product. Shapes of cumulative_returns: {cumulative_returns.shape}, weights: {self.weights.shape}")
                raise e
            
            # Store results for this simulation
            all_cumulative_returns[:, sim] = portfolio_cumulative_returns * self.initial_investment
            final_portfolio_values[sim] = portfolio_cumulative_returns[-1] * self.initial_investment
        
        return all_cumulative_returns, final_portfolio_values
