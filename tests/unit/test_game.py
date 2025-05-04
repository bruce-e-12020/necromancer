import pytest, os, ctypes
import pygame as pg
from src.game import Game
from src.settings import SCREEN_MARGIN, CAPTION, FPS, FPS_AVE_TIME, DEBUG

@pytest.fixture(scope="session")
def monitor_dimensions() -> tuple[int, int]:
    try:
        # Get DPI awareness
        awareness = ctypes.c_int()
        ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        # Get the DPI scale factor
        dpi = ctypes.windll.user32.GetDpiForSystem()
        scale_factor = dpi / 96.0  # 96 is the base DPI
    except Exception:
        scale_factor = 1.0
    # Initialize pygame with system display driver
    pg.init()
    info = pg.display.Info()
    # Apply scale factor to dimensions
    dimensions = (
        int(info.current_w * scale_factor),
        int(info.current_h * scale_factor)
    )
    return dimensions

@pytest.fixture
def game():
    """Create game instance with auto-run disabled"""
    game_instance = Game(auto_run=False)
    yield game_instance
    pg.display.quit()
    pg.quit()

def test_game_initialization(game):
    """Test if game initializes with correct settings"""
    assert pg.display.get_init()
    assert game.screen is not None
    assert isinstance(game.screen, pg.Surface)
    assert pg.display.get_caption()[0] == CAPTION

def test_screen_dimensions(monitor_dimensions, game):
    """Test if screen dimensions are calculated correctly"""

    expected_width = monitor_dimensions[0] - 2 * SCREEN_MARGIN
    expected_height = monitor_dimensions[1] - 2 * SCREEN_MARGIN 
    # for debugging, use pytest -v -s to show these print statements
    print(f"\nmonitor: {monitor_dimensions}")
    print(f"expected: ({expected_width}, {expected_height})")
    print(f"screen: ({game.screen_rect.width}, {game.screen_rect.height})\n")

    assert game.screen_rect.width == expected_width
    assert game.screen_rect.height == expected_height

def test_fps_tracking_initialization(game):
    """Test if FPS tracking is initialized correctly when debug is enabled"""
    if 'caption' in DEBUG:
        expected_maxlen = int(FPS_AVE_TIME * FPS)
        assert game.dt_list.maxlen == expected_maxlen

def test_update_caption(game):
    """Test if caption updates include all required information"""
    game.update_caption(16)  # Simulate ~60fps frame time
    caption = pg.display.get_caption()[0]
    
    assert CAPTION in caption
    assert 'FPS:' in caption
    assert 'Screen:' in caption
    assert 'Mouse:' in caption