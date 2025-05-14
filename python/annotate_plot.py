"""
annotate_plot
"""

__author__ = "ben_bazzett"

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def annotate_plot(annotation):
    for label, params in annotation.items():
        pos = params['position']
        align = params['alignment']
        size = params['fontsize']
        plt.gcf().text(pos[0], pos[1], label, horizontalalignment=align[0], verticalalignment=align[1], fontsize=size)

if __name__ == "__main__":
    def test_graph():
        x = np.linspace(-2, 2)
        y = x ** 2
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("annotated plot")
    today = datetime.today().date().isoformat()
    signature = f"Created by (Ben) (Bazzett) ({today})"
    annotations = {signature: {'position': [0.01, 0.01], 'alignment': ['left', 'bottom'], 'fontsize': 11}}
    test_graph()
    annotate_plot(annotations)
    plt.show()