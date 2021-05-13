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
    gpu_run = torch.rand([64, 3, 512, 512], device=train_device)
    gpu_mem = torch.rand([args.size*128 * 512 * 512], device=train_device)
    cpu_run = torch.rand([8, 3, 512, 512], device="cpu")
    cpu_mem = torch.rand([args.size*128 * 512 * 512], device="cpu")
    
    while True:
        t0 = time.time()
        a = 0
        while (time.time() - t0) < 0.003 * (2 / ( 1 + 2 * args.usage)):
            a = 1
        torch.sin(gpu_run)
        if args.time > 0 and time.time() - start_time > args.time:
            break


if __name__ == "__main__":
    main()
