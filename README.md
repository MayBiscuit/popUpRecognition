# 功能:识别弹窗
1. 输入：
![img.png](img.png)
2. 输出：
![img_1.png](img_1.png)

# 训练方式
1. 将标注数据放置于data_pop_ups文件夹内
2. 修改data_pop_ups文件夹里pop_uos.yaml的路径
2. 运行 python train.py --batch-size 2 --epochs 200 --data data_pop_ups/pop_ups.yaml --weights weight/yolov5m.pt

# 使用方式
1. 将待识别图片保存在 data\images_pop_ups 文件夹下
2. 运行 python .\detect.py --source .\data\images_pop_ups --weights .\runs\train\exp13\weights\best.pt
3. 结果保存在 runs\detect下的exp文件夹内

# 其他
1. 权重文件在.\runs\train\exp13\weights\best.pt下
2. 标注数据在.\data_pop_ups下：
![img_2.png](img_2.png)