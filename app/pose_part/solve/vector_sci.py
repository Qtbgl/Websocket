import numpy as np
from scipy.spatial.transform import Rotation


def degree180(v: np.ndarray):
    """
    例如(x,y,z)与(y,-x,0)垂直
    """
    vert = np.array([0, 0, 0])
    i = 0 if v[0] else 1 if v[1] else 2 if v[2] else -1
    if i == -1:
        raise Exception('向量为零向量，不支持求垂直向量')

    j = (i + 1) % 3  # 不同位
    vert[i] = v[j]
    vert[j] = -v[i]
    return vert


def from2vector(v1, v2):
    n_v1 = v1 / np.linalg.norm(v1)
    n_v2 = v2 / np.linalg.norm(v2)
    c = np.dot(n_v1, n_v2)
    if c < -0.9998:
        print('夹角接近180度')
        vec = degree180(v1)
        rot = np.pi
    else:
        vec = np.cross(v1, v2)
        rot = np.arccos(c)  # 弧度制，角度0~180度

    vec = vec / np.linalg.norm(vec)  # 标准化
    r = Rotation.from_rotvec(rot * vec)
    return r
