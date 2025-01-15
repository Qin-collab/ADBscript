import os

def reboot_to_fastboot():
    try:
        # 检查ADB设备是否连接
        result = os.system('adb devices')
        if 'device' not in str(result):
            print("没有检测到连接的设备,请确保手机已连接并启用了USB调试模式。")
            return
        
        # 重启进入Fastboot模式
        os.system('adb reboot bootloader')
        print("手机正在重启进入Fastboot模式...")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    reboot_to_fastboot()
