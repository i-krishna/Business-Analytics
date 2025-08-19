"""Personal activity grid with RAW VALUES and UNITS (no targets shown).

Rows = biweekly periods (time). Columns = activity categories.
Each cell contains the actual value + unit for that period; color shows
how high it is relative to the maximum for THAT column (darker = higher).
"""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# ------------------ Raw data (sample) ------------------
periods = ["Jun 1–15", "Jun 16–30", "Jul 1–15", "Jul 16–31"]

# YouTube watching hours per period (sample data)
youtube_hours = [12, 15, 14, 16]                      # hours

# Tool practice hours per period
tool_hours_total = [28, 30, 31, 32]                   # hours practiced

# Cooking unique recipes per period
unique_recipes = [5, 6, 6, 7]                         # recipes

# Swimming average km per session each period
swim_km_total = [7.5, 8.2, 8.8, 9.4]; sessions_per_period = 8
km_per_session = [d / sessions_per_period for d in swim_km_total]  # km per swim session

# Gym + Outdoor sports combined
strength_minutes = [270, 315, 320, 360]; gym_sessions = [6, 7, 7, 8]
outdoor_minutes = [80, 90, 100, 110]; outdoor_sessions = [2, 3, 3, 4]
total_active_minutes = [g + o for g, o in zip(strength_minutes, outdoor_minutes)]
total_sessions = [g + o for g, o in zip(gym_sessions, outdoor_sessions)]
combined_minutes_per_session = [m / s for m, s in zip(total_active_minutes, total_sessions)]  # min per active session

metrics = [
    ("YouTube\n(hours)", youtube_hours, plt.cm.Blues, "h"),
    ("Tool Practice\n(hours)", tool_hours_total, plt.cm.Greens, "h"),
    ("Cooking\n(recipes)", unique_recipes, plt.cm.Oranges, "rec"),
    ("Swimming\n(km/session)", km_per_session, plt.cm.Purples, "km"),
    ("Gym+Outdoor\n(min/session)", combined_minutes_per_session, plt.cm.Reds, "min"),
]

# ------------------ Build grid ------------------
rows = len(periods); cols = len(metrics)
plt.style.use("seaborn-v0_8-white")
fig, ax = plt.subplots(figsize=(10, 4.8))
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.invert_yaxis()
ax.set_xticks(np.arange(cols) + 0.5)
ax.set_xticklabels([m[0] for m in metrics], rotation=12, ha='right')
ax.set_yticks(np.arange(rows) + 0.5)
ax.set_yticklabels(periods)
ax.tick_params(length=0)
ax.set_title("Personal Activity Grid (Raw Values + Units)", fontsize=14, weight='bold')

for c, (label, values, cmap, unit) in enumerate(metrics):
    vmax = max(values) or 1
    norm = colors.Normalize(vmin=0, vmax=vmax)
    threshold = 0.65 * vmax
    for r, val in enumerate(values):
        color = cmap(norm(val))
        ax.add_patch(plt.Rectangle((c, r), 1, 1, facecolor=color, edgecolor='#eeeeee'))
        txt_color = '#000' if val < threshold else '#fff'
        display = f"{val:.2f}" if isinstance(val, float) and not float(val).is_integer() else f"{val:.0f}"
        ax.text(c + 0.5, r + 0.5, f"{display} {unit}", ha='center', va='center', fontsize=9, color=txt_color)

fig.text(0.01, 0.02, "Color scale per column (darker = higher for that metric).", fontsize=8, color='#444')
fig.tight_layout(rect=(0,0.05,1,0.98))
fig.savefig("personal_metrics_heatmap.png", dpi=150)
print("Raw-value heatmap saved to personal_metrics_heatmap.png")
