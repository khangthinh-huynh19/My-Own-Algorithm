import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# Read the Excel file
df = pd.read_excel('maze_matrix.xlsx', header = 0)

# Assuming the matrix data is in column 'Matrix'
numpy_matrix = df.to_numpy()
numpy_matrix_1 = df.to_numpy()

# get the size of matrix
m, n = numpy_matrix.shape

# start and end points
# this is just an example. You should input the own start and end points
start_point = [6,0]
end_point = [8,10]

# previous_points to get the passed points
previous_points = []

# recorded_points to get all the passed points
#recorded_points = []

# check 4 possible point to move
def check_possible_points(current_x, current_y):
  # list 4 possible points
  possible_points = [[current_x-1, current_y], [current_x+1, current_y], [current_x, current_y-1], [current_x, current_y+1]]
  next_points =[]

  # Check possible points
  for point in possible_points:
    if point[0] > 0 or point[1] > 0:
      if numpy_matrix[point[0], point[1]] == 1 and [point[0], point[1]] not in previous_points:
        next_points.append(point)
  #print("Next points list: ", next_points)
  if len(next_points) == 0:
    return previous_points[-1]
  else:
    next_point = random.choice(next_points)
    return next_point


# plotting function
def plotting(matrix, curr_point):
  cmap = plt.get_cmap("gray", 3)
  matrix = numpy_matrix_1.copy()
  matrix[curr_point[0], curr_point[1]] = 2
  ax.clear()
  ax.imshow(matrix, cmap=cmap, interpolation='nearest')
  ax.set_title("Live Binary Matrix Animation")
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_frame_on(False)
  plt.pause(0.5)
  
  
# Create image
fig, ax = plt.subplots()
cmap = plt.get_cmap("gray", 3)  # Chỉ có 3 mức màu: 0, 1, 2


current_point = start_point
while current_point != end_point:
  #recorded_points.append(current_point)
  next_point = check_possible_points(current_point[0], current_point[1])
  previous_points.clear()
  if current_point not in previous_points:
    previous_points.append(current_point)
  
  current_point = next_point
  #print(current_point)
  
  # Live Plotting
  # numpy_matrix = numpy_matrix_1.copy()
  # numpy_matrix[current_point[0], current_point[1]] = 2
  # ax.clear()
  # ax.imshow(numpy_matrix, cmap=cmap, interpolation='nearest')
  # ax.set_title("Live Binary Matrix Animation")
  # ax.set_xticks([])
  # ax.set_yticks([])
  # ax.set_frame_on(False)
  # plt.pause(0.5)  # Dừng 0.5s trước khi tiếp tục vòng lặp
  plotting(numpy_matrix, current_point)



plt.show()
# for i in recorded_points:
#   print(f"Row {i[0]}, Column {i[1]}")