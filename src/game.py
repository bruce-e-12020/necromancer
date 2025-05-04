import sys

import pygame as pg
from pygame import Surface, Rect
import numpy as np
from numpy.typing import NDArray

from .settings import SCREEN_MARGIN, CAPTION, DEBUG, FPS, FPS_AVE_TIME

class Game:
    def __init__(self) -> None:
        pg.init()
        monitor_info = pg.display.Info()
        mw: int = monitor_info.current_w
        mh: int = monitor_info.current_h
        sw: int = mw - 2 * SCREEN_MARGIN
        sh: int = mh - 2 * SCREEN_MARGIN
        self.screen: Surface = pg.display.set_mode((sw, sh))
        pg.display.set_caption(CAPTION)
        self.screen_rect: Rect = self.screen.get_rect()

        if 'caption' in DEBUG:
            self.dt_list: list[int] = []

        self.clock = pg.time.Clock()

        self.run()
    
    def run(self) -> None:
        keep_running: bool = True
        dt: int = self.clock.tick(FPS)
        while keep_running:
            if 'caption' in DEBUG:
                self.update_caption(dt)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    keep_running = False
                    pg.quit()
                    sys.exit()
            pg.display.update()
    
    def update_caption(self, dt: int) -> None:
        mx, my = pg.mouse.get_pos()
        tmp_mouse: str = f'Mouse: ({mx}, {my})'
        
        self.dt_list.append(dt)
        dt_array: NDArray = np.array(self.dt_list, dtype=np.float64)*0.001
        while np.sum(dt_array) > FPS_AVE_TIME:
            del self.dt_list[0]
            dt_array = np.array(self.dt_list, dtype=np.float64)*0.001
        num_frames: int = len(self.dt_list)
        tot_time: float = max(np.sum(dt_array), 0.001)
        fps: float = num_frames / tot_time
        tmp_fps: str = f'FPS: {num_frames} / {tot_time:.3f} = {fps:.1f}'
        tmp_screen: str = f'Screen: {self.screen_rect.width} x {self.screen.height}'
        caption: str = f'{CAPTION} -- {tmp_fps} -- {tmp_screen} -- {tmp_mouse}'
        pg.display.set_caption(caption)

        

