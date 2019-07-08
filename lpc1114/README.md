# lpc1114について
## lpc1114の書き込みについて
### lpc21ispのダウンロード
```
wget https://sourceforge.net/projects/lpc21isp/files/latest/download -O lpc21isp_197.tar.gz
```

### lpc21ispのビルド
```
make -f Makefile clean all
```
+  -f が無い場合、 make は makefile として、 GNUmakefile, makefile, Makefile をこの順に参照する
+ clean all を実行することでビルド結果の削除後にビルドの実行を行う = ビルドのやり直し  
    ⇒ 初回のビルドであれば  ```make``` のみでOK 

### binファイルの取得
Mbed OSにてnxp1114FN28ボードを選択し,コンパイル

### lpc21ispの使用方法
```
./lpc21isp -control -bin  hoge.bin /dev/ttyUSB0 115200 1200
```
+ `-control` : RTSやDTRを使用
+ `-bin` : hexファイルではなくbinファイルを使用
+ `hoge.bin` : ここには上記のMbedOSにて取得した.binファイルのディレクトリを指定 
+ `/dev/ttyUSB0` : 自分のlpc1114が認識しているポートを指定
+ `115200` : 通信速度 基本的に115200でOK
+ `1200` : kHz単位で12MHzを指定 クロックと合わせる lpc1114なら12MHzでOK

## Uartの通信について
+ RTSやDTRをFalse=HIGHにする ⇒ ブートモード(書き込みモードに入らないようにする)
+ プログラムはサンプルプログラムを参考に

## サンプルプログラムについて
内容は単純なエコーバック
+ `lpc_serial.py` : pcからの指令をmbedに送信し返信を受信する
+ `lpc_echo_back.cpp` : pcから受信した内容をpcへ送信する MbedOSのmain.cppにコピペして使用

