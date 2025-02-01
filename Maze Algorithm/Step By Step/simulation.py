# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from IPython.display import HTML
# # Đọc ma trận từ file CSV hoặc Excel
# df = pd.read_excel("maze_matrix.xlsx", header=0)  # Nếu là file Excel, dùng: pd.read_excel("matrix.xlsx", header=None)

# # Chuyển dataframe thành numpy array
# matrix = df.to_numpy()
# matrix_1 = df.to_numpy()
# # Lấy kích thước ma trận
# m, n = matrix.shape

# # # Kiểm tra phần tử bằng 1 ở border
# # border_indices = []
# # for i in range(m):
# #     for j in range(n):
# #         if matrix[i, j] == 1 and (i == 0 or i == m-1 or j == 0 or j == n-1):
# #             border_indices.append((i, j))

# # # In kết quả
# # print("Index của phần tử 1 ở border:", border_indices)

# # Khởi tạo hình ảnh
# fig, ax = plt.subplots()
# cmap = plt.get_cmap("gray", 3)  # Chỉ có 3 mức màu: 0, 1, 2

# # Hàm cập nhật vị trí của phần tử bằng 2
# def update(frame):
#     global matrix
#     global matrix_1
#     matrix = matrix_1.copy()
#     #matrix[matrix == 2] = 0  # Xóa vị trí cũ của số 2
#     x, y = np.random.randint(0, m), np.random.randint(0, n)  # Chọn vị trí ngẫu nhiên
#     matrix[x, y] = 2  # Đặt giá trị 2 vào vị trí mới
#     ax.clear()
#     ax.imshow(matrix, cmap=cmap, interpolation='nearest')
#     ax.set_title("Live Binary Matrix Animation")
#     ax.set_xticks([])
#     ax.set_yticks([])
#     ax.set_frame_on(False)
#       # Kiểm tra điều kiện dừng
#     # if (x, y) == (3, 3):  # Ví dụ: Dừng khi phần tử 2 ở góc dưới cùng bên phải
#     #     ani.event_source.stop()
#     #     print(f"Animation dừng lại tại tọa độ ({x}, {y})")


# # Tạo animation
# ani = animation.FuncAnimation(fig, update, frames=200, interval=100)
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Đọc ma trận từ file CSV hoặc Excel
df = pd.read_excel("maze_matrix.xlsx", header=0)  # Nếu là file Excel, dùng: pd.read_excel("matrix.xlsx", header=None)

# Chuyển dataframe thành numpy array
matrix = df.to_numpy()
matrix_1 = df.to_numpy()
# Lấy kích thước ma trận
m, n = matrix.shape

# Khởi tạo hình ảnh
fig, ax = plt.subplots()
cmap = plt.get_cmap("gray", 3)  # Chỉ có 3 mức màu: 0, 1, 2

# Số lần cập nhật tối đa
max_updates = 50
update_count = 0

while update_count < max_updates:

    matrix = matrix_1.copy()
    # Chọn vị trí ngẫu nhiên mới
    x, y = np.random.randint(0, m), np.random.randint(0, n)  
    matrix[x, y] = 2  
    
    # Cập nhật plot
    ax.clear()
    ax.imshow(matrix, cmap=cmap, interpolation='nearest')
    ax.set_title("Live Binary Matrix Animation")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    plt.pause(0.5)  # Dừng 0.5s trước khi tiếp tục vòng lặp
    update_count += 1

plt.show()
