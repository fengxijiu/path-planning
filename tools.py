import numpy as np
import open3d as o3d

def read_obj_with_numpy(file_path):
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):  # 顶点
                vertices.append(list(map(float, line.strip().split()[1:4])))
            elif line.startswith('f '):  # 面
                face = [int(item.split('/')[0]) - 1 for item in line.strip().split()[1:]]
                faces.append(face)

    return np.array(vertices), np.array(faces)

def visualize_clouds(clouds):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(clouds)
    o3d.visualization.draw_geometries([pcd])