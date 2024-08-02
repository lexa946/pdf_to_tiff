import fitz  # PyMuPDF
from PIL import Image
def pdf_to_tiff(pdf_path, tiff_path):
    # Открываем PDF файл
    pdf_document = fitz.open(pdf_path)
    # Переменная для хранения всех страниц в виде изображений
    images = []
    # Проходим по всем страницам PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # Загружаем страницу
        pix = page.get_pixmap()  # Получаем изображение страницы в формате Pixmap
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Конвертируем Pixmap в Image
        images.append(img)
    # Сохраняем все страницы в один TIFF файл
    if images:
        images[0].save(
            tiff_path,
            save_all=True,
            append_images=images[1:],
            compression="tiff_deflate"
        )
    else:
        print("No pages found in PDF.")
# Пример использования
pdf_path = "Диплом.pdf"
tiff_path = "Диплом.tiff"
pdf_to_tiff(pdf_path, tiff_path)
