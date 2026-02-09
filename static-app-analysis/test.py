import subprocess
import time
import os
from PIL import Image
from alive_progress import alive_bar

APP_INSTALL_PATH = './apks/'
ID = '7e0227c5'
SCREENSHOT_FILENAME = f'screen-{ID}.png'
x = '540'
y = '2330'
packages_med = ['com.goodreads']

green_pixels = [(300, 750), (360, 875), (710, 590), (770, 700)]
grey_pixels = [(280, 750), (480, 580), (570, 790), (800, 715)]
# subprocess.run(['adb', '-s', ID, 'shell', 'input', 'tap', x, y], check=True)

def open_app_playstore_page(package):
    try:
        subprocess.run(['adb', '-s', ID, 'shell', 'am', 'start', '-a', 'android.intent.action.VIEW', '-d', f'market://details?id={package}'])
        return True
    
    except subprocess.CalledProcessError as e:
        print(f'Open play store for package [{package}]\r\nFunction failed with exit code: {e.returncode}')
        return False


def screenshot():
    try:
        subprocess.run(['adb', '-s', ID, 'shell', 'screencap', '-p', f'/storage/emulated/0/{SCREENSHOT_FILENAME}'])
        subprocess.run(['adb', '-s', ID, 'pull', f'/storage/emulated/0/{SCREENSHOT_FILENAME}'])
        subprocess.run(['adb', '-s', ID, 'shell', 'rm', f'/storage/emulated/0/{SCREENSHOT_FILENAME}'])
        return SCREENSHOT_FILENAME

    except subprocess.CalledProcessError as e:
        print(f'Screenshot function failed with exit code: {e.returncode}')
        return False
    
# def get_sub(pic, x, y):
#     temp = []
#     for j in range(16):
#         for i in range(135):
#             temp.append(pic[x+i, y+j])
#     return temp 

def find_blue_rectangle(filename):
    img = Image.open(filename)
    pic = img.load()

    for coord in grey_pixels:
        print(pic[coord[0], coord[1]])

    # for j in range(150):
    #     for i in range(8):
    #         if is_all_blue(get_sub(pic, i*135, j*16)):
    #             print(i*135, j*16)
    #             return (i*135, j*16)
    # return False

# def check_if_app_exists(filename):
#     img = Image.open(filename)
#     pic = img.load()

#     for j in range(150):
#         for i in range(8):
#             if is_all_blue(get_sub(pic, i*135, j*16)):
#                 print(i*135, j*16)
#                 return (i*135, j*16)
#     return False


#subprocess.run(['adb', '-s', ID, 'uninstall', f'{packages_med[0]}'])

# print(os.path.isfile(f'{APP_INSTALL_PATH}{packages_med[0]}.apk'))
# print(f'{APP_INSTALL_PATH}{packages_med[0]}.apk')

# open_app_playstore_page(packages_med[0])

# result = subprocess.run(['adb', 'shell', 'pm list packages'], capture_output=True, text=True, check=True)

# print(result.stdout)

# print(packages_med[0] in result.stdout)

# with alive_bar(10) as bar:
#     for i in range(10):
#         time.sleep(1)
#         bar()

find_blue_rectangle(SCREENSHOT_FILENAME)