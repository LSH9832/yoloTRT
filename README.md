# yolo_result_provider

主要给Nvidia Jetson系列嵌入式设备使用的，程序使用tensorrt推理模型，并将结果发送到服务器，接收demo见DataServer.py。
网络输入输出适配于yolox。

## 安装
```
git clone https://github.com/LSH9832/yolo_result_provider.git
cd yolo_result_provider && sh setup.sh
```

## 使用
```
./detect -e          /path/to/your/tensorrt_engine_file, 在model文件夾中已經提供了四個engine文件
         -no-push    stop pushing rtmp stream，列舉此選項將不會進行推流
         -post       post json result(default false) 列舉此項將向服務器發送json數據，具體見DataServer.py
         -show       show image(default false), 列舉此項將在本地端顯示圖像
         -repeat     repeat playing video(default false)，如果是圖像源是本地視頻，列舉此項將重復播放
         -v          /path/to/your/video_file or rtsp/rtmp stream 圖像源，可以是本地視頻，也可以是rtsp/rtmp視頻流
         -conf       confidence threshold between 0-1(default 0.25)，置信度閾值
         -nms        NMS threshold between 0-1(default 0.45) NMS閾值
         -size       input size of images, wrong size will cause error(default 640, 416 if tiny-model or nano-model)
         -ip         rtmp server ip(default 127.0.0.1)
         -port       rtmp server port(default 1935)
         -post-port  request server port(default 80)
         -fps        stream rate(default 30)
         -b          bit rate(default 4000000)
         -name       rtmp name(default live/test)  example: rtmp://ip:port/live/test
         -post-name  post json result name(default detect_result) example: http://ip:postport/post-name?data
         -clsfile    class file name(default classes.txt), 類別文件，見文件夾classes中的兩個文件

# for more details
./detect -h
```
### 如果覺得每次在命令行中輸入這麼多參數太麻煩，可以運行run.py文件代替detect,只需要在run.py文件中將相應的參數進行修改即可。
