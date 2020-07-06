from PIL import ImageDraw


class DonkeyWagonImageDraw(ImageDraw.ImageDraw):
    def wagon(self, xy, fill):
        # furgon
        self.rectangle(((xy[0], xy[1]), (xy[0] + xy[2], xy[1] + xy[3])), fill[0])
        # window
        win_side = xy[3] - xy[3] // 10
        self.rectangle(((xy[0] + xy[3] // 10, xy[1] + xy[3] // 10), (xy[0] + win_side, xy[1] + win_side)), fill[1])
        # left wheel
        col_left_x = xy[2] // 4 - xy[2] // 10
        self.ellipse((
            (xy[0] + col_left_x, xy[1] + xy[3]),
            (xy[0] + col_left_x + xy[2] // 5, xy[1] + xy[3] + xy[2] // 5)),
            fill[2])
        # right wheel
        col_right_x = xy[0] + xy[2] - col_left_x - xy[2] // 5
        self.ellipse((
            (col_right_x, xy[1] + xy[3]),
            (col_right_x + xy[2] // 5, xy[1] + xy[3] + xy[2] // 5)),
            fill[2])
