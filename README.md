# 里工 Quadrupedal project


#前期所有资料在网盘:  
https://pan.baidu.com/s/1lUSNyG8YdDMUPyh-FUg5kA 提取码: qb24

# 代码版本控制在GitHub上
https://github.com/fatgenius/LIgong_Quadrupedal.git 


 
#技术要求如下：

- 底盘部分：
   - A，能够四足完成爬楼梯，崎岖路面的能力；
   - B，能够摔倒后爬起来（无论左右）—-腰部电机 ？？？？？
   - C，能够前进和后退；
   - D，可以三只稳定（左或右前足失效情况下）
   - E，移动速度在2米/s即可 7.2km/h
   - F，无线充电（已经找到有合作伙伴）
   - G，电机拖动功能，类似解锁部分电机，可以拖着机器人移动。

- 导航部分： 
   -  A，16线激光，实现点云3D制图；
   -  B，双目镜头融合激光制图；
   -  C，可以自主执行任务（在已经建图的情况下）
   -  D，有避障能力（3维），如头部有物件，机器人会调整爬姿穿过；

- 深度学习部分：
  - 可以识别场景中物件，如人，设备，植物，建筑物，标志；

- 目前状态
  - 积累理论 40%
  - 用 gazebo进行运动仿真 10%

# 仿真部分（代码在 catkin_ws 里持续贡献中）
 - 每个腿 6DOF
 - 输入maxcon关节电机信息
 - 加入普通重力模型
 - 低俗度行动
 - solidworks to URDF use opensource:  https://github.com/ros/solidworks_urdf_exporter/releases
 - 里工机器人仿真 world ： https://github.com/fatgenius/LIgong_Quadrupedal/tree/master/catkin_ws/src/ligong_gazebo/worlds
 - 里工机器人仿真 BringUp和launch 文件： https://github.com/fatgenius/LIgong_Quadrupedal/tree/master/catkin_ws/src/ligong_gazebo/launch 
 - 里工机器人urdf模型 通过Solidworks至今导出 描述在： https://github.com/fatgenius/LIgong_Quadrupedal/tree/master/catkin_ws/src/ligong_description
 
# 图形
![](picture/simulation.jpg)
