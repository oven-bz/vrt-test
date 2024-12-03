import os
import ollama
import cv2


def grayscale_image(image_name):
    """Converts an image to grayscale.
    Args:
        image_name: The name of the image file.

    Returns:
        The path to the grayscale image.
    """

    image = cv2.imread(os.path.join("./images", image_name))

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image_path = os.path.join(
        "./images", f"{os.path.splitext(image_name)[0]}-gray.png"
    )
    cv2.imwrite(gray_image_path, gray_image)

    return gray_image_path


def analyze_image(image_path, prompt):
    """Analyzes an image using Llama 3.2-Vision and a given prompt.
    Args:
        image_path: Path to the image file.
        prompt: The prompt to guide the analysis.

    Returns:
        The response from the Llama 3.2-Vision model.
    """

    response = ollama.chat(
        model="llama3.2-vision:latest",
        messages=[{"role": "user", "content": prompt, "images": [image_path]}],
    )

    return response


image_name = "marked-answers.png"
gray_image_path = grayscale_image(image_name)

prompt = "Act as an OCR assistant. Analyze the provided image and identify the marked answer in each box. The answer is marked with a cross (X), a circle (O), and an underscore (_). There are 54 boxes arranged with the number on its left-side. Please output the number of the box and the marked answer."
response = analyze_image(gray_image_path, prompt)

print(response.message.model_dump_json())
