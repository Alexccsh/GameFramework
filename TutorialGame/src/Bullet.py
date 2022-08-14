import pygame
from mlgame.view.view_model import create_rect_view_data

class Bullet(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, is_player: bool, init_pos: tuple,play_area_rect:pygame.Rect):
        super().__init__()
        self._y_speed = 10
        self._init_pos = init_pos
        self._play_area_rect=play_area_rect
        self.rect = pygame.Rect(init_pos, (5, 8))
        self._is_player = is_player
        if self._is_player:
            self.color="#FF00FF"
        else:
            self.color="#0000ff"

    def update(self, *args, **kwargs) -> None:
        if self._is_player:
            self.rect.centery -= self._y_speed
        else:
            self.rect.centery += self._y_speed

        #當子彈的上方超出畫面的下方，從集合刪除子彈物件
        if self.rect.top>self._play_area_rect.bottom or self.rect.bottom<self._play_area_rect.top:
            self.kill()




    @property
    def game_object_data(self):
        return create_rect_view_data(name="bullet"
                                     , x=self.rect.x
                                     , y=self.rect.y
                                     , width=self.rect.width
                                     , height=self.rect.height
                                     , color=self.color
                                     , angle=0)


