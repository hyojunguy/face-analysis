import cv2
import sys
import os
import shutil
from insightface.app import FaceAnalysis

# 1. 모델 로드
def load_model():
    app = FaceAnalysis(allowed_modules=['detection', 'genderage'])  # 성별 및 나이 예측 모듈 사용
    app.prepare(ctx_id=0, det_size=(640, 640))  # ctx_id=0은 GPU 사용, -1은 CPU 사용
    return app

# 2. 폴더 생성 함수 (성별 폴더)
def create_gender_folders(output_folder):
    male_folder = os.path.join(output_folder, "Male")
    female_folder = os.path.join(output_folder, "Female")
    os.makedirs(male_folder, exist_ok=True)
    os.makedirs(female_folder, exist_ok=True)
    return male_folder, female_folder

# 3. 이미지 처리 및 복사 함수
def process_image(app, image_path, male_folder, female_folder):
    # 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        print(f"이미지를 불러올 수 없습니다: {image_path}")
        return
    
    # 얼굴 검출 및 속성 분석
    faces = app.get(img)  # 이미지에서 얼굴을 검출하고 성별과 나이를 분석
    
    for idx, face in enumerate(faces):
        predicted_gender = 'Male' if face['gender'] > 0.5 else 'Female'
        age = int(face['age'])  # 나이를 정수로 변환

        # 원본 파일명과 확장자 분리
        original_filename = os.path.basename(image_path)
        name, ext = os.path.splitext(original_filename)

        # 파일명은 나이와 원본 파일명을 조합하여 저장
        new_filename = f"{age}_{name}{ext}"
        
        if predicted_gender == 'Male':
            dest_path = os.path.join(male_folder, new_filename)
        else:
            dest_path = os.path.join(female_folder, new_filename)
        
        # 이미지 복사 및 이름 변경
        shutil.copy(image_path, dest_path)
        print(f"이미지 복사 완료: {image_path} -> {dest_path}")

def process_image_backup(app, image_path, male_folder, female_folder):
    # 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        print(f"이미지를 불러올 수 없습니다: {image_path}")
        return
    
    # 얼굴 검출 및 속성 분석
    faces = app.get(img)  # 이미지에서 얼굴을 검출하고 성별과 나이를 분석
    
    for idx, face in enumerate(faces):
        gender_value = face['gender']  # 성별 값 (0 ~ 1 사이 값)
        predicted_gender = 'Male' if gender_value > 0.5 else 'Female'
        age = int(face['age'])  # 나이를 정수로 변환

        # 원본 파일명과 확장자 분리
        original_filename = os.path.basename(image_path)
        name, ext = os.path.splitext(original_filename)

        # 성별 값 소수점 둘째 자리까지 반올림하여 파일명에 포함
        gender_value_str = f"{gender_value:.2f}"

        # 파일명은 나이, 성별 값, 원본 파일명을 조합
        new_filename = f"{age}_{gender_value_str}_{name}{ext}"
        
        if predicted_gender == 'Male':
            dest_path = os.path.join(male_folder, new_filename)
        else:
            dest_path = os.path.join(female_folder, new_filename)
        
        # 이미지 복사 및 이름 변경
        shutil.copy(image_path, dest_path)
        print(f"이미지 복사 완료: {image_path} -> {dest_path}")


# 4. 폴더 내 모든 이미지 처리 함수
def process_folder(app, folder_path, output_folder):
    # 성별에 따라 폴더 생성
    male_folder, female_folder = create_gender_folders(output_folder)
    
    # 폴더 내 모든 파일 탐색
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        # 이미지 파일만 처리 (확장자로 필터링)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            process_image(app, image_path, male_folder, female_folder)

# 5. 메인 함수
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("사용법: python app.py [이미지 폴더 경로] [결과 저장 폴더 경로]")
        sys.exit(1)
    
    folder_path = sys.argv[1]  # 커맨드라인에서 이미지 폴더 경로 받기
    output_folder = sys.argv[2]  # 결과 저장할 폴더 경로 받기

    model = load_model()  # 모델 로드
    process_folder(model, folder_path, output_folder)  # 폴더 내 모든 이미지 처리

