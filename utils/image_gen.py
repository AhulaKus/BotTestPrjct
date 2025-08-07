from PIL import Image, ImageDraw, ImageFont

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    while words:
        line = []
        while words:
            line.append(words.pop(0))
            test_line = ' '.join(line)
            w = draw.textbbox((0, 0), test_line, font=font)[2]
            if w > max_width:
                if len(line) == 1:
                    # Слово не помещается даже одно (длиннющее) — просто добавим
                    break
                words.insert(0, line.pop(-1))
                break
        lines.append(' '.join(line))
    return lines

def fit_text_block(draw, text, font_path, block_width, block_height, min_font=10, max_font=120):
    best_font = None
    best_lines = []
    # Самый большой подходящий шрифт
    for font_size in range(max_font, min_font-1, -1):
        font = ImageFont.truetype(font_path, font_size)
        lines = wrap_text(text, font, block_width, draw)
        # <-- вот здесь надо считать именно высоту с учётом всех межстрочных интервалов!
        line_heights = [draw.textbbox((0,0), line, font=font)[3] - draw.textbbox((0,0), line, font=font)[1] for line in lines]
        total_h = sum(line_heights)
        # Добавим небольшой запас: чуть-чуть отступа между строками!
        total_h += int(font_size * 0.2) * (len(lines) - 1)
        if total_h <= block_height:
            best_font = font
            best_lines = lines
            break
    # Если даже минимальный не помещается
    if not best_font:
        best_font = ImageFont.truetype(font_path, min_font)
        best_lines = wrap_text(text, best_font, block_width, draw)
    return best_font, best_lines

def draw_text_fill(draw, text, font_path, block_x, block_y, block_w, block_h):
    font, lines = fit_text_block(draw, text, font_path, block_w, block_h)
    # 1. Считаем высоту каждой строки + отступы
    line_heights = [draw.textbbox((0,0), line, font=font)[3] - draw.textbbox((0,0), line, font=font)[1] for line in lines]
    total_height = sum(line_heights) + int(font.size * 0.2) * (len(lines)-1)
    # 2. Начальный y: от верха баннера + центрируем по высоте
    y = block_y + (block_h - total_height) // 2
    # 3. Рисуем все строки друг под другом, не давая “уплывать”
    for idx, line in enumerate(lines):
        w = draw.textbbox((0,0), line, font=font)[2]
        x = block_x + (block_w - w) // 2  # Центр по горизонтали
        # Обводка:
        outline_range = max(1, int(font.size / 15))
        for ox in range(-outline_range, outline_range+1):
            for oy in range(-outline_range, outline_range+1):
                draw.text((x+ox, y+oy), line, font=font, fill='black')
        draw.text((x, y), line, font=font, fill='white')
        y += line_heights[idx]
        if idx < len(lines)-1:
            y += int(font.size * 0.2)  # Межстрочный отступ

# Использование:
# draw_text_fill(draw, "ТВОЙ ТЕКСТ", "fonts/impact.ttf", block_x, block_y, block_w, block_h)

# Пример использования в make_meme:
def make_meme(template_path, text, out_path, font_path="fonts/impact.ttf"):
    img = Image.open(template_path).convert("RGB")
    w, h = img.size

    banner_height = int(h * 0.18)
    new_img = Image.new("RGB", (w, h + banner_height), color=(0, 0, 0))
    new_img.paste(img, (0, 0))
    draw = ImageDraw.Draw(new_img)

    draw_text_fill(draw, text, font_path, 0, h, w, banner_height)
    new_img.save(out_path)
    return out_path

