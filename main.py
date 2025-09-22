import pygame
from setting import * #変数値を収容したsetting.pyファイルをインポート
from game import Game #Gameクラスをインポート

pygame.init()

#ウィンドウの作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('shooting game')

#FPSの設定
clock = pygame.time.Clock()

#ゲームクラスの呼び出し 変数gameに代入
game = Game()

#メインループ-----------------------------------------------------------------------
run = True
while run:
    
    #背景の塗りつぶし
    screen.fill(BLACK)
    
    #ゲームクラス内のrunメソッドを実行
    game.run()
    
    
    #イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    #更新
    pygame.display.update()
    clock.tick(FPS) #あらかじめ指定したフレームレート




#-----------------------------------------------------------------------------------

pygame.quit()