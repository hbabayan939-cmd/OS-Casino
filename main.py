import random
from pathlib import Path

import customtkinter as ctk
from PIL import Image
from core.config import OS_NAMES, OS_STYLE
from core.game import SlotGame
from functions.formatting import describe_result

SPIN_FRAMES = 15

class CasinoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OS Casino")
        self.geometry("600x640")
        self.resizable(False, False)

        self.game = SlotGame()
        self._frame = 0
        assets_dir = Path(__file__).parent / "assets"
        self.os_images = {
            name: self._load_os_image(assets_dir / style["icon"])
            for name, style in OS_STYLE.items()
        }

        ctk.CTkLabel(
            self, text="OS CASINO", font=ctk.CTkFont(size=32, weight="bold")
        ).pack(pady=(20, 5))

        self.score_label = ctk.CTkLabel(
            self, text="Очки: 0", font=ctk.CTkFont(size=22, weight="bold")
        )
        self.score_label.pack(pady=5)

        reels_frame = ctk.CTkFrame(self, corner_radius=20)
        reels_frame.pack(pady=20)

        self.reel_boxes = []
        for _ in range(3):
            box = ctk.CTkLabel(
                reels_frame,
                text="?",
                width=150,
                height=150,
                corner_radius=15,
                fg_color="#2b2b2b",
                font=ctk.CTkFont(size=16, weight="bold"),
            )
            box.pack(side="left", padx=12, pady=20)
            self.reel_boxes.append(box)

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
            "Linux x3: +500  |  FreeBSD 3x: +450 | NetBSD / OpenBSD x3: +250\n"
            "macOS x3: -300  |  Windows x3: -500"
        )
        ctk.CTkLabel(
            self, text=rules, font=ctk.CTkFont(size=13), text_color="gray"
        ).pack(pady=10)

    def start_spin(self):
        self.spin_button.configure(state="disabled")
        self.result_label.configure(text="Rolling...", text_color="white")
        self._frame = 0
        self._animate()

    def _animate(self):
        if self._frame < SPIN_FRAMES:
            for box in self.reel_boxes:
                self._show(box, random.choice(OS_NAMES))
            self._frame += 1
            delay = 50 + self._frame * 8
            self.after(delay, self._animate)
        else:
            reels, change = self.game.spin()
            for box, name in zip(self.reel_boxes, reels):
                self._show(box, name)

            self.score_label.configure(text=f"Points: {self.game.score}")
            text, color = describe_result(change)
            self.result_label.configure(text=text, text_color=color)
            self.spin_button.configure(state="normal")

    def _show(self, box: ctk.CTkLabel, name: str):
        style = OS_STYLE[name]
        box.configure(
            text=style["label"],
            image=self.os_images[name],
            compound="top",
            fg_color=style["color"],
            text_color=style["text"],
        )

    @staticmethod
    def _load_os_image(path: Path) -> ctk.CTkImage:
        with Image.open(path) as source:
            image = source.copy()
        return ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(76, 76),
        )

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = CasinoApp()
    app.mainloop()
