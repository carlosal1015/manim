from slides import *

class GitConfig(SlideScene):
    CONFIG = {
        "script_name": "git_definitions",
        "index_paragraphs": [25,27,28],
        "test_code": False,
        "alignment": "\\flushleft",
        "justify_length": 200,
        "functions": [
          lambda mob: mob[1].align_to(mob[0],LEFT*2).set_color(YELLOW),
          lambda mob: mob[2].align_to(mob[1],LEFT).set_color(YELLOW),
          ],
        "pause_at_start": 0.1,
        "animation_in": "Keyboard",
        "middle_pauses": [1],
        "pause_before_remove": 1.5,
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 1.5
        },
    }

class GitClone(SlideScene):
    CONFIG = {
        "script_name": "git_definitions",
        "index_paragraphs": [13,14,15],
        "test_code": False,
        "alignment": "\\flushleft",
        "justify_length": 250,
        "functions": [
        #   lambda mob: mob[0].scale(1.4).set_color(BLUE),
          lambda mob: mob[1].align_to(mob[0],LEFT*2).set_color(YELLOW),
          lambda mob: mob[2].align_to(mob[1],LEFT).set_color(YELLOW),
          ],
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Keyboard",
        # "run_times": [2,3,2], Not run_times in this animation
        # Before OUT
        "middle_pauses": [1], # 2s pause between paragraph 1 and 2, 2s pause between paragraph 2 and 1
        "pause_before_remove": 1.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 1.5
        },
    }
# https://github.com/3b1b/manim/pull/1035