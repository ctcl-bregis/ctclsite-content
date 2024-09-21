# ctclsite-rust - CTCL 2020-2024
# Single-use script kept for reference

import os, json
        
themes = {
    "99gray": {"color": "#999999", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "99green": {"color": "#009900", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "99red": {"color": "#990000", "fgcolor": "#ffffff", "css": "base", "defaultfont": "play"},
    "bcctc": {"color": "#d900ff", "fgcolor": "#ffffff", "css": "bcctc", "defaultfont": "bebasneue"},
    "blue": {"color": "#0000ff", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "ddr": {"color": "#000099", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "ddr2": {"color": "#999900", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "ddr3": {"color": "#990000", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "ddr4": {"color": "#009999", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "ddr5": {"color": "#990099", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "discord": {"color": "#707bf4", "fgcolor": "#ffffff", "css": "base", "defaultfont": "play"},
    "flipper": {"color": "#ff8200", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "gold": {"color": "#f0d000", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "green": {"color": "#00ff00", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "insta": {"color": "#f400a7", "fgcolor": "#ffffff", "css": "base", "defaultfont": "play"},
    "mediacow": {"color": "#996633", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "nanblue": {"color": "#00b7d5", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "netkart": {"color": "#006633", "fgcolor": "#ffffff", "css": "base", "defaultfont": "play"},
    "orange": {"color": "#ff6600", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "qipurple": {"color": "#520c82", "fgcolor": "#ffffff", "css": "base", "defaultfont": "play"},
    "red": {"color": "#ff0000", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "sdram": {"color": "#996600", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "source": {"color": "#ff9900", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "smyellow": {"color": "#e29e1c", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "white": {"color": "#ffffff", "fgcolor": "#000000", "css": "base", "defaultfont": "play"},
    "mct2": {"color": "#ffffff", "fgcolor": "#000000", "css": "mct2", "defaultfont": "heuristica"}
}

for name, data in themes.items():
    try:
        os.mkdir(name)
    except:
        pass

    with open(f"{name}/theme.json", "w") as f:
        f.write(json.dumps(data, indent=4))