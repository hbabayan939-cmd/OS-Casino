OS_STYLE = {
    "Windows": {"label": "WINDOWS", "color": "#0078D6", "text": "white"},
    "Linux":   {"label": "LINUX",   "color": "#FCC624", "text": "black"},
    "macOS":   {"label": "macOS",   "color": "#A2AAAD", "text": "black"},
    "FreeBSD": {"label": "FreeBSD", "color": "#AB2B28", "text": "white"},
    "NetBSD":  {"label": "NetBSD",  "color": "#FF6600", "text": "white"},
    "OpenBSD": {"label": "OpenBSD", "color": "#F2CA30", "text": "black"},
}

OS_NAMES = list(OS_STYLE.keys())

POINTS = {
    "Linux":   500,
    "FreeBSD": 400,
    "NetBSD":  250,
    "OpenBSD": 250,
    "macOS":   -300,
    "Windows": -500,
}
