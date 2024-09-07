import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 300

# Read the combined CSV file
combined_df = pd.read_csv("ha_spectral_data.csv")

# Convert date to ordinal
combined_df["Date"] = pd.to_datetime(combined_df["Date"]).map(datetime.toordinal)

x_data = []
y_data = []
z_data = []

grouped = combined_df.groupby("Filename")

for name, group in grouped:
    x_data.append(group["Wavelength"].values)
    y_data.append(np.full_like(group["Wavelength"].values, group["Date"].values[0]))
    z_data.append(group["Flux"].values)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot each spectrum
for i in range(len(x_data)):
    ax.plot(x_data[i], y_data[i], z_data[i], label=f"Spectrum {i+1}")

# Plot the data
ax.set_xlabel("Wavelength (Å)")
ax.set_ylabel("Date")
ax.set_zlabel("Flux")
ax.set_title("Ha Evolution NovaPer2020 - EBE - Lhires III")

ax.legend(loc="upper left", bbox_to_anchor=(1.25, 1))

plt.savefig("Waterfall.png", bbox_inches="tight")
plt.show()
