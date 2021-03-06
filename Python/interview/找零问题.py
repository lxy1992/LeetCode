# -*- coding: UTF-8 -*-
def coinChange(values, money, coinsUsed):
#values T[1:n]数组
#valuesCounts 钱币对应的种类数
#money 找出来的总钱数
#coinsUsed 对应于 前钱币总数i所使 的硬币数
    for cents in range(1, money+1):
        minCoins = cents
        #从第 个开始到money的所有情况初始
        for value in values:
            if value <= cents:
                temp = coinsUsed[cents - value] + 1
                if temp < minCoins:
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print(' 值为:{0} 的最 硬币数 为:{1} '.format(cents, coinsUsed[cents]))

if __name__ == '__main__':
    values = [25, 21, 10, 5, 1]
    money = 63
    coinsUsed = {i: 0 for i in range(money + 1)}
    coinChange(values, money, coinsUsed)