import pygame
from setting import * #変数値を収容したsetting.pyファイルをインポート

class Game:
    
    def __init__(self):
        #ゲーム画面がself.screenに入る
        self.screen = pygame.display.get_surface()
        
        #背景
        self.pre_bg_img = pygame.image.load('assets/img/background/bg.png')
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_height))
        self.bg_y = 0
        self.scroll_speed = 0.5
        
    #背景をスクロールさせるメソッド
    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height))
        self.screen.blit(self.bg_img, (0, self.bg_y))
        
        
    #実行メソッド
    def run(self):
        #blitメソッドで描画したい画像と描画する位置を指定 pygameの座標は画面左上が原点
        # self.screen.blit(self.bg_img, (0, 0))
        self.scroll_bg()
        
        