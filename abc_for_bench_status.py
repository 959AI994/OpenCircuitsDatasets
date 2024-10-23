import subprocess


def run_abc(file_path):
    """
    使用 ABC 工具处理 BENCH 文件并打印统计信息
    """
    abc_command = f"./abc/abc -c 'read {'DataSets/I99T/i99t/b01/b01.bench'}; print_stats; quit;'"

    try:
        # 运行命令并捕获输出
        output = subprocess.check_output(abc_command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"错误: {e.output.decode()}")


if __name__ == "__main__":
    # 指定 BENCH 文件路径
    bench_file_path = "b01.bench"  # 实际的文件路径
    run_abc(bench_file_path)


