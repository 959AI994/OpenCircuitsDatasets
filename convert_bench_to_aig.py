# import subprocess
# import os
#
# def convert_bench_to_aig(bench_file, aig_file):
#     """
#     将 BENCH 文件转换为 AIG 格式
#     """
#     abc_command = f"./abc/abc -c 'read {bench_file}; write_aiger {os.path.abspath(aig_file)}; quit;'"
#
#     try:
#         print(f"执行命令: {abc_command}")
#         output = subprocess.check_output(abc_command, shell=True, stderr=subprocess.STDOUT)
#         print(output.decode())
#         print(f"成功将 {bench_file} 转换为 {aig_file}.")
#     except subprocess.CalledProcessError as e:
#         print(f"错误: {e.output.decode()}")
#
# if __name__ == "__main__":
#     # 指定 BENCH 文件路径和输出的 AIG 文件路径
#     bench_file_path = "DataSets/I99T/i99t/b01/b01.bench"  # 实际的 BENCH 文件路径
#     aig_file_path = "/Users/wangjingxin/PycharmProjects/Learning-Circuits-Datasets/DataSets/AigGraph"  # 目标 AIG 文件路径，确保包括文件名
#
#     # 创建目标目录（如果不存在）
#     os.makedirs(os.path.dirname(aig_file_path), exist_ok=True)
#
#     # 转换 BENCH 文件为 AIG 图
#     convert_bench_to_aig(bench_file_path, aig_file_path)

import subprocess
import os

def convert_bench_to_aig(bench_file, aig_file):
    """
    将 BENCH 文件转换为 AIG 格式
    """
    # 构建 ABC 命令,这里需要现将bench电路转换为结构哈希AIG（使用strsh命令转aig）
    abc_command = f"./abc/abc -c 'read {bench_file}; strash;write_aiger {aig_file}; quit;'"
    print(f"执行命令: {abc_command}")

    try:
        output = subprocess.check_output(abc_command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())  # 输出命令的结果
        print(f"成功将 {bench_file} 转换为 {aig_file}.")
    except subprocess.CalledProcessError as e:
        print(f"错误: {e.output.decode()}")

if __name__ == "__main__":
    # 指定 BENCH 文件路径和输出的 AIG 文件路径
    bench_file_path = "DataSets/I99T/i99t/b01/b01.bench"  # 实际的 BENCH 文件路径
    aig_file_path = "DataSets/AigGraph/b01.aig"  # 目标 AIG 文件路径，确保包括文件名

    # 创建目标目录（如果不存在）
    os.makedirs(os.path.dirname(aig_file_path), exist_ok=True)

    # 转换 BENCH 文件为 AIG 图
    convert_bench_to_aig(bench_file_path, aig_file_path)
