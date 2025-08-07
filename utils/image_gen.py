from PIL import Image, ImageDraw, ImageFont
import textwrap

def make_meme(
    img_path,
    text,
    out_path,
    font_path="fonts/impact.ttf",
    img_size=(600, 400),
    wrap_width=30
):
    # 1. Загружаем и масштабируем картинку
    img = Image.open(img_path).convert("RGB")
    img = img.resize(img_size)
    draw = ImageDraw.Draw(img)

    # 2. Готовим шрифт
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    # 3. Перенос текста (по символам)
    lines = textwrap.wrap(text, width=wrap_width)
    # Или можешь по словам, если хочется красивее

    # 4. Считаем высоту текста
    text_height = sum(draw.textbbox((0,0), line, font=font)[3] for line in lines) + 10 * (len(lines)-1)
    banner_height = text_height + 30  # с запасом

    # 5. Координаты баннера (внизу картинки)
    img_w, img_h = img.size
    banner_y0 = img_h - banner_height
    banner_y1 = img_h

    # 6. Рисуем черный полупрозрачный прямоугольник
    banner = Image.new("RGBA", (img_w, banner_height), (0,0,0,180))
    img.paste(banner, (0, banner_y0), banner)

    # 7. Рисуем текст по центру баннера
    y = banner_y0 + 15  # небольшой верхний отступ
    for line in lines:
        w = draw.textbbox((0,0), line, font=font)[2]
        x = (img_w - w) // 2
        # Обводка для контраста
        outline_range = 2
        for ox in range(-outline_range, outline_range+1):
            for oy in range(-outline_range, outline_range+1):
                draw.text((x+ox, y+oy), line, font=font, fill='black')
        draw.text((x, y), line, font=font, fill='white')
        y += draw.textbbox((0,0), line, font=font)[3] + 10  # шаг + отступ между строками

    # 8. Сохраняем
    img.save(out_path)
    return out_path
