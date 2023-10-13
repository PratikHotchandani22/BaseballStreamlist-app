# Required libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Sample data creation (replace this with your actual data)
np.random.seed(42)
data = {
    'batter': np.random.choice(['Batter1', 'Batter2', 'Batter3'], 1000),
    'pitcher': np.random.choice(['Pitcher1', 'Pitcher2', 'Pitcher3'], 1000),
    'exit_velocity': np.random.normal(90, 5, 1000),
    'launch_angle': np.random.normal(15, 5, 1000)
}
df = pd.DataFrame(data)

def draw_baseball_pitch(ax):
    """Draws a baseball diamond on the given axes."""
    # Drawing the diamond shape
    diamond = patches.RegularPolygon((0, 0), numVertices=4, radius=1, orientation=np.pi/4, fill=False)
    ax.add_patch(diamond)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

def main():
    st.title("Joint Probability Density for Exit Velocity & Launch Angle on Baseball Pitch")

    batter_selected = st.selectbox("Choose a batter:", df['batter'].unique())
    pitcher_selected = st.selectbox("Choose a pitcher:", df['pitcher'].unique())
    filtered_data = df[(df['batter'] == batter_selected) & (df['pitcher'] == pitcher_selected)]

    if not filtered_data.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Draw baseball pitch shape
        draw_baseball_pitch(ax)

        # Overlay the KDE plot (Adjust levels and cmap as needed)
        sns.kdeplot(data=filtered_data, x="exit_velocity", y="launch_angle", ax=ax, fill=True, cmap='Blues', cbar=True, levels=5, alpha=0.5)
        
        # Label the angles (You can add more angles if needed)
        angles = [-45, -30, -15, 0, 15, 30, 45]
        for angle in angles:
            x = 1.2 * np.cos(np.radians(angle))
            y = 1.2 * np.sin(np.radians(angle))
            ax.text(x, y, f"{angle}°", ha='center', va='center', fontsize=8)

        ax.set_title(f'Exit Velocity vs. Launch Angle for {batter_selected} against {pitcher_selected}')
        st.pyplot(fig)
    else:
        st.write(f"No data available for {batter_selected} against {pitcher_selected}")

if __name__ == "__main__":
    main()
