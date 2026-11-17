OS_STYLE = {
    "Windows": {"label": "WINDOWS", "color": "#FAFAFA", "text": "#000000", "icon": "windows_logo.png"},
    "Linux":   {"label": "LINUX",   "color": "#FAFAFA", "text": "#000000", "icon": "linux_logo.png"},
    "macOS":   {"label": "macOS",   "color": "#FAFAFA", "text": "#000000", "icon": "macos_logo.png"},
    "FreeBSD": {"label": "FreeBSD", "color": "#FAFAFA", "text": "#000000", "icon": "freebsd_logo.png"},
    "NetBSD":  {"label": "NetBSD",  "color": "#FAFAFA", "text": "#000000", "icon": "netbsd_logo.png"},
    "OpenBSD": {"label": "OpenBSD", "color": "#FAFAFA", "text": "#000000", "icon": "openbsd_logo.png"},
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
