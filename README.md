다음은 위 코드에 대한 `README.md` 파일을 전문가답게 작성한 예시입니다. 이 문서에는 프로젝트 개요, 설치 방법, 사용법, 코드 설명 등이 포함되어 있습니다.

---

# Face Gender and Age Detection with InsightFace

This project uses the [InsightFace](https://github.com/deepinsight/insightface) library to detect faces and predict both gender and age. The predicted gender is returned as a probability (using a sigmoid function), and images are categorized and saved based on the detected gender and age. The file names follow the format `age_genderProbability_originalFilename.extension`.

## Features

- Detects faces from images using the `InsightFace` library.
- Predicts age and gender for each detected face.
- Categorizes images into folders (`Male` and `Female`) based on the predicted gender.
- Saves images with file names formatted as `age_genderProbability_originalFilename.extension`, where `genderProbability` is a float value between 0 and 1 representing the confidence of the gender prediction.
  
## Getting Started

### Prerequisites

- Python 3.7+
- `InsightFace` library
- `OpenCV` for image processing

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repository-url/face-gender-age-detection.git
   cd face-gender-age-detection
   ```

2. Set up a Python virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure to include the following libraries in your `requirements.txt`:
   - `insightface`
   - `opencv-python`
   - `numpy`
   - `shutil` (no installation required as it is part of the standard Python library)

### Usage

To run the script, use the following command:

```bash
python app.py [image_folder_path] [output_folder_path]
```

- `image_folder_path`: Path to the folder containing input images.
- `output_folder_path`: Path to the folder where categorized images will be saved.

### Example

```bash
python app.py ./input_images ./output_images
```

This command processes all images in the `input_images` folder, predicts their gender and age, and saves them in `output_images/Male` or `output_images/Female` with a filename format of `age_genderProbability_originalFilename.extension`.

### Output

For each image in the input folder, if a face is detected, the image will be saved in either the `Male` or `Female` folder, depending on the predicted gender. The filename will include the predicted age and gender probability.

For example, an image `person1.jpg` with a predicted age of 25 and a gender probability of 0.67 (indicating a 67% chance of being male) will be saved as:

```
output_images/Male/25_0.67_person1.jpg
```

### Code Structure

- **`load_model()`**: Loads the InsightFace model with the `detection` and `genderage` modules enabled.
  
- **`sigmoid(x)`**: A helper function to convert raw gender prediction scores into a probability using the sigmoid function.

- **`process_image()`**: Processes each image, detects faces, predicts age and gender, and saves the image in the appropriate gender folder with the correct filename format.

- **`process_folder()`**: Iterates over all images in the input folder, processing each image and categorizing it into the correct folder based on gender.

### File Naming Convention

The output images are saved in the following format:

```
age_genderProbability_originalFilename.extension
```

Where:
- `age`: Predicted age of the detected face.
- `genderProbability`: A floating-point number (0.00 to 1.00) representing the confidence of the predicted gender (closer to 1.00 means male, closer to 0.00 means female).
- `originalFilename`: The name of the input file without the extension.
- `extension`: The original file extension (e.g., `.jpg`, `.png`).

### Folder Structure

After running the script, the output directory will have the following structure:

```
output_folder/
    ├── Male/
    │   ├── age_genderProbability_originalFilename.jpg
    │   └── ...
    └── Female/
        ├── age_genderProbability_originalFilename.jpg
        └── ...
```

### Customization

You can adjust the gender threshold inside the `process_image()` function by modifying the condition for gender classification.

```python
predicted_gender = 'Male' if gender_probability > 0.5 else 'Female'
```

Change `0.5` to your desired threshold to adjust the sensitivity of the gender prediction.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgements

- [InsightFace](https://github.com/deepinsight/insightface): Face analysis project based on deep learning.
- [OpenCV](https://opencv.org/): Open source computer vision and machine learning software library.

---

Feel free to modify and enhance this README file based on your project needs and any additional features you may add.
