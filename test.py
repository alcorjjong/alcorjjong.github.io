import os

def convert_to_utf8(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                # 우선 기본 인코딩으로 열어보기 시도
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"{filepath} : 이미 UTF-8")
            except UnicodeDecodeError:
                # UTF-8이 아니면, 기본 인코딩 또는 다른 인코딩으로 시도해서 변환
                try:
                    with open(filepath, 'r', encoding='euc-kr') as f:
                        content = f.read()
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"{filepath} : euc-kr -> UTF-8 변환 완료")
                except Exception as e:
                    print(f"{filepath} : 변환 실패 - {e}")

# 사용 예시 (경로 지정)
convert_to_utf8('./')