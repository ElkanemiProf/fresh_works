import sys, pygame as pg

# pg.init()
# screen_size = 750, 750
# screen = pg.display.set_mode(screen_size)
# font = pg.font.SysFont(None, 80)

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return  False





def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("--------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" |", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


print_board(board)
solve(board)
print("-------------------------------------------")
print_board(board)


#
# def draw_background():
#     screen.fill((pg.Color("white")))
#     pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
#     i = 1
#     while (i * 80) < 720:
#         line_width = 5 if i % 3 > 0 else 10
#         pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 80) + 15, 15), pg.Vector2((i * 80) + 15, 735),
#                      line_width)
#         pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 80) + 15), pg.Vector2(735, (i * 80) + 15, ),
#                      line_width)
#
#         i += 1
#
#
# def draw_numbers():
#     row = 0
#     offset = 35
#     while row < 9:
#         col = 0
#         while col < 9:
#             output = number_grid[row][col]
#             # print(str(output))
#             n_text = font.render(str(output), True, pg.Color("black"))
#             screen.blit(n_text, pg.Vector2((col * 80) + offset +3, (row * 80) + offset - 2))
#             col += 1
#
#         row += 1
#
#
# def game_loop():
#     for event in pg.event.get():
#         if event.type == pg.QUIT: sys.exit()
#
#     draw_background()
#     draw_numbers()
#     pg.display.flip()
#
#
# while True:
#     game_loop()
