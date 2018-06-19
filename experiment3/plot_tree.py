from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from pylab import *


DECISION_NODE = dict(boxstyle="sawtooth", fc="0.8")
LEAF_NODE = dict(boxstyle="round4", fc="0.8")
ARROW_ARGS = dict(arrowstyle="<-")


def get_num_leafs(tree):
    num_leafs = 0
    first_branch = next(iter(tree))
    second_dict = tree[first_branch]
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == 'dict':
            num_leafs += get_num_leafs(second_dict[key])
        else:
            num_leafs += 1
    return num_leafs


def get_tree_depth(tree):
    max_depth = 0
    first_branch = next(iter(tree))
    second_dict = tree[first_branch]
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == 'dict':
            this_depth = 1 + get_tree_depth(second_dict[key])
        else:
            this_depth = 1
        if this_depth > max_depth:
            max_depth = this_depth
    return max_depth


def plot_mid_text(now_pt, father_pt, txt):
    x_mid = (father_pt[0]-now_pt[0]) / 2.0 + now_pt[0]
    y_mid = (father_pt[1]-now_pt[1]) / 2.0 + now_pt[1]
    create_plot.ax1.text(x_mid, y_mid, txt)


def plot_tree(tree, father_pt, node_txt):
    num_leafs = get_num_leafs(tree)
    depth = get_tree_depth(tree)
    root = list(tree.keys())[0]
    now_pt = (plot_tree.xoff + (1.0 + float(num_leafs))/2.0/plot_tree.totalW, plot_tree.yoff)
    plot_mid_text(now_pt, father_pt, node_txt)
    plot_node(root, now_pt, father_pt, DECISION_NODE)
    first_root = tree[root]
    plot_tree.yoff = plot_tree.yoff - 1.0/plot_tree.totalD
    for key in first_root.keys():
        if type(first_root[key]) == type({}):
            plot_tree(first_root[key], now_pt, str(key))
        else:
            plot_tree.xoff = plot_tree.xoff + 1.0/plot_tree.totalW
            plot_node(first_root[key], (plot_tree.xoff, plot_tree.yoff), now_pt, LEAF_NODE)
            plot_mid_text((plot_tree.xoff, plot_tree.yoff), now_pt, str(key))
    plot_tree.yoff = plot_tree.yoff + 1.0/plot_tree.totalD


def plot_node(node_txt, center_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_txt, xy=parent_pt,  xycoords='axes fraction',
                             xytext=center_pt, textcoords='axes fraction',
                             va="center", ha="center", bbox=node_type, arrowprops=ARROW_ARGS)


def create_plot(tree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False,**axprops)
    plot_tree.totalW = float(get_num_leafs(tree))
    plot_tree.totalD = float(get_tree_depth(tree))
    plot_tree.xoff = -1.0 / 2.0 / plot_tree.totalW    # 1分成2倍叶子数那么多份
    plot_tree.yoff = 1.0
    plot_tree(tree, (0.5, 1.0), '')
    plt.show()


if __name__ == "__main__":
    tree = tree = {'Petal Length': {'< 3.00': 'Iris-setosa', '>=3.00': {'Petal Width': {'< 1.80': {'Sepal Length': {'< 7.20': {'Sepal Width': {'< 2.90': 'Iris-versicolor', '>=2.90': 'Iris-versicolor'}}, '>=7.20': 'Iris-virginica'}}, '>=1.80': {'Sepal Length': {'< 6.00': {'Sepal Width': {'< 3.20': 'Iris-virginica', '>=3.20': 'Iris-versicolor'}}, '>=6.00': 'Iris-virginica'}}}}}}

    create_plot(tree)
