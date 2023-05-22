import fitz
import os

print("Program started...")
print("Converting PDF files to images...")

def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_counter = 1
    
    # Extract number from the PDF file name
    pdf_file_name = os.path.basename(pdf_path)
    number = pdf_file_name.split("_")[1].split(".")[0]
    
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            
            image_path = os.path.join(output_folder, f"m3_{number}_{image_counter}.jpg")
            with open(image_path, "wb") as f:
                f.write(image_data)
            
            image_counter += 1

    doc.close()

def process_pdf_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        extract_images_from_pdf(pdf_path, output_folder)

# Example usage
input_folder = "PDF files"
output_folder = "Converted Images"
process_pdf_files(input_folder, output_folder)
print("Program finished...")