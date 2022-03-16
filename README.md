# yolo_result_provider

主要给Nvidia Jetson系列嵌入式设备使用的，程序使用tensorrt推理模型，并将结果发送到服务器，接收demo见Server.py。
网络输入输出适配于yolox。

## 安装
```
mkdir build && cd build
cmake ..
make -j6
```

## 使用
```
./detect -e      [/path/to/your/engine/file]
         -v      [/path/to/your/video/file(or rtmp/rtsp stream address)]
         -ip     [your server ip]
         -port   [your server port]
         -name   [request name, see file Server.py]
         -conf   [confidence threshold]
         -nms    [NMS threshold]
         -size   [input image size (640 or 416, default 640)]
# for more details
./detect -h
```

