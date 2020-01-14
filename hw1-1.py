import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

def eight_connect(img):


    # 함수 작성

    # bin img를 label img로 복사
    # label img의 경계는 0으로 설정
    height = img.shape[0]
    width = img.shape[1]
    # print("h:", height, "w: ", width)
    label_img = img
    # print("h:", label_img.shape[0], "w: ", label_img.shape[0])

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if np.all(img[i][j] != [0, 0, 0]):
                label_img[i][j][0] = 255

    # label_img[0][:] = 0
    # label_img[height - 1][:] = 0
    # label_img[:][0] = 0
    # label_img[:][width - 1] = 0

    # for i in range(1, height - 1):
    #     for j in range(1, width - 1):
    #         print(label_img[i][j], end="")
    #     print()


    color = [0, 75, 200]
    color_cnt = 0
    label = 1
    for i in range(1, height - 2):
        for j in range(1, width - 2):
            if np.all(label_img[i][j] == [255, 255, 255]):
                floodfill8(label_img, j, i, color)
                color = [random.randrange(1, 254), random.randrange(1, 254), random.randrange(1, 254)]
                label += 1


    # for i in range(1, height - 1):
    #     for j in range(1, width - 1):
    #         print("%02d" % label_img[i][j][0], end=" ")
    #     print()
    #print(label)

    return label_img


def floodfill8(label_img, j, i, color):
    queue = []
    queue.insert(0, [j, i])
    #print("color r ", color[0], "g: ", color[1], "b: ", color[2])
    while queue:
        x, y = queue.pop()
        if np.all(label_img[y][x] == [255, 255, 255]):
            left = right = x
            while np.all(label_img[y][left - 1] == [255, 255, 255]):
                left -= 1
            while np.all(label_img[y][right + 1] == [255, 255, 255]):
                right += 1
            for c in range(left, right + 1):
                # label_img[c][y][0] = color[0]
                # label_img[c][y][1] = color[1]
                # label_img[c][y][2] = color[2]
                label_img[y][c] = color
                if np.all(label_img[y - 1][c] == [255, 255, 255]) and (c == left or np.any(label_img[y - 1][c - 1] != [255, 255, 255])):
                    queue.insert(0, [c, y - 1])
                if np.all(label_img[y + 1][c] == [255, 255, 255]) and (c == left or np.any(label_img[y + 1][c - 1] != [255, 255, 255])):
                    queue.insert(0, [c, y + 1])

                if np.all(label_img[y - 1][c - 1] == [255, 255, 255]) and (c == left or np.any(label_img[y - 1][c - 1] != [255, 255, 255])):
                    queue.insert(0, [c - 1, y - 1])
                if np.all(label_img[y - 1][c + 1] == [255, 255, 255]) and (c == left or np.any(label_img[y - 1][c - 1] != [255, 255, 255])):
                    queue.insert(0, [c + 1, y - 1])
                if np.all(label_img[y + 1][c - 1] == [255, 255, 255]) and (c == left or np.any(label_img[y + 1][c - 1] != [255, 255, 255])):
                    queue.insert(0, [c - 1, y + 1])
                if np.all(label_img[y + 1][c + 1] == [255, 255, 255]) and (c == left or np.any(label_img[y + 1][c - 1] != [255, 255, 255])):
                    queue.insert(0, [c + 1, y + 1])


# def floodfill4(label_img, j, i, label):
#     queue = []
#     queue.insert(0, [j, i])
#     #print("color r ", color[0], "g: ", color[1], "b: ", color[2])
#     while queue:
#         x, y = queue.pop()
#         if np.all(label_img[y][x] == [255, 255, 255]):
#             left = right = x
#             while np.all(label_img[y][left - 1] == [255, 255, 255]):
#                 left -= 1
#             while np.all(label_img[y][right + 1] == [255, 255, 255]):
#                 right += 1
#             for c in range(left, right + 1):
#                 # label_img[c][y][0] = color[0]
#                 # label_img[c][y][1] = color[1]
#                 # label_img[c][y][2] = color[2]
#                 # label_img[y][c] = color
#                 label_img[y][c] = label
#                 if np.all(label_img[y - 1][c] == [255, 255, 255]) and (c == left or np.any(label_img[y - 1][c - 1] != [255, 255, 255])):
#                     queue.insert(0, [c, y - 1])
#                 if np.all(label_img[y + 1][c] == [255, 255, 255]) and (c == left or np.any(label_img[y + 1][c - 1] != [255, 255, 255])):
#                     queue.insert(0, [c, y + 1])


if __name__ == "__main__":
    img = cv2.imread('./sample.png')

    labeled_img = four_connect(img)

    # image 출력
    plt.imshow(labeled_img)
    plt.grid(None)
    plt.xticks([])
    plt.yticks([])
    plt.show()