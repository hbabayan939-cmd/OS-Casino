import random
from pathlib import Path
import tkinter as tk
import time

import customtkinter as ctk
from PIL import Image, ImageTk
from core.config import OS_NAMES, OS_STYLE
from core.game import SlotGame
from functions.formatting import describe_result

REEL_WIDTH = 520
CARD_WIDTH = 118
CARD_GAP = 10
CARD_STEP = CARD_WIDTH + CARD_GAP
SPIN_DURATION = 2.4
FRAME_INTERVAL = 16

class CasinoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OS Casino")
        self.geometry("600x640")
        self.resizable(False, False)

        self.game = SlotGame()
        self._reel_offset = 0
        self._displayed_offset = 0
        self._target_offset = 0
        self._spin_started = 0
        ctk.CTkLabel(
            self, text="OS CASINO", font=ctk.CTkFont(size=32, weight="bold")
        ).pack(pady=(20, 5))

        self.score_label = ctk.CTkLabel(
            self, text="Points: 0", font=ctk.CTkFont(size=22, weight="bold")
        )
        self.score_label.pack(pady=5)

        reel_frame = ctk.CTkFrame(self, corner_radius=18, fg_color="#191919")
        reel_frame.pack(padx=30, pady=24, fill="x")
        self.reel_canvas = tk.Canvas(
            reel_frame, width=REEL_WIDTH, height=178, bg="#191919",
            highlightthickness=0,
        )
        self.reel_canvas.pack(padx=10, pady=16)
        assets_dir = Path(__file__).parent / "assets"
        self.os_images = {}
        for name, style in OS_STYLE.items():
            with Image.open(assets_dir / style["icon"]) as source:
                image = source.copy()
            image.thumbnail((70, 70))
            self.os_images[name] = ImageTk.PhotoImage(image)
        self._draw_reel(["Linux", "Windows", "FreeBSD", "macOS", "OpenBSD", "NetBSD"] * 2)
        marker_x = REEL_WIDTH // 2
        self.reel_canvas.create_polygon(
            marker_x - 9, 4, marker_x + 9, 4, marker_x, 18,
            fill="#f4c542", outline="", tags="marker",
        )
        self.reel_canvas.create_line(
            marker_x, 18, marker_x, 174, fill="#f4c542", width=3, tags="marker",
        )

        self.result_label = ctk.CTkLabel(
            self, text="Click SPIN!", font=ctk.CTkFont(size=16)
        )
        self.result_label.pack(pady=5)

        self.spin_button = ctk.CTkButton(
            self,
            text="SPIN",
            width=220,
            height=55,
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.start_spin,
        )
        self.spin_button.pack(pady=15)

        rules = (
            "Linux: +500  |  FreeBSD: +400  |  NetBSD / OpenBSD: +250\n"
            "macOS: -300  |  Windows: -500"
        )
        ctk.CTkLabel(
            self, text=rules, font=ctk.CTkFont(size=13), text_color="gray"
        ).pack(pady=10)

    def start_spin(self):
        self.spin_button.configure(state="disabled")
        self.result_label.configure(text="Rolling...", text_color="white")
        result, change = self.game.spin()
        sequence = [random.choice(OS_NAMES) for _ in range(36)] + [result]
        self._reel_offset = 0
        self._draw_reel(sequence)
        self._target_offset = (len(sequence) - 1) * CARD_STEP + CARD_WIDTH / 2 - REEL_WIDTH / 2
        self.reel_result = (result, change)
        self._spin_started = time.perf_counter()
        self._animate()

    def _animate(self):
        elapsed = time.perf_counter() - self._spin_started
        progress = min(elapsed / SPIN_DURATION, 1)
        if progress < 1:
            eased = 1 - (1 - progress) ** 3
            self._reel_offset = self._target_offset * eased
            self._move_reel()
            self.after(FRAME_INTERVAL, self._animate)
        else:
            self._reel_offset = self._target_offset
            self._move_reel()
            _, change = self.reel_result

            self.score_label.configure(text=f"Points: {self.game.score}")
            text, color = describe_result(change)
            self.result_label.configure(text=text, text_color=color)
            self.spin_button.configure(state="normal")

    def _draw_reel(self, names: list[str]):
        self.reel_canvas.delete("reel")
        self._displayed_offset = 0
        for index, name in enumerate(names):
            x = index * CARD_STEP
            style = OS_STYLE[name]
            self.reel_canvas.create_rectangle(
                x, 26, x + CARD_WIDTH, 164, fill="#ffffff", outline="#4a4f57",
                width=2, tags="reel",
            )
            photo = self.os_images[name]
            self.reel_canvas.create_image(x + CARD_WIDTH // 2, 83, image=photo, tags="reel")
            self.reel_canvas.create_text(
                x + CARD_WIDTH // 2, 139, text=style["label"], fill="#000000",
                font=("Arial", 10, "bold"), tags="reel",
            )
        self.reel_canvas.tag_raise("marker")
        self._move_reel()

    def _move_reel(self):
        delta = self._reel_offset - self._displayed_offset
        self.reel_canvas.move("reel", -delta, 0)
        self._displayed_offset = self._reel_offset

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = CasinoApp()
    app.mainloop()
