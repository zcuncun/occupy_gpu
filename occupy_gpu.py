#! /usr/bin/python
# -*- coding: utf-8 -*-
# Create by zcuncun @ 2021/03/18 11:08:26
"""
gpu_train.py
"""

import argparse, logging
import torch
import time


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--device",
        type=str,
        required=True,
        help="device",
    )

    parser.add_argument(
        "--time",
        type=int,
        required=True,
        help="运行时间",
    )

    parser.add_argument(
        "--size",
        default=1,
        type=int,
        help="显存占用大小",
    )

    parser.add_argument(
        "--usage",
        default=1,
        type=float,
        help="使用率",
    )

    args = parser.parse_args()

    train_device = "cuda:{}".format(args.device)
    start_time = time.time()
    sleep_time = 0
    x = torch.rand([64, 3, 512, 512], device=train_device)
    y = torch.rand([args.size*128, 3, 512, 512], device=train_device)
    while True:
        time.sleep(0.01)
        for _ in range(int(10 * args.usage)):
            torch.sin(x)
        if args.time > 0 and time.time() - start_time > args.time:
            break
        

        
        

if __name__ == "__main__":
    main()
