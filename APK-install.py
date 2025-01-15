import os

def install_apk(apk_path):
    try:
        # 检查ADB设备是否连接
        result = os.system('adb devices')
        if 'device' not in str(result):
            print("没有检测到连接的设备,请确保手机已连接并启用了USB调试模式。")
            return
        
        # 安装APK文件
        install_command = f'adb install {apk_path}'
        result = os.system(install_command)
        
        if 'Success' in str(result):
            print("APK安装成功!")
        else:
            print("APK安装失败,请检查APK文件路径和文件是否完整。")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    apk_path =input("请输入APK文件路径:")
    install_apk(apk_path)
