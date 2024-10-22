def parse_bench(file_path):
    """
    解析 BENCH 文件，提取输入、输出和逻辑门信息
    """
    inputs = []
    outputs = []
    gates = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # 跳过空行和注释行
            if not line or line.startswith('#'):
                continue

            # 解析输入
            if line.startswith('INPUT'):
                input_var = line.split('(')[1].split(')')[0]
                inputs.append(input_var)

            # 解析输出
            elif line.startswith('OUTPUT'):
                output_var = line.split('(')[1].split(')')[0]
                outputs.append(output_var)

            # 解析逻辑门
            else:
                # 逻辑门的格式为 A = AND(B, C)
                gate_parts = line.split('=')
                if len(gate_parts) == 2:
                    gate_output = gate_parts[0].strip()
                    gate_func = gate_parts[1].strip()
                    gates.append((gate_output, gate_func))

    return inputs, outputs, gates

def display_circuit_info(inputs, outputs, gates):
    """
    输出电路的基本信息
    """
    print(f"电路中的输入变量: {', '.join(inputs)}")
    print(f"电路中的输出变量: {', '.join(outputs)}")
    print("\n电路中的逻辑门:")
    for gate_output, gate_func in gates:
        print(f"{gate_output} = {gate_func}")

if __name__ == "__main__":
    # 指定 BENCH 文件路径
    file_path = "DataSets/I99T/i99t/b01/b01.bench"  # 实际的文件路径
    inputs, outputs, gates = parse_bench(file_path)
    display_circuit_info(inputs, outputs, gates)
