# find_last_fork

## 背景

有个各类验证码的库，库的主人已经将库删掉了，想要 fork，只能从该库的 fork 版本 fork。所以需要对众多 fork 库进行排序比较，可是 github 并没有直接列出 fork 库的 fork 时间线，所以手动写一个吧。

![image-20191122182725865](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/2019-11-22-102726.png)



## 使用

1. 克隆仓库

    ```python
    git clone https://github.com/Annihilater/find_last_fork
    ```

2. 安装依赖

    ```python
    pip install -r requirements.txt
    ```

3. 运行 main.py 文件

    ```python
    python main.py
    ```

4. 运行截图

    ![image-20191122182545868](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/2019-11-22-102546.png)

    