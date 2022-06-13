bp=[]
choice='y'

while choice=='y':
    highBlood=int(input('당신의 수축기혈압 수치는? : '))
    lowBlood=int(input('당신의 이완기혈압 수치는? : '))
    state="abnormal"
    print("당신의 혈압은 수축기 : " + str(highBlood) + " 이완기 : " +str(lowBlood) + " 입니다.")
    if highBlood < 90 and lowBlood < 60:
        print('당신의 혈압은 저혈압입니다.','꾸준한 운동으로 혈액순환 촉진 요함,충분한 수면 권장')
        state = "normal"
    if highBlood < 120 and highBlood >= 90 and lowBlood < 80 and lowBlood >= 60:
        print('당신의 혈압은 정상입니다.','현재 몸 상태를 잘 유지하세요')
        state = "normal"
    if highBlood >= 120 and highBlood < 140 and lowBlood >= 80 and lowBlood < 90:
        print('당신의 혈압은 고혈압 전단계입니다.','식이요법,체중관리,꾸준한 운동,금연,금주를 통해 혈압 관리 요함')
        state = "normal"
    if highBlood >= 140 and highBlood < 160 and lowBlood >= 90 and lowBlood < 100:
        print('당신의 혈압은 고혈압 1단계입니다.','생활습관 개선 요함,지속적 혈압 확인 권장')
        state = "normal"
    if highBlood >= 160 and highBlood < 200 and lowBlood >= 100 and lowBlood < 170 : 
        print('당신의 혈압은 고혈압 2단계입니다.','가까운 병원에 내원하여 의사 상담 권함,상담 후 혈압약 복용 권장')
        state = "normal"
    if state == "abnormal":
        print("잘못된 정보입니다. 혈압을 다시 측정하세요.")  
    
    #비정상 데이터가 입력되었을때, 저장 방지
    if state != "abnormal":
        s=input('혈압 수치를 저장하시겠습니까?(y/n)')
        if s=='y' or 'Y':
            bp.append(highBlood)
            bp.append(lowBlood)
            print("저장된 데이터 : " + str(bp))
        else:
            break
    
    choice=input('혈압을 더 확인하시겠습니까?(y/n)')
    if choice=='n':
        print('사용해 주셔서 감사합니다.')