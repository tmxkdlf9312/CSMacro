import tkinter as tk
from tkinter import messagebox

# 템플릿 정의
templates = {
    1: (
        "은행: KB국민은행\n"
        "예금주: 김철기\n"
        "계좌번호: 360101-04-194116\n\n"
        "주문내역 : {}\n"
        "추가요청 : {}\n"
        "비용 : 배송비포함 {}원 (배송비 {}원)\n\n"
        "주문내역 맞는지 꼭 확인하고 입금해주세요!\n\n"
        "입금후 수령자분의 성함, 연락처, 주소 부탁드리겠습니다"
    ),
    2: (
        "안녕하세요 {}님 아크릴업체입니다\n\n"
        "주문을 확인해보니 주문항목이 불분명하여 연락드렸습니다\n\n"
        "1. 원하시는 소재 (아크릴, PC, PVC, 포맥스 등)\n"
        "2. 색상\n"
        "3. 두께\n"
        "4. 사이즈\n"
        "5. 갯수\n\n"
        "위에 있는 항목들에 대해 알려주시면 제작진행하겠습니다\n\n"
        "감사합니다"
    ),
    3: (
        "안녕하세요 {}님 아크릴업체입니다\n\n"
        "고객님께서 주문해주신 {}은 가격이 {}원입니다\n\n"
        "현재 결제는 {}만 되어있어서 연락드렸습니다\n\n"
        "차액이 {}원에 대해 취소후 재결제하는 방법이 있고, 계좌이체 방식이 있습니다\n\n"
        "어떤게 편하신가요?"
    ),
    4: (
        "안녕하세요 {}님 아크릴업체입니다\n\n"
        "고객님께서 견적서 넣어주신건 보고 연락드렸습니다\n\n"
        "결제하실 예정이시면 말씀해주세요\n\n"
        "작업목록에 올려두겠습니다\n\n"
        "주문제작이다보니 순번이 밀리면 출고날짜가 밀려서 연락드렸습니다"
    )
}

def generate_message():
    template_number = template_var.get()
    
    # 입력받은 값들
    inputs = [entry.get() for entry in entry_fields]
    
    # 템플릿에서 메시지 생성
    message = templates[template_number].format(*inputs)
    
    # 메시지 출력
    messagebox.showinfo("생성된 메시지", message)

# GUI 설정
root = tk.Tk()
root.title("배송 템플릿 매크로")

# 템플릿 선택
template_var = tk.IntVar(value=1)
for index in range(1, 5):
    tk.Radiobutton(root, text=f"템플릿 {index}", variable=template_var, value=index).pack(anchor=tk.W)

# 입력 필드 생성
entry_fields = []
for i in range(5):
    entry = tk.Entry(root)
    entry.pack(pady=5)
    entry_fields.append(entry)

# 메시지 생성 버튼
generate_button = tk.Button(root, text="메시지 생성", command=generate_message)
generate_button.pack(pady=10)

root.mainloop()
