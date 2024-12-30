import argparse

import tools

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--obj_file', type=str, default=r'示例及任务部件模型/任务3-前盖模型.obj')
    args.add_argument('--output_file', type=str, default='./output/example.png')
    args = args.parse_args()
    vertices, faces = tools.read_obj_with_numpy(args.obj_file)
    tools.visualize_clouds(vertices)

