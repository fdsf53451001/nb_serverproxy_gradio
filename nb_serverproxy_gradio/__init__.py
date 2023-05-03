__version__="0.0.5"

import os
from pathlib import Path

# Requires openrefine to be on the path as: refine
def setup_gradio():
    return {
        'command': ['ls'],
        'port': 7860,
        'environment': {},
        'timeout': 120,
        'launcher_entry': {
            'title': 'Gradio',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'gradio.svg')
        }
    }
