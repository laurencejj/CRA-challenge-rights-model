"""Shared plot style."""
import matplotlib.pyplot as plt

INK, MUTE, GRID = '#1f2a37', '#6b7685', '#e3e7ec'
BLUE, ORANGE, RED, GREEN = '#2b6cb0', '#d9822b', '#c0392b', '#2f855a'
plt.rcParams.update({'font.size': 11, 'axes.edgecolor': MUTE, 'axes.labelcolor': INK,
                     'xtick.color': MUTE, 'ytick.color': MUTE, 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.grid': True, 'grid.color': GRID,
                     'figure.dpi': 150, 'savefig.bbox': 'tight'})
