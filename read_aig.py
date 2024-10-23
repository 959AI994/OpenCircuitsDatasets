import subprocess

def process_aig_with_abc(aig_file):
    # 构建 ABC 命令

    # abc_command = f"./abc/abc -c 'read {aig_file}; print_stats; quit;'"
    abc_command = f"./abc/abc -c 'read_aiger {aig_file}; print_stats; quit;'"

    # 执行命令
    process = subprocess.Popen(abc_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取输出
    stdout, stderr = process.communicate()

    # 打印结果
    print(stdout.decode())
    if stderr:
        print("Error:", stderr.decode())


# 指定 AIG 文件的路径
aig_file_path = "DataSets/AigGraph/b01.aig"
process_aig_with_abc(aig_file_path)


