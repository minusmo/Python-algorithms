def solution(brown, yellow):
    width_and_height = []
    width_and_height = get_width_and_height(brown, yellow)
    return width_and_height


def get_width_and_height(brown, yellow):
    width_and_height = []
    for height in range(1, yellow+1):
        for width in range(1, yellow//height+1):
            if height * width == yellow:
                brown_cells = get_brown_cells(height, width)
                if brown_cells == brown:
                    width_and_height = [width+2, height+2]
                    return width_and_height
    return width_and_height

def get_brown_cells(yellow_height, yellow_width):
    brown_cells = (yellow_height+2) * (yellow_width+2) - yellow_height * yellow_width
    return brown_cells