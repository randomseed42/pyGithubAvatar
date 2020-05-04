import numpy as np
import matplotlib.pyplot as plt


class CharAvatar(object):
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

        self.char_dict = {
            # in the form of [left, top, width, height]
            '0': np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 3],
                [2, 1, 1, 3],
                [0, 4, 3, 1],
            ]),
            '1': np.array([
                [2, 0, 1, 5],
            ]),
            '2': np.array([
                [0, 0, 3, 1],
                [2, 1, 1, 1],
                [0, 2, 3, 1],
                [0, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            '3': np.array([
                [0, 0, 3, 1],
                [2, 1, 1, 1],
                [0, 2, 3, 1],
                [2, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            '4': np.array([
                [0, 0, 1, 3],
                [1, 2, 1, 1],
                [2, 0, 1, 5],
            ]),
            '5': np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 1],
                [0, 2, 3, 1],
                [2, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            '6': np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 3],
                [0, 2, 3, 1],
                [2, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
            '7': np.array([
                [0, 0, 2, 1],
                [2, 0, 1, 5],
            ]),
            '8': np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 3],
                [2, 1, 1, 3],
                [1, 2, 1, 1],
                [0, 4, 3, 1],
            ]),
            '9': np.array([
                [0, 0, 3, 1],
                [0, 1, 1, 2],
                [2, 1, 1, 3],
                [1, 2, 1, 1],
                [0, 4, 3, 1],
            ]),
            'A': np.array([
                [1, 0, 1, 1],
                [0, 1, 1, 4],
                [2, 1, 1, 4],
                [1, 2, 1, 1],
            ]),
            'B': np.array([
                [0, 0, 2, 1],
                [0, 1, 1, 3],
                [0, 4, 2, 1],
                [1, 2, 1, 1],
                [2, 1, 1, 1],
                [2, 3, 1, 1],
            ]),
            'C': np.array([
                [0, 1, 1, 3],
                [1, 0, 1, 1],
                [1, 4, 1, 1],
                [2, 1, 1, 1],
                [2, 3, 1, 1],
            ]),
            'D': np.array([
                [0, 0, 1, 5],
                [1, 0, 1, 1],
                [1, 4, 1, 1],
                [2, 1, 1, 3],
            ]),
            'E': np.array([
                [0, 0, 1, 5],
                [1, 0, 2, 1],
                [1, 2, 1, 1],
                [1, 4, 2, 1],
            ]),
            'F': np.array([
                [0, 0, 1, 5],
                [1, 0, 2, 1],
                [1, 2, 1, 1],
            ]),
            'G': np.array([
                [1, 0, 2, 1],
                [0, 1, 1, 3],
                [1, 4, 2, 1],
                [2, 3, 1, 1],
            ]),
            'H': np.array([
                [0, 0, 1, 5],
                [2, 0, 1, 5],
                [1, 2, 1, 1],
            ]),
            'I': np.array([
                [0, 0, 3, 1],
                [1, 1, 1, 3],
                [0, 4, 3, 1],
            ]),
            'J': np.array([
                [2, 0, 1, 4],
                [0, 3, 1, 1],
                [1, 4, 1, 1],
            ]),
            'K': np.array([
                [0, 0, 1, 5],
                [1, 1, 1, 2],
                [2, 0, 1, 1],
                [2, 3, 1, 2],
            ]),
            'L': np.array([
                [0, 0, 1, 5],
                [1, 4, 2, 1],
            ]),
            'M': np.array([
                [0, 0, 1, 5],
                [1, 1, 1, 2],
                [2, 0, 1, 5],
            ]),
            'N': np.array([
                [0, 0, 1, 5],
                [1, 0, 1, 1],
                [2, 1, 1, 4],
            ]),
            'O': np.array([
                [1, 0, 1, 1],
                [0, 1, 1, 3],
                [2, 1, 1, 3],
                [1, 4, 1, 1],
            ]),
            'P': np.array([
                [0, 0, 1, 5],
                [1, 0, 1, 1],
                [1, 2, 1, 1],
                [2, 1, 1, 1],
            ]),
            'Q': np.array([
                [1, 0, 1, 1],
                [0, 1, 1, 1],
                [1, 2, 1, 1],
                [2, 0, 1, 5],
            ]),
            'R': np.array([
                [0, 0, 1, 5],
                [1, 0, 1, 1],
                [1, 2, 1, 1],
                [2, 1, 1, 1],
                [2, 3, 1, 2],
            ]),
            'S': np.array([
                [1, 0, 2, 1],
                [0, 1, 1, 1],
                [1, 2, 1, 1],
                [2, 3, 1, 1],
                [0, 4, 2, 1],
            ]),
            'T': np.array([
                [0, 0, 3, 1],
                [1, 1, 1, 4],
            ]),
            'U': np.array([
                [0, 0, 1, 4],
                [2, 0, 1, 4],
                [1, 4, 1, 1],
            ]),
            'V': np.array([
                [0, 0, 1, 3],
                [2, 0, 1, 3],
                [1, 3, 1, 2],
            ]),
            'W': np.array([
                [0, 0, 1, 5],
                [1, 2, 1, 2],
                [2, 0, 1, 5],
            ]),
            'X': np.array([
                [0, 0, 1, 2],
                [2, 0, 1, 2],
                [1, 2, 1, 1],
                [0, 3, 1, 2],
                [2, 3, 1, 2],
            ]),
            'Y': np.array([
                [0, 0, 1, 2],
                [2, 0, 1, 2],
                [1, 2, 1, 3],
            ]),
            'Z': np.array([
                [0, 0, 3, 1],
                [2, 1, 1, 1],
                [1, 2, 1, 1],
                [0, 3, 1, 1],
                [0, 4, 3, 1],
            ]),
        }


    def avatar(self, twoChars, path=None):
        self.img_width = self.line_width*7 + self.left_border + self.right_border
        self.img_height = self.line_height*5 + self.top_border + self.bottom_border

        self.img = np.zeros((self.img_height, self.img_width, 4), dtype='uint8')
        self.img[:, :] = self.bg_rgba

        chars = list(str(twoChars))

        for pos, char in enumerate(chars):
            left_padding = pos*4*self.line_width + self.left_border
            top_padding = self.top_border
            for block in self.char_dict[char]:
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
    gca = CharAvatar()
    gca.avatar(42)

    for i in range(int(10/2)):
        gca.avatar(f'{i*2}{i*2+1}')

    for i in range(int(26/2)):
        gca.avatar(chr(i*2+65)+chr(i*2+1+65))
