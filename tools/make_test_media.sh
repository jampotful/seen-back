#!/bin/sh
# Make the looping fake camera feed the browser checks use, from the test photo. Needs ffmpeg.
cd "$(dirname "$0")/../test" || exit 1
ffmpeg -hide_banner -loglevel error -y -loop 1 -i assets/garden.jpg \
  -vf "scale=900:-2,crop=640:360:x='(in_w-640)*(0.5+0.5*sin(2*PI*t/5))':y='(in_h-360)/2',drawbox=x='mod(130*t\,700)-50':y=150:w=36:h=36:color=red@1:t=fill,drawbox=x='320+150*sin(5*t)':y=260:w=22:h=22:color=white@1:t=fill" \
  -t 5 -r 30 -pix_fmt yuvj420p -q:v 4 -f mjpeg cam.mjpeg && ls -la cam.mjpeg
