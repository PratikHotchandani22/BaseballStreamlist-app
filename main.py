# Required libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data creation (replace this with your actual data)
# For simplicity, I'm generating some random data
np.random.seed(42)
data = {
    'batter': np.random.choice(['Batter1', 'Batter2', 'Batter3'], 1000),
    'pitcher': np.random.choice(['Pitcher1', 'Pitcher2', 'Pitcher3'], 1000),
    'exit_velocity': np.random.normal(90, 5, 1000),
    'launch_angle': np.random.normal(15, 5, 1000)
}
df = pd.DataFrame(data)

# Streamlit App
def main():
    st.title("Joint Probability Density for Exit Velocity & Launch Angle")

    # Dropdown for batters
    batter_selected = st.selectbox("Choose a batter:", df['batter'].unique())
    
    # Dropdown for pitchers
    pitcher_selected = st.selectbox("Choose a pitcher:", df['pitcher'].unique())
    
    # Filter data based on batter and pitcher selection
    filtered_data = df[(df['batter'] == batter_selected) & (df['pitcher'] == pitcher_selected)]

    # Plot
    if not filtered_data.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.kdeplot(data=filtered_data, x="exit_velocity", y="launch_angle", ax=ax, fill=True, cmap='Blues', cbar=True)
        ax.set_title(f'Exit Velocity vs. Launch Angle for {batter_selected} against {pitcher_selected}')
        st.pyplot(fig)
    else:
        st.write(f"No data available for {batter_selected} against {pitcher_selected}")

if __name__ == "__main__":
    main()
