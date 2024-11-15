import time
import board
import busio
import adafruit_vl53l0x

pii2c = busio.I2C(board.SCL, board.SDA)
makerobo_vl53 = adafruit_vl53l0x.VL53L0X(pii2c)

# 程序入口
if __name__ == '__main__':
    try:
        # 循环持续输出距离值
        while True:
            print("Range: {0}mm".format(makerobo_vl53.range))   # 打印出距离值
            time.sleep(1.0)                                     # 延时1s
    except KeyboardInterrupt:
        print("Exit")  # Exit on CTRL+C