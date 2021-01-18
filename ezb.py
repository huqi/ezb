import time
import logging
import pyautogui

BACK_POS = (42, 110)                    # 返回键的坐标
YKT_POS = (170, 990)                    # 云课堂的坐标
ZT_POS = (350, 177)                     # 专题的坐标
CENTER_POS = (250, 620)                 # 中心的坐标
NONE_POS = (0, 0)                       # 空坐标
FIRST_POS = (272, 214)                  # 第一集坐标
PLAY_POS = (284, 437)                   # 播放键坐标
WATCH_TIME = 5#50 * 60                  # 观看时间（秒）
ACTION_TIME = 0.5                       # 鼠标移动的时间
DELAY_TIME = 2                          # 每个动作的间隔时间
PLAY_DELAY_TIME = 10                    # 播放前再等一会儿
SCROLL = -500                           # 鼠标滚动的距离
GAP = 137                               # 每一集的间隔距离

logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s')

def delay(t):
    time.sleep(t)

def move_click(x, y, click):
    delay(DELAY_TIME)
    if x and y:
        pyautogui.moveTo(x, y, DELAY_TIME)
    if click:
        pyautogui.click()

def scroll():
    delay(DELAY_TIME)
    pyautogui.scroll(SCROLL)
    
def main():
    move_click(*YKT_POS, True)
    logging.info("点击“云课堂”")
    move_click(*ZT_POS, True)
    logging.info("点击“专题”")
    move_click(*CENTER_POS, False)
    logging.info("查找“必由之路”")
    for i in range(11):
        scroll()
    move_click(*NONE_POS, True)
    logging.info("点击“必由之路”")
    
    while True:
        for i in range(6):
            x, y = FIRST_POS[0], FIRST_POS[1]
            y = y + i * GAP
            move_click(x, y, True)
            logging.info("正在播放第%d集" % int(8 - i))            
            delay(PLAY_DELAY_TIME)
            move_click(*PLAY_POS, True)
            logging.info("点击播放")
            delay(WATCH_TIME)
            move_click(*BACK_POS, True)
            logging.info("点击返回")

        




if __name__ == "__main__":
    main()