import os

def flash_boot_image(boot_image_path):
    try:
        # 检查ADB设备是否连接
        result = os.system('adb devices')
        if 'device' not in str(result):
            print("没有检测到连接的设备,请确保手机已连接并启用了USB调试模式.")
            return
        
        # 重启进入Fastboot模式
        os.system('adb reboot bootloader')
        print("手机正在重启进入Fastboot模式...")
        
        # 等待手机重启到Fastboot模式
        input("请确保手机已进入Fastboot模式后,按回车键继续...")
        
        # 刷入boot image
        flash_command = f'fastboot flash boot {boot_image_path}'
        result = os.system(flash_command)
        
        if 'Finished' in str(result):
            print("Boot刷入成功!")
        else:
            print("Boot刷入失败,请检查boot image文件路径和文件是否完整.")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    boot_image_path = input("请输入boot文件的路径: ")
    flash_boot_image(boot_image_path)
