# install gflags  
因為 db_bench 執行需要 gflags  
```
git clone https://github.com/gflags/gflags.git
cd gflags
```
安裝cmake  
```
sudo apt  install cmake
```
使用 cmake 配置 gflags 的安裝，最後安裝到 lib/  
```
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local
make 
```
完成編譯後，執行以下指令將 gflags 安裝到指定的目錄：
```
sudo make install
```
檢查安裝是否在正確的路徑中：
‵‵‵
ls /usr/local/include/gflags/gflags.h
ls /usr/local/lib/libgflags.a
‵‵‵
將這些路徑加入編譯與執行環境，讓 db_bench 能夠找到 gflags：
```
export CPATH=/usr/local/include:$CPATH
export LIBRARY_PATH=/usr/local/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```


# db_bench 製作　　
查看 INSTAll.md  
```
make clean
make db_bench
```