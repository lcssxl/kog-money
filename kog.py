# -*- coding: utf-8 -*-


import logging
import os
from time import sleep

# 屏幕分辨率
device_x = 1920
device_y = 1080
# 通关顺序：0=再次挑战 -> 1=闭关 -> 2=跳过 -> 3=跳过 -> 4=点击屏幕继续 ->->
game_mode = 1
# 各步骤等待间隔
step_wait = [5, 48, 6, 5, 10]
# 刷金币次数
repeat_times = 60

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x = 1920.0
    base_y = 1080.0
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))


def do_money_work():

    logging.debug('#0 - start the game again')
    tap_screen(1600, 1000)
    sleep(step_wait[0])

    logging.debug('#1 - ready, go!!!')
    tap_screen(1500, 920)
    sleep(step_wait[1])

    #for i in range(2):
    #    logging.debug('#' + str(2+i) + ' - auto power on!')
    #    tap_screen(1800, 80)
    #    sleep(2+i)
    logging.debug('#2 - auto power on!')
    tap_screen(1800, 80)
    sleep(step_wait[2])
    logging.debug('#3 - auto power on!')
    tap_screen(1800, 80)
    sleep(step_wait[3])

    logging.debug('#4 - do it again...\n')
    tap_screen(1000, 1024)
    sleep(step_wait[4])


if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('round #{}'.format(i + 1))
        do_money_work()
