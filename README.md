# occupy_gpu
For better usage of GPU

nohup python occupy_gpu.py --device 2 --time 0 --gpu_mem 2 --cpu_mem 4 --usage 5 >/dev/null 2>&1 & echo $! >> oc_gpu.pid
