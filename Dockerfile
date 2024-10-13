FROM python:3.10
WORKDIR /mysite
COPY requirements.txt .
#ffmpegの構築
RUN apt-get update && apt-get install -y ffmpeg && apt-get install -y imagemagick
# RUN apt-get update && apt-get install -y \
#       wget \
#       xz-utils
# RUN wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz \
#       && tar xvf ./ffmpeg-git-amd64-static.tar.xz \
#       && cp ./ffmpeg*amd64-static/ffmpeg /usr/local/bin/
#ImageMagickの構築
# RUN mkdir -p /tmp/distr && \
#     cd /tmp/distr && \
#     wget https://download.imagemagick.org/ImageMagick/download/releases/ImageMagick-7.0.11-2.tar.xz && \
#     tar xvf ImageMagick-7.0.11-2.tar.xz && \
#     cd ImageMagick-7.0.11-2 && \
#     ./configure --enable-shared=yes --disable-static --without-perl && \
#     make && \
#     make install && \
#     ldconfig /usr/local/lib && \
#     cd /tmp && \
#     rm -rf distr
# RUN sed -i '/<policy domain="path" rights="none" pattern="@\*"/d' /etc/ImageMagick-6/policy.xml 
#フォントのインストール
COPY AppliMincho .
COPY policy.xml /etc/ImageMagick-6/
#moduleのインストール
RUN pip install --upgrade --root-user-action=ignore pip
RUN pip install --upgrade --root-user-action=ignore setuptools
RUN pip install -r requirements.txt
CMD ["python","manage.py","runserver","0.0.0.0:$PORT"]