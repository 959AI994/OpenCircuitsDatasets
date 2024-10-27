import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def load_aig_to_graph(file_path):
    """
    读取 AIG 文件并转换为 NetworkX 图
    """
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # 跳过第一行
        parts = line.strip().split()
        if len(parts) > 2:  # 确保有 AND 门定义
            and_node = parts[0]
            fanins = parts[2:]  # 从第三个部分开始是输入
            for fanin in fanins:
                G.add_edge(fanin, and_node)

    return G


def graph_to_npz(graph, output_file):
    """
    将 NetworkX 图转换为 NPZ 文件
    """
    # 获取节点和边
    nodes = list(graph.nodes())
    edges = list(graph.edges())

    # 将节点和边转换为适合的 NumPy 数组
    node_indices = {node: idx for idx, node in enumerate(nodes)}
    edge_list = np.array([[node_indices[edge[0]], node_indices[edge[1]]] for edge in edges])

    # 保存为 NPZ 文件
    np.savez(output_file, nodes=np.array(nodes), edges=edge_list)


def visualize_graph(graph):
    """
    可视化 NetworkX 图
    """
    plt.figure(figsize=(12, 8))

    # 使用 spring 布局
    pos = nx.spring_layout(graph)

    # 绘制节点和边
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold',
            arrows=True)

    # 设置标题
    plt.title("AIG Graph Visualization", fontsize=15)
    plt.show()


# 使用示例
input_file = 'DataSets/AigGraph/b01.aig'
output_file = 'DataSets/DividedAig/b01_graph.npz'

# 读取 AIG 文件并转换为图
graph = load_aig_to_graph(input_file)
visualize_graph(graph)  # 可视化图
# 将图保存为 NPZ 文件
graph_to_npz(graph, output_file)
