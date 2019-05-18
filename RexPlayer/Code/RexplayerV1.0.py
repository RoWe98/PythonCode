


# -*- coding: utf-8 -*-
import os
import tkinter
import tkinter.filedialog
import time
import threading
import pygame
import eyed3
from mutagen.mp3 import MP3


root = tkinter.Tk()
root.title('音乐播放器')
# 窗口大小及位置
root.geometry('460x600+500+100')

root.resizable(False, False)
folder = ''
res = []
num = 0
now_music = ''


# 添加文件函数
def buttonChooseClick():
    # 选择要播放的音乐文件夹

    global folder
    global res
    if not folder:
        folder = tkinter.filedialog.askdirectory()
        musics = [folder + '\\' + music

                  for music in os.listdir(folder) \
 \
                  if music.endswith(('.mp3', '.wav', '.ogg'))]
        # res = musics
        # print(res)
        ret = []
        for i in musics:
            ret.append(i.split('\\')[1:])
            res.append(i.replace('\\', '/'))
        var2 = tkinter.StringVar()
        var2.set(ret)
        lb = tkinter.Listbox(root, listvariable=var2)
        lb.place(x=50, y=130, width=260, height=300)
    if not folder:
        return
    global playing

    playing = True

    # 根据情况禁用和启用相应的按钮

    buttonPlay['state'] = 'normal'

    buttonStop['state'] = 'normal'

    # buttonPause['state'] = 'normal'

    pause_resume.set('播放')


# 播放音乐函数


def play():
    # 初始化混音器设备
    if len(res):
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                # 随机播放一首歌曲
                nextMusic = res[num]
                NewnextMusic = nextMusic.replace(folder,'')
                print("当前歌名为: {}".format(NewnextMusic))
                nextMusicName = nextMusic
                print("当前为第{}首歌".format(num + 1))
                pygame.mixer.music.load(nextMusic.encode())
                # 播放一次
                pygame.mixer.music.play(1)
                # print(len(res)-1)
                if len(res) - 1 == num:
                    num = 0
                else:
                    num = num + 1
                nextMusic = nextMusic.split('\\')[1:]
                musicName.set('playing....' + ''.join(nextMusic))
                audio = MP3(nextMusicName)
                MusicTime = int(audio.info.length)
                print(u"音乐时长为: <{}:{}>".format(MusicTime//60,MusicTime%60))
                print("\n")
            else:
                time.sleep(0.1)


# 点击播放
def buttonPlayClick():
    buttonNext['state'] = 'normal'

    buttonPrev['state'] = 'normal'
    # 选择要播放的音乐文件夹
    if pause_resume.get() == '播放':
        pause_resume.set('暂停')
        global folder

        if not folder:
            folder = tkinter.filedialog.askdirectory()

        if not folder:
            return

        global playing

        playing = True

        # 创建一个线程来播放音乐，当前主线程用来接收用户操作

        t = threading.Thread(target=play)

        t.start()

    elif pause_resume.get() == '暂停':
        # pygame.mixer.init()
        pygame.mixer.music.pause()

        pause_resume.set('继续')

    elif pause_resume.get() == '继续':
        # pygame.mixer.init()
        pygame.mixer.music.unpause()

        pause_resume.set('暂停')


# 停止播放
def buttonStopClick():
    global playing

    playing = False

    pygame.mixer.music.stop()


# 下一首
def buttonNextClick():
    global playing

    playing = False

    pygame.mixer.music.stop()
    #
    # pygame.mixer.quit()
    global num
    # num += 1
    # num -= 1
    if len(res) == num:
        num = 0
    # elif num < 0:
    #     num = 0
    # buttonPlayClick()
    # global playing
    #
    playing = True

    # 创建一个线程来播放音乐，当前主线程用来接收用户操作

    t = threading.Thread(target=play)

    t.start()


# 关闭窗口
def closeWindow():
    # 修改变量，结束线程中的循环

    global playing

    playing = False

    time.sleep(0.3)

    try:

        # 停止播放，如果已停止，

        # 再次停止时会抛出异常，所以放在异常处理结构中

        pygame.mixer.music.stop()

        pygame.mixer.quit()

    except:

        pass

    root.destroy()


# 声音控制
def control_voice(value=0.5):
    # 设置背景音乐的音量。取值从0.0到1.0。在新的音乐加载前设置,音乐加载时生效。
    # 注意; 音乐加载时生效
    pygame.mixer.music.set_volume(float(value))


# 上一首
def buttonPrevClick():
    global playing

    playing = False

    pygame.mixer.music.stop()
    #
    # pygame.mixer.quit()
    global num
    # num += 1
    # num -= 1
    if num == 0:
        num = len(res) - 2
        # num -= 1
    elif num == len(res) - 1:
        num -= 2
    else:
        num -= 2
        # num -= 1
    print(num)

    playing = True

    # 创建一个线程来播放音乐，当前主线程用来接收用户操作

    t = threading.Thread(target=play)

    t.start()


root.protocol('WM_DELETE_WINDOW', closeWindow)

buttonChoose = tkinter.Button(root, text='添加', command=buttonChooseClick)

buttonChoose.place(x=50, y=10, width=50, height=20)

# buttonChoose['state'] = 'disabled'
# 播放按钮
# now_music = res
# print(res)
pause_resume = tkinter.StringVar(root, value='播放')
buttonPlay = tkinter.Button(root, textvariable=pause_resume, command=buttonPlayClick)

buttonPlay.place(x=190, y=10, width=50, height=20)
buttonPlay['state'] = 'disabled'
# 停止播放
buttonStop = tkinter.Button(root, text='停止', command=buttonStopClick)

buttonStop.place(x=120, y=10, width=50, height=20)

buttonStop['state'] = 'disabled'

# 下一首
buttonNext = tkinter.Button(root, text='下一首', command=buttonNextClick)

buttonNext.place(x=260, y=10, width=50, height=20)

buttonNext['state'] = 'disabled'
# 上一首
buttonPrev = tkinter.Button(root, text='上一首', command=buttonPrevClick)

buttonPrev.place(x=330, y=10, width=50, height=20)

buttonPrev['state'] = 'disabled'

musicName = tkinter.StringVar(root, value='暂时没有播放音乐...')

labelName = tkinter.Label(root, textvariable=musicName)

labelName.place(x=10, y=30, width=260, height=20)

# HORIZONTAL表示为水平放置，默认为竖直,竖直为vertical
s = tkinter.Scale(root, label='音量', from_=0, to=1, orient=tkinter.HORIZONTAL,
                  length=240, showvalue=0, tickinterval=2, resolution=0.1, command=control_voice)
s.place(x=50, y=50, width=200)
# 启动消息循环
root.mainloop()
