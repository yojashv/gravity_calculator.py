import matplotlib.pyplot as plt
import numpy as np

def gravitational_potential_calculator():
    # 1. Define Constants
    G = 6.67e-11  # Gravitational Constant

    print("--- Gravitational Potential Calculator (V = -GM/R) ---")
    print("Note: Enter large values for Mass (e.g., Earth is approx 5.97e24 kg)")
    
    # 2. Input Boxes (Calculator Section)
    try:
        # taking inputs as float, supports scientific notation (e.g., 6e24)
        M = float(input("Enter Mass of Object (M) in kg: ")) 
        R_target = float(input("Enter Distance/Radius (R) in meters: "))
        
        if R_target <= 0:
            print("Error: Distance must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    # 3. Calculation
    # Calculate V for the specific input
    V_target = - (G * M) / R_target

    print("\n--- Results ---")
    print(f"Calculated Potential (V): {V_target:.4e} J/kg")
    print("----------------")
    print("Generating Graph...")

    # 4. Graphing Logic
    
    # Create a range of R values for the curve
    # We start from a small fraction of the target R up to 5x the target R
    # We avoid 0 exactly to prevent division by zero error
    r_values = np.linspace(R_target * 0.1, R_target * 5, 1000)
    
    # Calculate V for all points in the range
    v_values = - (G * M) / r_values

    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot the main blue curve
    plt.plot(r_values, v_values, label=r'$V = -\frac{GM}{R}$', color='blue', linewidth=2)
    
    # Plot the specific calculator point (Red Dot)
    plt.scatter([R_target], [V_target], color='red', zorder=5, s=100, label=f'Your Point\nR={R_target:.2e}\nV={V_target:.2e}')
    
    # Draw a dashed line to show the relationship to axes
    plt.axvline(x=R_target, color='gray', linestyle='--', alpha=0.5)
    plt.axhline(y=V_target, color='gray', linestyle='--', alpha=0.5)

    # Draw the "Zero" line (Maximum Potential)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1.5, label='V=0 (Max at Infinity)')

    # Graph Formatting
    plt.title(f'Gravitational Potential vs Distance\n(Mass = {M:.2e} kg)', fontsize=14)
    plt.xlabel('Distance R (meters)', fontsize=12)
    plt.ylabel('Potential V (J/kg)', fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend()
    
    # Visualizing the concept: 
    # V is negative, so 0 is at the top (Maximum)
    # As R -> 0 (left), V -> -Infinity (down)
    
    plt.show()

# Run the program
if __name__ == "__main__":
    gravitational_potential_calculator()
