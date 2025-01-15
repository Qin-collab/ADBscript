import os
import zipfile
import tarfile
import shutil

def extract_zip(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

def extract_gz(gz_path, extract_dir):
    with tarfile.open(gz_path, 'r:gz') as tar_ref:
        tar_ref.extractall(extract_dir)

def flash_firmware(package_path):
    try:
        # 检查ADB设备是否连接
        result = os.system('adb devices')
        if 'device' not in str(result):
            print("没有检测到连接的设备,请确保手机已连接并启用了USB调试模式。")
            return
        
        # 重启进入Fastboot模式
        os.system('adb reboot bootloader')
        print("手机正在重启进入Fastboot模式...")
        
        # 等待手机重启到Fastboot模式
        input("请确保手机已进入Fastboot模式后,按回车键继续...")
        
        # 解压线刷包
        extract_dir = 'firmware'
        if package_path.endswith('.zip'):
            extract_zip(package_path, extract_dir)
        elif package_path.endswith('.gz'):
            extract_gz(package_path, extract_dir)
        else:
            print("不支持的文件格式。请提供 .zip 或 .gz 文件。")
            return
        
        # 切换到解压后的目录
        os.chdir(extract_dir)
        
        # 执行刷机命令
        for file_name in os.listdir('.'):
            if file_name.endswith('.img'):
                flash_command = f'fastboot flash {file_name[:-4]} {file_name}'
                result = os.system(flash_command)
                if 'Finished' in str(result):
                    print(f"{file_name} 刷入成功！")
                else:
                    print(f"{file_name} 刷入失败，请检查文件路径和文件是否完整.")
        
        # 删除解压后的目录
        shutil.rmtree(extract_dir)
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    package_path = input("请输入线刷包的路径: ")
    flash_firmware(package_path)
