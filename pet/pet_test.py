from pet import Pet
import sys
import time
import os
try:
    import pygame
    _PYGAME_AVAILABLE = True
except ImportError:
    _PYGAME_AVAILABLE = False

class Spacer:
    """Utility class to print spacer lines."""

    @staticmethod
    def equal_spacer(count=70):
        return "=" * count

    @staticmethod
    def dash_spacer(count=175):
        return "-" * count

    @staticmethod
    def one_line_spacer():
        print()

    @staticmethod
    def small_spacer():
        for i in range(3):
            print()

    @staticmethod
    def screen_clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def low_bar_divider(count=86):
        return "  " + "▄" * count

    @staticmethod
    def high_bar_divider(count=86):
        return "  " + "▀" * count


class Effects:
    """Utility class to print various effects."""

    @staticmethod
    def slowtype(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class Sound:
    # ── File names (place these in pet/assets/sounds/) ─────────────────
    MUSIC_BG_FILE     = "pet_care_bgm.mp3"
    SFX_START_FILE    = "start.wav"
    SFX_QUIT_FILE     = "quit.wav"
    SFX_NAVIGATE_FILE = "select.wav"
    SFX_ERROR_FILE    = "error.wav"
    SFX_FEED_FILE     = "feed.wav"
    SFX_PLAY_FILE     = "play.wav"
    SFX_STAT_UP_FILE  = "stat_up.wav"
    SFX_PROFILE_FILE  = "profile_card_view.wav"
    SFX_CAT_FILE      = "cat.wav"  
    SFX_DOG_FILE      = "dog.wav"
    SFX_BIRD_FILE     = "bird.wav"
    SFX_FISH_FILE     = "fish.wav"
    SFX_TURTLE_FILE   = "turtle.wav"
    SFX_RABBIT_FILE   = "rabbit.wav"

    
    # ── Volume levels (0.0 – 1.0) ─────────────────────────────────────
    MUSIC_VOLUME  = 0.4   # background music — keep lower than SFX
    SFX_VOLUME    = 0.7   # all sound effects
 
    # ── Fade durations (milliseconds) ─────────────────────────────────
    MUSIC_FADE_IN  = 1500
    MUSIC_FADE_OUT = 2000
 
    _ready = False
    _sound_dir = None
    _sounds = {}  # cache for loaded sound effects
 
    @staticmethod
    def init():
        """Call once at the very start of the app."""
        if not _PYGAME_AVAILABLE:
            return
        try:
            pygame.mixer.init()
            Sound._ready = True
            script_dir = os.path.dirname(__file__)
            Sound._sound_dir = os.path.join(script_dir, "assets", "sounds")
            os.makedirs(Sound._sound_dir, exist_ok=True)
        except Exception:
            pass
 
    @staticmethod
    def _get_path(filename):
        """Get full path to a sound file."""
        if Sound._sound_dir:
            return os.path.join(Sound._sound_dir, filename)
        return filename
 
    @staticmethod
    def _load_sfx(name, filepath):
        """Load a sound effect into cache."""
        if not Sound._ready:
            return None
        try:
            full_path = Sound._get_path(filepath)
            if os.path.exists(full_path):
                sfx = pygame.mixer.Sound(full_path)
                sfx.set_volume(Sound.SFX_VOLUME)
                Sound._sounds[name] = sfx
                return sfx
        except Exception:
            pass
        return None
 
    @staticmethod
    def play_sfx(name, filepath, volume=None):
        """Play a sound effect once (non-blocking)."""
        if not Sound._ready:
            return
        if name not in Sound._sounds:
            Sound._load_sfx(name, filepath)
        sfx = Sound._sounds.get(name)
        if sfx:
            vol = volume if volume is not None else Sound.SFX_VOLUME
            sfx.set_volume(vol)
            sfx.play()
 
    @staticmethod
    def play_music():
        """Start background music on infinite loop with fade-in."""
        if not Sound._ready:
            return
        path = Sound._get_path(Sound.MUSIC_BG_FILE)
        if os.path.exists(path):
            try:
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(Sound.MUSIC_VOLUME)
                pygame.mixer.music.play(loops=-1, fade_ms=Sound.MUSIC_FADE_IN)
            except Exception:
                pass
 
    @staticmethod
    def stop_music(fade_ms=None):
        """Stop background music with fade-out."""
        if not Sound._ready:
            return
        fade = fade_ms if fade_ms is not None else Sound.MUSIC_FADE_OUT
        try:
            pygame.mixer.music.fadeout(fade)
        except Exception:
            pass
 
    # ── Named shortcuts (call these in App instead of play_sfx) ───────
 
    @staticmethod
    def on_start():
        Sound.play_sfx("start", Sound.SFX_START_FILE)
 
    @staticmethod
    def on_quit():
        Sound.stop_music()
        Sound.play_sfx("quit", Sound.SFX_QUIT_FILE)
 
    @staticmethod
    def on_navigate():
        Sound.play_sfx("navigate", Sound.SFX_NAVIGATE_FILE)
 
    @staticmethod
    def on_error():
        Sound.play_sfx("error", Sound.SFX_ERROR_FILE)
 
    @staticmethod
    def on_feed():
        Sound.play_sfx("feed", Sound.SFX_FEED_FILE)
 
    @staticmethod
    def on_play():
        Sound.play_sfx("play", Sound.SFX_PLAY_FILE)
 
    @staticmethod
    def on_stat_up():
        Sound.play_sfx("stat_up", Sound.SFX_STAT_UP_FILE)
 
    @staticmethod
    def on_profile():
        Sound.play_sfx("profile", Sound.SFX_PROFILE_FILE)
 
    @staticmethod
    def on_cat():
        Sound.play_sfx("cat", Sound.SFX_CAT_FILE)
 
    @staticmethod
    def on_dog():
        Sound.play_sfx("dog", Sound.SFX_DOG_FILE)
 
    @staticmethod
    def on_bird():
        Sound.play_sfx("bird", Sound.SFX_BIRD_FILE)
 
    @staticmethod
    def on_fish():
        Sound.play_sfx("fish", Sound.SFX_FISH_FILE)
 
    @staticmethod
    def on_turtle():
        Sound.play_sfx("turtle", Sound.SFX_TURTLE_FILE)
 
    @staticmethod
    def on_rabbit():
        Sound.play_sfx("rabbit", Sound.SFX_RABBIT_FILE)


def title():
    return("""
                                                         ██████╗ ███████╗████████╗     ██████╗ █████╗ ██████╗ ███████╗
                                                         ██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝
                                                         ██████╔╝█████╗     ██║       ██║     ███████║██████╔╝█████╗  
                                                         ██╔═══╝ ██╔══╝     ██║       ██║     ██╔══██║██╔══██╗██╔══╝  
                                                         ██║     ███████╗   ██║       ╚██████╗██║  ██║██║  ██║███████╗
                                                         ╚═╝     ╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
""")

def ascii_pet(animal_type):
    """Return ASCII art based on pet type."""
    ascii_map = {
        "Cat": r"""
                                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⣄⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⢀⣤⡤⣀⡀⠀⠀⠀⣀⢷⠊⢁⢻⣆⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠸⣤⡚⠃⢪⠓⠊⠉⠀⠀⠈⠀⠹⡿⡀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠈⡿⢴⡐⠁⠀⠀⠀⠀⠀⢀⣠⣄⡀⠑⣄⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⢹⢻⠀⢀⣤⣤⡀⠀⠀⠛⠿⠟⠀⠀⠈⢲⠄
                                                                            ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠻⠾⠟⠃⠰⣶⣀⠴⠀⠀⠀⠀⣨⠃
                                                                            ⠀⠀⠀⠀⠀⠀⢜⡀⠀⠀⠀⠀⠀⠘⠯⠼⠀⠀⢀⡠⢺⣅⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠈⢳⣤⠄⡀⠀⢀⣀⠀⠀⠀⠞⠁⠀⠀⢳⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁
                                                                            ⠀⣠⠔⠚⢉⠝⡝⠉⠀⠀⠇⠠⡀⠀⠀⠀⠀⠀⠀⠀⣰⢫⠀
                                                                            ⢰⠁⠀⢀⠃⢔⠁⠀⠀⠀⠇⠀⠈⢦⡀⠀⠀⠀⢀⠔⠁⢸⠀
                                                                            ⡗⠀⠀⠈⠀⡈⠀⠀⠀⠀⠀⢀⠀⠀⠑⢄⠀⡠⠂⠀⡆⡘⠀
                                                                            ⢹⡀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⢂⠀⠀⠀⢋⠀⠀⠸⠀⡇⠀
                                                                            ⠀⠙⠦⢤⣄⠀⢂⠀⠀⠀⠀⠀⠈⠆⠀⠀⢸⠀⠀⡸⠋⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠉⠁⠙⠦⢴⠄⣀⡀⢴⣐⣀⠦⠤⠤⠋⠀⠀⠀
""",
        "Dog": r"""
                                                                          ⠀⠀⠀⠀⢀⣠⡤⣀⣀⣠⠤⠤⠤⠤⠤⢤⡠⠐⠛⠒⠲⣄⠀⠀⠀⠀⠀⠀
                                                                          ⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⡀⠀⠀⠀
                                                                          ⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀
                                                                          ⢸⡀⠀⣀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⢄⠉⢿⠒⠋⠀⠀⠀
                                                                          ⠀⠉⠉⣱⢱⠀⠀⢰⣾⣦⠀⠀⠀⡀⢰⣿⣿⡆⠀⠀⠈⢣⣄⣑⡢⠀⠀⠀
                                                                          ⠀⠀⠸⠥⡇⠀⠀⠈⠛⠋⠸⡚⢒⡇⠀⠉⠉⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠜⠁⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⢩⠓⡆⠀⢠⠀⠀⠀⠀⠀⠀⣞⠀⢀⣹⠓⡄⠀⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⡳⠤⣙⣖⢸⠀⠀⠀⠀⠀⠀⣿⡥⣝⣡⠤⡞⠀⠀⠀⠀⣠⡀
                                                                          ⠀⠀⠀⠀⡰⠀⠀⠀⢹⣈⡆⠀⠀⠀⠀⢰⢯⣤⠇⠀⠀⠘⡄⢀⡶⡴⠁⢷
                                                                          ⠀⠀⠀⠀⡇⠀⠀⡔⠀⠉⡇⠀⠀⠀⠀⢸⠀⠀⠀⡆⠀⠀⢷⠞⠀⠀⠀⣸
                                                                          ⠀⠀⠀⠠⣇⣀⡤⠃⠀⢀⠃⠀⠀⠀⠀⢸⠀⠀⠀⠸⢄⢀⣸⠀⠀⠀⣰⠃
                                                                          ⠀⠀⠀⠀⣸⣍⠀⠀⠀⢸⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠈⣹⣧⡤⠔⠋⠁⠀
                                                                          ⠀⠀⠀⠀⠛⠺⡽⣯⣶⡇⢀⣀⣀⣀⣀⣀⣳⣶⣉⣿⣽⠷⠛⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⠀⣇⡄⡀⣰⠉⠀⠀⠀⠀⠀⠹⡀⠀⣄⡏⠀⠀⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
""",
        "Bird": r"""
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠶⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢟⣹⡮⡦⢀⣀⢡⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠕⠒⠀⠉⠒⠢⣍⡲⢄⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡃⠀⠀⢀⠀⢰⣷⠈⡎⡶⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠁⠈⠉⠉⢏⠀⠀⠀⠀⡏⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣍⠀⠀⠀⠀⠀⣀⡠⠜⠃⠀⠀⣰⠧⠤⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢳⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⣀⠴⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⣠⠞⠁⠀⣼⣥⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠒⢷⡒⠢⡜⢁⣴⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⢠⣇⢀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡗⢢⠤⠤⠤⠤⢤⠤⡤⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢡⠃⠀⠀⠀⢀⡞⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣔⣊⣁⡎⠀⠀⣤⣔⣊⣀⡧⠀⠀⠀⠀⠀⠀
""",
        "Fish": r"""
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⢻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡄⠀⢠⡞⠁⠀⢼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⠹⣶⠏⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣯⠁⠉⠀⠀⠀⠀⢾⠗⠛⣛⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠴⠿⠛⣦⣤⣀⣀⠀⠀⠀⠀⣴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⢀⡤⠶⠋⠁⠀⠀⠀⠀⠀⢹⣆⣰⣽⡗⢲⣬⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⢀⣴⠋⠀⠀⣠⡴⠶⠶⣄⠀⠀⠈⣯⠉⢳⡀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⢀⣴⣿⣤⡀⠀⣸⡇⠀⢲⠀⠘⣧⠀⠀⢽⡆⢀⡟⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⡄
                                                                        ⠀⠙⢻⣷⣿⠀⠸⣧⡀⠀⠀⣰⠇⢀⣤⣾⣿⡿⣦⣤⣤⣶⣦⣾⣿⣧⠀⠀⢀⣠⣶⡿⣿⡿⠿⢿⡏⠁
                                                                        ⠀⠀⠘⣿⢻⡧⣿⢮⡍⠙⠋⣡⣴⡿⢟⣉⣍⣭⣭⣿⣯⣭⠟⢻⡇⠹⣦⠖⣫⠟⠙⣏⢀⡀⣄⣼⠁⠀
                                                                        ⠀⢠⣾⣿⣿⠇⠈⠳⣽⣆⢸⣿⣿⣗⡋⠉⠀⠀⠀⣰⠟⠁⠀⣼⠀⠀⢿⣾⠷⠚⠛⠉⠉⠉⣹⠃⠀⠀
                                                                        ⠀⣿⡿⢿⡿⣄⠀⠀⢻⣿⡆⠈⠛⢯⣙⠛⠲⠄⣼⠃⠀⠀⢰⡏⠀⢀⡿⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀
                                                                        ⠀⢻⣿⠈⠳⣌⡳⢦⣼⣿⣧⠀⠀⢀⡞⢻⣦⣄⣿⠀⠀⢠⡾⢀⣴⢿⠿⡆⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀
                                                                        ⠀⠈⢿⣇⠀⠀⠙⠻⣽⣿⣗⣶⣴⣏⣠⠾⠂⣈⠙⣂⣤⡾⠗⠋⢸⣾⡇⠙⣄⠀⠀⣻⡇⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠈⢿⣆⠀⠀⠀⠀⣿⣿⠉⠉⠙⠛⠛⠛⢯⣉⠉⠀⠀⠀⠀⠘⣿⣷⡀⠈⠳⣄⣽⠃⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠈⢿⣆⠀⠀⢠⣿⣿⡇⠀⡀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠈⢯⣧⡀⢀⡾⠃⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⢘⣿⡄⠀⠛⠋⢿⣿⡶⠛⣆⠀⢠⡦⣤⣀⣳⣄⠀⠀⠀⠀⠈⠳⣷⡟⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⢨⣿⡗⠀⠀⠀⠈⢻⣿⣄⠈⠻⡾⠀⠀⠀⠉⠋⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⣼⡟⠁⠀⠀⠀⠀⠀⠘⢯⡷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
        "Turtle": r"""
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠤⠴⠶⠖⠒⠲⠶⠤⢤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠋⠉⠈⣡⠀⠒⠒⠂⠒⠀⠹⡁⠀⠀⠀⠈⠉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⢹⢛⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠥⠤⠤⠶⠤⢤⣘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣰⠤⠤⡀⣀⣼⡈⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⣠⠔⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠈⠓⢄⠀⠀⠹⣄⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠤⠤⠤⢀⡀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⡤⡄⣘⣦⠀⠀⠀⠀
                                                                ⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠈⠦⡀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠹⣇⠀⠀⠀
                                                                ⠀⡼⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠀⠙⢂⡤⠤⠤⠤⠤⢼⠃⠀⠀⠀⠀⠻⡄⠀⠀
                                                                ⢨⡇⢺⣿⣯⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢿⣇⡀⠀⠀⠀⠀⣧⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⣿⠀⠀
                                                                ⢸⡇⠈⠛⠛⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠘⢿⣾⠟⠁⠀⠀⠀⠀⣱⠤⠦⠀⢀⣏⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⣀⠠⠔⠻⣆⡀
                                                                ⠈⣇⠀⠀⠀⠀⠀⠀⠉⠒⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢐⣆⣀⠀⠀⣼⠉⠐⠒⠒⠒⡒⠒⠊⣁⣀⣤⣵⣄⣈⡷
                                                                ⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠾⠋⠁⠀⠈⠉⠑⠣⡀⠀⠀⠀⠀⣧⡠⠞⠉⠀⠀⠀⣆⠀⠀
                                                                ⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⢴⡏⠀⠀⠀⠀⠀⠀⣸⣠⣌⡷⠲⠶⠿⢿⠶⠒⠁⠀⠀⠀⢿⠀⠀
                                                                ⠀⠀⠀⠀⣾⠀⠉⠉⠒⠒⠒⢲⠖⠒⠒⠒⠓⠋⠉⠁⠀⢰⡇⠀⠀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⢾⡂⠀⠀⠀⠀⠀⣼⠀⠀
                                                                ⠀⠀⠀⠀⠈⠳⠤⠤⣀⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣅⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠈⠓⠤⠤⠤⠴⠚⠁⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠂⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
        "Rabbit": r"""
                                                                        ⢠⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⢰⠀⠀⠑⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠸⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⢇⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠶⡀⠀⠀
                                                                        ⠀⠈⡄⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠱⠀⠀
                                                                        ⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⡇⠀
                                                                        ⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢳⠀
                                                                        ⠀⠀⠀⠀⠀⠳⣄⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⣼⠀
                                                                        ⠀⠀⠀⠀⠀⠀⢀⠵⠞⠁⠀⠀⠀⠈⢉⠦⠤⠄⣀⠀⠀⠀⠀⠀⠀⢀⠏⠀
                                                                        ⠀⠀⠀⠀⠀⢰⣏⣽⢳⢇⣀⣀⠤⠒⣁⡀⠀⠀⠀⠉⠒⠺⡒⠢⢤⠎⠀⠀
                                                                        ⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠈⠲⡀⠈⡆⠀
                                                                        ⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠛⢟⠛⠈⢖⢓⡤
                                                                        ⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠁⠀⡆⠀⠈⠣⠀⠈⣦⠇
                                                                        ⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠒⢄⠀⡇⠀⠀⠀⠀⠀⢹⠀
                                                                        ⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠈⣤⠁⠀⠀⠀⠀⠀⢸⠀
                                                                        ⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠀⠒⠁⠀⠀⠀⠀⠀⠀⠇⠀
                                                                        ⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠈⠑⠢⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠔⠋⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠒⠀⠀⠀⠒⠒⠉⠁⠀⠀⠀⠀⠀⠀
"""
    }
    return ascii_map.get(animal_type)

def manual_center(text, width=175):
    if len(text) >= width:
        return text
    padding = (width - len(text)) // 2
    return ' ' * padding + text

def separator(title_text="", total_width=175):
    """Return a centered separator line with optional title."""
    line_width = 70  # Width of the separator itself
    if title_text:
        pad = (line_width - len(title_text) - 2) // 2
        sep_line = f"{'═' * pad} {title_text} {'═' * pad}"
    else:
        sep_line = "─" * line_width
    
    # Center the entire separator line within total_width
    padding = (total_width - len(sep_line)) // 2
    return f"\n{' ' * padding}{sep_line}"

def animate_stat(label, from_val, to_val, max_val=10, bar_width=10, step_delay=0.3):
    """Animate a stat bar filling or draining (centered)."""
    direction = 1 if to_val >= from_val else -1
    for val in range(from_val, to_val + direction, direction):
        filled = round((val / max_val) * bar_width)
        bar = '█' * filled + '░' * (bar_width - filled)
        if label:
            animation_line = f'{label}: [{bar}] {val:>2}/{max_val}'
        else:
            animation_line = f'[{bar}] {val:>2}/{max_val}'
        padding = (175 - len(animation_line)) // 2
        sys.stdout.write(f'\r{" " * padding}{animation_line}')
        sys.stdout.flush()
        time.sleep(step_delay)
    print()

class App():
    
    @staticmethod
    def main():
        Sound.init()
        Spacer.screen_clear()
        print(title())
        time.sleep(0.4)
        input(manual_center("Press Enter to proceed..."))
        Sound.on_start()
        time.sleep(0.2)
        Sound.play_music()

        # ── Pet Input ─────────────────────────────────────────────
        name = None
        animal_type = None
        age = None

        Spacer.screen_clear()
        print(title())
        Effects.slowtype(separator("Register Your Pet"), delay=0.01)
        Spacer.one_line_spacer()

        # ── Name Input ────────────────────────────────────────────
        while name is None:
            try:
                name_input = input(' ' * 62 + "Pet's Name      : ").strip()
                if not name_input:
                    raise ValueError("Name cannot be empty.")
                name = name_input
            except ValueError as e:
                print(manual_center(f"      {e}"))
                time.sleep(1.5)
                Spacer.screen_clear()
                print(title())
                print(separator("Register Your Pet")) 
                Spacer.one_line_spacer()

        # ── Animal Type Input ─────────────────────────────────────
        while animal_type is None:
            Spacer.screen_clear()
            print(title())
            print(separator("Register Your Pet"))
            Spacer.one_line_spacer()
            print(' ' * 62 + f"Pet's Name      : {name}")
            
            try:
                atype_input = input(' ' * 62 + "Animal Type     : ").strip()
                if not atype_input:
                    raise ValueError("Animal type cannot be empty.")
                atype_input = atype_input.title()
                if atype_input not in Pet.ANIMAL_TYPES:
                    raise ValueError(f"Animal type must be one of: {', '.join(Pet.ANIMAL_TYPES)}")
                animal_type = atype_input
            except ValueError as e:
                print(manual_center(f"      {e}"))
                time.sleep(1.5)

        # ── Age Input ─────────────────────────────────────────────
        while age is None:
            Spacer.screen_clear()
            print(title())
            print(separator("Register Your Pet"))
            Spacer.one_line_spacer()
            print(' ' * 62 + f"Pet's Name      : {name}")
            print(' ' * 62 + f"Animal Type     : {animal_type}")
            
            try:
                age_input = input(' ' * 62 + "Age (years)     : ").strip()
                if not age_input:
                    raise ValueError("Age cannot be empty.")
                try:
                    age_value = int(age_input)
                except ValueError:
                    raise ValueError("Age must be a whole number (e.g., 3, 5, 10).")
                if age_value < 0 or age_value > 100:
                    raise ValueError("Age must be between 0 and 100.")
                age = age_value
            except ValueError as e:
                print(manual_center(f"      {e}"))
                time.sleep(1.5)

        my_pet = Pet(name, animal_type, age)
        print(separator())
        time.sleep(0.005)

        # ── Profile Screen ────────────────────────────────────────
        Spacer.screen_clear()
        print(title())
        Effects.slowtype(ascii_pet(my_pet.get_animal_type()), delay=0.001)
        Effects.slowtype(manual_center(f"{my_pet}"), delay=0.01)
        Spacer.one_line_spacer()
        print(manual_center(my_pet.profile_card()))
        Spacer.one_line_spacer()
        time.sleep(1.2)

        # ── Interactive Care Launcher ─────────────────────────────
        App.interactive_care(my_pet)

        # ── Final Profile ─────────────────────────────────────────
        Spacer.screen_clear()
        print(title())
        Effects.slowtype(ascii_pet(my_pet.get_animal_type()), delay=0.001)
        Effects.slowtype(separator("Final Profile"), delay=0.01)
        Spacer.one_line_spacer()
        print(manual_center(my_pet.profile_card()))
        Spacer.one_line_spacer()
        time.sleep(1.2)
        print(manual_center(Spacer.equal_spacer()))
        time.sleep(2)

        # ── Outro ─────────────────────────────────────────────────
        Spacer.screen_clear()
        print(title())
        print(ascii_pet(my_pet.get_animal_type()))
        Spacer.one_line_spacer()
        print(manual_center(Spacer.equal_spacer()))
        Spacer.one_line_spacer()
        Effects.slowtype(manual_center("Thank you for testing the Pet class!"), delay=0.01)
        time.sleep(0.4)
        Effects.slowtype(manual_center(f"Take good care of {my_pet.get_name()}! "), delay=0.01)
        Spacer.one_line_spacer()
        print(manual_center(Spacer.equal_spacer()))
        Sound.on_close()
        time.sleep(2)
        Spacer.screen_clear()
    
    @staticmethod
    def interactive_care(pet):
        """Interactive care mode — player chooses to feed or play."""
        while True:
            Spacer.screen_clear()
            print(title())
            print(ascii_pet(pet.get_animal_type()))
            print(separator("Interactive Pet Care"))
            Spacer.one_line_spacer()
            Effects.slowtype(manual_center("Feed (F) or Play (P)? Type 'Q' to finish"), delay=0.01)
            Spacer.one_line_spacer()
            print(manual_center(pet.profile_card()))
            Spacer.one_line_spacer()
            
            choice = input(manual_center("Action (F/P/Q) : ")).strip().upper()

            if choice == 'Q':
                Spacer.screen_clear()
                print(title())
                print(manual_center("Time for rest..."))
                time.sleep(2)
                break
            elif choice == 'F':
                hunger_before = pet.get_hunger()
                msg = pet.feed()
                hunger_after = pet.get_hunger()
                
                Spacer.screen_clear()
                print(title())
                print(ascii_pet(pet.get_animal_type()))
                print(manual_center(msg))
                Spacer.one_line_spacer()

                fullness_before = Pet.MAX_HUNGER - hunger_before
                fullness_after = Pet.MAX_HUNGER - hunger_after
                Effects.slowtype(manual_center("Fullness bar:", width=175), delay=0.015)
                Spacer.one_line_spacer()
                animate_stat("Fullness", fullness_before, fullness_after, step_delay=0.25)

                Spacer.one_line_spacer()
                print(manual_center(pet.profile_card()))
                Spacer.one_line_spacer()
                input(manual_center("Press Enter to continue..."))
            elif choice == 'P':
                happiness_before = pet.get_happiness()
                msg = pet.play()
                happiness_after = pet.get_happiness()
                
                Spacer.screen_clear()
                print(title())
                print(ascii_pet(pet.get_animal_type()))
                print(manual_center(msg))
                Spacer.one_line_spacer()

                Effects.slowtype(manual_center("Happiness bar:", width=175), delay=0.015)
                Spacer.one_line_spacer()
                animate_stat("Happiness", happiness_before, happiness_after, step_delay=0.25)

                Spacer.one_line_spacer()
                print(manual_center(pet.profile_card()))
                Spacer.one_line_spacer()
                input(manual_center("Press Enter to continue..."))
            else:
                print(manual_center("    Invalid action. Please enter F, P, or Q."))
                time.sleep(1.2)


if __name__ == "__main__":
    App.main()

