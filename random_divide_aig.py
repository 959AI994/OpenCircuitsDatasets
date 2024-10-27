import subprocess
import os

def split_aig_with_abc(input_file, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 构建 ABC 命令
    abc_command = f"./abc/abc -c 'read {input_file}; decomp -f 0.5; write_aig {output_dir}/b01_part1.aig; write_aig {output_dir}/b01_part2.aig; write_aig {output_dir}/b01_part3.aig; quit;'"

    try:
        # 运行命令并捕获输出
        output = subprocess.check_output(abc_command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"错误: {e.output.decode()}")

if __name__ == "__main__":
    # 指定 AIG 文件路径和输出目录
    input_file = "DataSets/AigGraph/b01.aig"
    output_dir = "DataSets/DividedAig"
    split_aig_with_abc(input_file, output_dir)
