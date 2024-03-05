import numpy as np
import matplotlib.pyplot as plt

# Constants
Cp_specific = 1.146  # Specific heat capacity at constant pressure in kJ/kg-K
R = 0.287  # Gas constant in kJ/kg-K

# Given data
Tt1 = 1400  # Inlet temperature to turbine in Kelvin
Pt1 = 6.5    # Inlet pressure to turbine in bar
Tt2 = 1000   # Outlet temperature from turbine in Kelvin
Pt2 = 1      # Outlet pressure from turbine in bar

# Calculations
# Total Temperature Ratio
Tt_ratio = Tt2 / Tt1
print("Total Temperature Ratio:", Tt_ratio)

# Total Pressure Ratio
Pt_ratio = Pt2 / Pt1
print("Total Pressure Ratio:", Pt_ratio)

# Total Turbine Efficiency
efficiency = 1 - (Tt2 / Tt1) / (Pt2 / Pt1) ** ((Cp_specific * (Tt1 - Tt2)) / (Tt1 * 1000))
print("Total Turbine Efficiency:", efficiency)

# Total Turbine Work Output
Turbine_work = Cp_specific * (Tt1 - Tt2)
print("Total Turbine Work Output:", Turbine_work, "kJ/kg")

# Turbine Outlet Temperature
Tt_outlet = Tt1 - (Tt1 - Tt2) * (Pt2 / Pt1) ** ((Cp_specific * (Tt1 - Tt2)) / (Tt1 * 1000))
print("Turbine Outlet Temperature:", Tt_outlet, "K")

# Turbine Outlet Pressure
Pt_outlet = Pt1 * (Tt_outlet / Tt1)
print("Turbine Outlet Pressure:", Pt_outlet, "bar")

# Turbine Outlet Pressure
Pt2_atm = Pt2 * 1.01325  # Convert outlet pressure from bar to atm
if Pt2_atm >= 1:
    print("Outlet pressure meets or exceeds atmospheric pressure.")
else:
    print("Outlet pressure does not meet atmospheric pressure requirements.")

# Stage-wise data
stages = {
    1: {'Tt1': 1212.5, 'Tt3': 1109, 'Pt1': 1497.70, 'Pt3': 975, 'M1': 0.5, 'M2': 0.5},
    2: {'Tt1': 1109, 'Tt3': 1053, 'Pt1': 974.71, 'Pt3': 757.9, 'M1': 0.5, 'M2': 0.5},
    3: {'Tt1': 1052.6, 'Tt3': 1000, 'Pt1': 757.89, 'Pt3': 591.8, 'M1': 0.5, 'M2': 0.5},
    4: {'Tt1': 999.8, 'Tt3': 949, 'Pt1': 591.80, 'Pt3': 460.3, 'M1': 0.5, 'M2': 0.5},
    5: {'Tt1': 949.0, 'Tt3': 903.8, 'Pt1': 460.32, 'Pt3': 363.9, 'M1': 0.5, 'M2': 0.5},
    6: {'Tt1': 903.8, 'Tt3': 862.4, 'Pt1': 363.93, 'Pt3': 290.3, 'M1': 0.5, 'M2': 0.5},
    7: {'Tt1': 862.4, 'Tt3': 824.7, 'Pt1': 290.32, 'Pt3': 234.1, 'M1': 0.5, 'M2': 0.5},
    8: {'Tt1': 824.7, 'Tt3': 790.3, 'Pt1': 234.10, 'Pt3': 190.9, 'M1': 0.5, 'M2': 0.5},
    9: {'Tt1': 790.3, 'Tt3': 758.8, 'Pt1': 190.88, 'Pt3': 157.6, 'M1': 0.5, 'M2': 0.5},
    10: {'Tt1': 758.8, 'Tt3': 729.9, 'Pt1': 157.64, 'Pt3': 131.0, 'M1': 0.5, 'M2': 0.5}
}

# Turbine Parameters
T_inlet = 298  # Combustor output in Kelvin
P_inlet = 101.3  # Combustor output in kPa

# Initialize lists to store calculated values
turbine_efficiencies = []
turbine_work_outputs = []
mass_flow_rates = []

# Loop through each stage to calculate turbine efficiency, work output, and mass flow rate
for stage, data in stages.items():
    Tt1 = data['Tt1']
    Tt3 = data['Tt3']
    Pt1 = data['Pt1']
    Pt3 = data['Pt3']
    M1 = data['M1']
    M2 = data['M2']

    # Turbine Efficiency
    h_ideal = Cp_specific * (Tt1 - Tt3)
    h_actual = R * T_inlet * np.log(Pt1 / Pt3)
    eta_turbine = h_actual / h_ideal
    turbine_efficiencies.append(eta_turbine)

    # Turbine Work Output
    work_output = h_ideal
    turbine_work_outputs.append(work_output)

    # Mass Flow Rate
    mass_flow_rate = M1 * (Pt1) / (R * Tt1) * (np.sqrt(Cp_specific * R * Tt1))
    mass_flow_rates.append(mass_flow_rate)

    # Print work at each step
    print(f"Stage {stage}: Work Output = {work_output:.2f} kJ/kg")

# Calculate Total Mass Flow Rate
total_mass_flow_rate = sum(mass_flow_rates)
print("Total Mass Flow Rate:", total_mass_flow_rate, "kg/s")

# Print Mass Flow Rates for each stage
print("Mass Flow Rates for Each Stage:")
for stage, mass_flow_rate in enumerate(mass_flow_rates, 1):
    print(f"Stage {stage}: {mass_flow_rate:.2f} kg/s")

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Pressure Ratio vs stage
axs[0, 0].plot(range(1, len(stages) + 1), [stages[stage]['Pt3'] / stages[stage]['Pt1'] for stage in stages], marker='o', color='blue', linestyle='-')
axs[0, 0].set_xlabel('Stage', fontsize=15)  # Adjust fontsize here
axs[0, 0].set_ylabel('Pressure Ratio', fontsize=15)  # Adjust fontsize here
axs[0, 0].set_title('Pressure Ratio vs Stage', fontsize=20)
axs[0, 0].grid(True)
axs[0, 0].tick_params(axis='both', which='major', labelsize=15)  # Adjust fontsize here
plt.xticks(np.arange(1, len(stages) + 1, step=1), fontsize=15)  # Adjust fontsize here
plt.yticks(np.arange(0, 2, step=0.1), fontsize=15)  # Adjust fontsize here

# Temperature Ratio vs stage
axs[0, 1].plot(range(1, len(stages) + 1), [stages[stage]['Tt3'] / stages[stage]['Tt1'] for stage in stages], marker='o', color='green', linestyle='-')
axs[0, 1].set_xlabel('Stage', fontsize=15)  # Adjust fontsize here
axs[0, 1].set_ylabel('Temperature Ratio', fontsize=15)  # Adjust fontsize here
axs[0, 1].set_title('Temperature Ratio vs Stage', fontsize=20)
axs[0, 1].grid(True)
axs[0, 1].tick_params(axis='both', which='major', labelsize=15)  # Adjust fontsize here
plt.xticks(np.arange(1, len(stages) + 1, step=1), fontsize=15)  # Adjust fontsize here
plt.yticks(np.arange(0, 1, step=0.1), fontsize=15)  # Adjust fontsize here

# Turbine Efficiency vs stages
axs[1, 0].plot(range(1, len(stages) + 1), turbine_efficiencies, marker='o', color='red', linestyle='-')
axs[1, 0].set_xlabel('Stage', fontsize=15)  # Adjust fontsize here
axs[1, 0].set_ylabel('Turbine Efficiency', fontsize=15)  # Adjust fontsize here
axs[1, 0].set_title('Turbine Efficiency vs Stage', fontsize=20)
axs[1, 0].grid(True)
axs[1, 0].tick_params(axis='both', which='major', labelsize=15)  # Adjust fontsize here
plt.xticks(np.arange(1, len(stages) + 1, step=1), fontsize=15)  # Adjust fontsize here
plt.yticks(np.arange(0, 1.2, step=0.1), fontsize=15)  # Adjust fontsize here

# Work Output vs stages
axs[1, 1].plot(range(1, len(stages) + 1), turbine_work_outputs, marker='o', color='orange', linestyle='-')
axs[1, 1].set_xlabel('Stage', fontsize=15)  # Adjust fontsize here
axs[1, 1].set_ylabel('Work Output (kJ/kg)', fontsize=15)  # Adjust fontsize here
axs[1, 1].set_title('Work Output vs Stage', fontsize=20)
axs[1, 1].grid(True)
axs[1, 1].tick_params(axis='both', which='major', labelsize=15)  # Adjust fontsize here
plt.xticks(np.arange(1, len(stages) + 1, step=1), fontsize=15)  # Adjust fontsize here
plt.yticks(np.arange(0, 130, step=15), fontsize=15)  # Adjust fontsize here


# Additional plot for Mass Flow Rate vs stages
ax2 = axs[1, 1].twinx()
ax2.plot(range(1, len(stages) + 1), mass_flow_rates, marker='o', color='purple', linestyle='-', label='Mass Flow Rate (kg/s)')
ax2.set_ylabel('Mass Flow Rate (kg/s)')
ax2.tick_params(axis='y', labelcolor='purple')
ax2.yaxis.label.set_color('purple')
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()
