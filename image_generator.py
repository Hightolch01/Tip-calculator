from PIL import Image, ImageDraw, ImageFont
import os
import datetime

def generate_receipt_image(bill: float, tax: float, tip: float, people: int, total: float, path: str):
    width, height = 400, 600
    padding = 30
    line_height = 40
    
    image = Image.new('RGB', (width, height), color=(220, 220, 220))
    draw = ImageDraw.Draw(image)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_body = ImageFont.truetype("arial.ttf", 18) 
    except IOError:
        print("Ошибка шрифта")
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()

    y_position = padding
    
    draw.text((padding, y_position), "КВИТАНЦИЯ ОБ ОПЛАТЕ", fill="black", font=font_title)
    y_position += 60
    
    items = [
        ("СУММА СЧЕТА:", f"{bill:.2f} ₽"),
        ("НАЛОГ:", f"{tax:.2f}%"),
        ("ЧАЕВЫЕ:", f"{tip:.2f}%"),
        ("ГОСТЕЙ:", f"{people} чел."),
        ("-" * 50, ""), 
        ("ИТОГО ВСЕГО:", f"{total:.2f} ₽"),
        ("НА ЧЕЛОВЕКА:", f"{total / people:.2f} ₽"),
    ]
    
    for key, value in items:
        draw.text((padding, y_position), key, fill="black", font=font_body)
        
        if value: 
            bbox = font_body.getbbox(value)
            text_width = bbox[2] - bbox[0]
        else:
            text_width = 0
            
        x_value_pos = width - padding - text_width
        draw.text((x_value_pos, y_position), value, fill="black", font=font_body)
        
        y_position += line_height
        
        current_year = datetime.datetime.now().year
    footer_text = f"Автоматический расчет калькулятором \n© TipCalc {current_year}"
    
    bbox = font_body.getbbox(footer_text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    y_position_footer = height - padding - text_height
    
    x_position_footer = (width - text_width) + 90
    
    draw.text((x_position_footer, y_position_footer), footer_text, fill="gray", font=font_body, align="center")
              
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    image.save(path, format="PNG")