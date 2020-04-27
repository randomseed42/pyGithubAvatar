import numpy as np
import matplotlib.pyplot as plt


class NumAvatar(object):
    def __init__(self, 
            top_border=35,
            left_border=35,
            right_border=35,
            bottom_border=35,
            line_width=50,
            line_height=70,
            bg_rgba=[240, 240, 240, 255],
            fg_rgba=[153, 136, 225, 255],
        ):
        self.top_border = top_border
        self.left_border = left_border
        self.right_border = right_border
        self.bottom_border = bottom_border
        self.line_width = line_width
        self.line_height = line_height
        self.bg_rgba = bg_rgba
        self.fg_rgba = fg_rgba

        self.num_dict = {
            0: np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 3],
                [2, 1, 1, 3],
                [0, 4, 3, 1],
            ]),
            1: np.array([
                [2, 0, 1, 5],
            ]),
            2: np.array([
                [0, 0, 3, 1],
                [2, 1, 1, 1],
                [0, 2, 3, 1],
                [0, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            3: np.array([
                [0, 0, 3, 1],
                [2, 1, 1, 1],
                [0, 2, 3, 1],
                [2, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            4: np.array([
                [0, 0, 1, 3],
                [1, 2, 1, 1],
                [2, 0, 1, 5],
            ]),
            5: np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 1],
                [0, 2, 3, 1],
                [2, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            6: np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 3],
                [0, 2, 3, 1],
                [2, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            7: np.array([
                [0, 0, 2, 1],
                [2, 0, 1, 5],
            ]),
            8: np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 3],
                [2, 1, 1, 3],
                [1, 2, 1, 1],
                [0, 4, 3, 1],
            ]),
            9: np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 2],
                [2, 1, 1, 3],
                [1, 2, 1, 1],
                [0, 4, 3, 1],
            ]),
        }
    
    def avatar(self, num, path=None):
        self.img_width = self.line_width*7 + self.left_border + self.right_border
        self.img_height = self.line_height*5 + self.top_border + self.bottom_border

        self.img = np.zeros((self.img_height, self.img_width, 4), dtype='uint8')
        self.img[:, :] = self.bg_rgba

        digits = {1: num % 10, 0: num // 10}

        for digit in digits:
            left_padding = digit*4*self.line_width + self.left_border
            top_padding = self.top_border
            for block in self.num_dict[digits[digit]]:
                left, right, top, bottom = (
                    block[0]*self.line_width + left_padding,
                    (block[0]+block[2])*self.line_width + left_padding,
                    block[1]*self.line_height + top_padding,
                    (block[1]+block[3])*self.line_height + top_padding,
                )
                self.img[top:bottom, left:right] = self.fg_rgba
                
        plt.axis('off')
        plt.imshow(self.img)
        if not path:
            plt.show()
        elif isinstance(path, str):
            plt.imsave(path, self.img, dpi=300)
        return


if __name__ == '__main__':
    gna = NumAvatar()
    gna.avatar(42, path='./img/42.png')
