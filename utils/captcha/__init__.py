
import random
import string
# Image：一个画布
# ImageDraw：一个画笔
# ImageFont：画笔的字体
from PIL import Image, ImageDraw, ImageFont

class Captcha(object):
    # 生成几位数的验证码
    number = 4
    # 验证码图片的宽度和高度
    size = (100, 30)
    # 验证码字体大小
    fontsize = 25
    # 加入干扰线的条数
    line_number = 2
    # 构建一个验证码源文本
    SOURCE = list(string.ascii_letters)
    for index in range(0, 10):
        SOURCE.append(str(index))

    # 用来绘制干扰线
    @classmethod
    def __gene_line(cls, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=cls.__gene_random_color(),width=2)

    # 随机生成的颜色点
    @classmethod
    def __gene_random_point(cls, draw, point_chance, width, height):
        chance = min(100, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100-chance:
                    draw.point((w, h), fill=cls.__gene_random_color())

    # 生成随机颜色值
    @classmethod
    def __gene_random_color(cls, start=0, end=255):
        random.seed()
        return (random.randint(start, end), random.randint(start, end), random.randint(start, end))

    # 获取随机字体
    @classmethod
    def __gene_random_font(cls):
        fonts = [
            'Arial.ttf',
            'Arial Bold Italic.ttf',
            'Batang.ttf',
            'Verdana Bold.ttf'
        ]
        return 'utils/captcha/'+random.choice(fonts)

    # 获取字符串
    @classmethod
    def gene_text(cls, number):
        return ''.join(random.sample(cls.SOURCE, number))

    # 生成验证码
    @classmethod
    def gene_graph_captcha(cls):
        # 验证码图片的宽和高
        width, height = cls.size
        # 创建图片
        image = Image.new('RGBA', (width, height), cls.__gene_random_color(0, 100))
        # 创建字体
        font = ImageFont.truetype(cls.__gene_random_font(), cls.fontsize)
        # 创建画笔
        draw = ImageDraw.Draw(image)
        # 生成字符串
        text = cls.gene_text(cls.number)
        print(text)
        # 获取字符串尺寸
        font_width, font_height = font.getsize(text)
        # 填充字符串
        draw.text(((width - font_width)/2, (height - font_height)/2), text, fill=cls.__gene_random_color(start=100, end=255), font=font)
        # 绘制干扰线
        for x in range(0, cls.line_number):
            cls.__gene_line(draw, width, height)
        # 绘制随机点
        cls.__gene_random_point(draw, 10, width, height)

        # with open('captcha.png', 'wb') as fi:
        #     image.save(fi)
        return (text, image)
