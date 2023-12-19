nofnof = "NöfNöf"
import simpleaudio

class KlinoffMath:
    wave_obj = simpleaudio.WaveObject.from_wave_file("nofnof.wav")
    @staticmethod
    def add(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a + b}\nAdded!! {nofnof}")

    @staticmethod
    def subtract(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a - b}\nSubtracted!! {nofnof}")

    @staticmethod
    def multiply(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a * b}\nMultiplied!! {nofnof}")

    @staticmethod
    def divide(a, b):
        if b == 0:
            play_obj = KlinoffMath.wave_obj.play()
            play_obj.wait_done()
            raise ValueError(f"Division by zero is not allowed... {nofnof} I am displeased {nofnof}")
        return print(f"{a / b}\nDivided!! {nofnof}")
