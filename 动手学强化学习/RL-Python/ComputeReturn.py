import numpy as np

#
np.random.seed(0)

# 定义状态转移函数,S6转移到S6的概率为1，每一行的概率总和为1
P = [
    [0.9, 0.1, 0, 0, 0, 0],
    [0.5, 0, 0.5, 0, 0, 0],
    [0, 0, 0, 0.6, 0, 0.4],
    [0, 0, 0, 0, 0.3, 0.7],
    [0, 0.2, 0.3, 0.5, 0, 0],
    [0, 0, 0, 0, 0, 1]
]
P = np.array(P)

# 定义进入到每一种状态获得的奖励
returns = [-1, -2, -2, 10, 1, 0]
#定义折扣因子
gamma = 0.5


# 给定一个固定的轨迹，计算得到的奖励总和
# Gt = Rt + γRt+1 + ......
def compute_return(start_index, chain, gamma):
    sum_return = 0  # 初始总回报
    for i in range(start_index, len(chain)):
        sum_return = sum_return + gamma ** i * returns[chain[i] - 1]
    return sum_return


# 计算一个序列 S1——>S2——>S3——>S6
chain = [1, 2, 3, 6]
start_index = 0
sum_return = compute_return(start_index, chain, gamma)
print(sum_return)
