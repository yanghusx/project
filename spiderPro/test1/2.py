# 安装必要库（先执行以下命令）
# pip install moviepy pillow

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from PIL import Image, ImageDraw, ImageFont
import os


# 1. 创建临时图片（用于演示）
def create_image(text, filename, size=(1920, 1080), bg_color=(30, 30, 30)):
    img = Image.new("RGB", size, bg_color)
    draw = ImageDraw.Draw(img)

    # 使用系统字体或指定字体文件
    try:
        font = ImageFont.truetype("Arial.ttf", 120)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    draw.text(
        ((size[0] - text_width) / 2, (size[1] - text_height) / 2),
        text,
        font=font,
        fill=(255, 255, 255)
    )
    img.save(filename)
    return filename


# 生成演示图片
img1 = create_image("Hello DeepSeek!", "frame1.jpg")
img2 = create_image("Python短视频生成", "frame2.jpg")
img3 = create_image("代码示例", "frame3.jpg")

# 2. 创建视频剪辑
clips = []
durations = [3, 3, 2]  # 每个片段的持续时间（秒）

# 创建带渐变的剪辑片段
for i, img in enumerate([img1, img2, img3]):
    clip = ImageClip(img).set_duration(durations[i])
    if i > 0:  # 添加渐变过渡
        clip = clip.crossfadein(1)
    clips.append(clip)

# 合并剪辑（添加转场效果）
final_clip = concatenate_videoclips(clips, padding=-0.5, method="compose")

# 3. 添加字幕
generator = lambda txt: TextClip(
    txt,
    fontsize=40,
    color="white",
    font="Arial",
    stroke_color="black",
    stroke_width=1
)
subtitles = SubtitlesClip([
    [(0, 2), "欢迎来到Python视频生成"],
    [(4, 6), "使用moviepy库"],
    [(7, 8), "DeepSeek技术支持"]
], generator)
final_clip = CompositeVideoClip([final_clip, subtitles.set_position(("center", "bottom"))])

# 4. 添加背景音乐
audio = AudioFileClip(r"D:\Down\alone-296348.mp3").volumex(0.5)
audio = audio.subclip(0, final_clip.duration)  # 匹配视频长度
final_clip = final_clip.set_audio(audio)

# 5. 输出视频
final_clip.write_videofile(
    "output_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True
)

# 清理临时文件
for f in [img1, img2, img3]:
    os.remove(f)