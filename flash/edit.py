import os
import glob
import json
import pdb
import datetime
# os.environ["IMAGEMAGICK_BINARY"] = "C:/Program Files/ImageMagick-7.1.1-Q16/magick.exe"
import moviepy.editor as mp
import moviepy.editor
import moviepy.video
import moviepy.video.VideoClip
import whisper
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

from moviepy.editor import *
from moviepy.video.VideoClip import VideoClip
from django.core.files.base import ContentFile
from pathlib import Path
import numpy as np

import cloudinary
import cloudinary.uploader

MEDIA_ROOT = os.path.join(Path(__file__).resolve().parent.parent, 'media')
BASE_DIR = Path(__file__).resolve().parent.parent
#ファイルから音声認識して単語ごと秒数を記録
def recognition(path):
    files:list[str] = [path]
    model = whisper.load_model('tiny.en')
    for i, file in enumerate(files):
        print("## {}".format(file))
        result = model.transcribe(file, language='en', verbose=True, word_timestamps=True)
        # pdb.set_trace()
        result['segments']
    return result

#もし処理元のファイルが動画なら
#動画を生成、編集して単語ごとにテキストを表示
def make_movie(path,texts):
    clip = VideoFileClip(path)
    height,width = clip.size
    final_clip = VideoFileClip(path).subclip(0,1)
    # before_last = texts[0]['start']
    array = [clip]
    #単語ごとのテキストデータを秒数事にclipに書き込みそれをつなげて１つの動画にする
    for text in texts:
        #その単語のテキストを生成
        start_second = float(text['start'])
        end_second = float(text['end'])
        txtclip = TextClip(text['word'],font='AppliMincho/アプリ明朝.otf',fontsize=int(height*0.1),color='white',stroke_width=2,stroke_color='black').subclip(start_second,end_second)
        txtclip = txtclip.set_start(start_second)
        #配列に順番に入れる
        array.append(txtclip)
    #元動画にテキストを挿入
    final_clip = CompositeVideoClip(array)
        
    #動画の書き出し
    media_path = MEDIA_ROOT + '/videos'
    # pdb.set_trace()
    file_name = os.path.basename(path)
    path_name = path.rsplit(file_name,1)[0]
    output_path = os.path.join(media_path, 'リオ式'+file_name)
    write = final_clip.write_videofile(output_path)
    #cloudinaryにアップロード
    result = cloudinary.uploader.upload(write, public_id='リオ式'+file_name, resource_type="video")
    return result['secure_url'],output_path

# サムネイルを作るために動画の秒数で画像切り出し
def create_thumbnail(path):
    clip = VideoFileClip(path)

    file_name = str(datetime.datetime.now()) +"." + "jpeg"
    media_path = MEDIA_ROOT + '/images'
    output_path = os.path.join(media_path, 'リオ式'+file_name)
    thumbnails = clip.save_frame(output_path, t=1)
    # 保存した画像を読み込んで、ContentFileを作成
    with open(output_path, 'rb') as f:
        content_file = ContentFile(f.read())
    #cloudinaryにアップロード
    result = cloudinary.uploader.upload(content_file, public_id='リオ式'+file_name, resource_type="image")
    return output_path,result['secure_url']