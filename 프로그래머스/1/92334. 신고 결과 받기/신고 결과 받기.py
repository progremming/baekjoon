def solution(id_list, report, k):
    # 중복 신고를 set을 사용하여 처리
    unique_reports = {}  # 신고한 사람 -> 신고받은 사람 (set으로 저장하여 중복 제거)
    
    for r in report:
        sender, receiver = r.split()
        if receiver not in unique_reports:
            unique_reports[receiver] = set()
        unique_reports[receiver].add(sender)  # receiver를 신고한 sender 추가
    
    # 신고 받은 횟수 계산
    score = {}
    for receiver, senders in unique_reports.items():
        score[receiver] = len(senders)  # receiver가 받은 신고 횟수
    
    # 정지된 사용자 목록 추출
    suspended = set(user for user, count in score.items() if count >= k)
    
    # 각 사용자가 받은 결과 메일 카운트 초기화
    returns = {user: 0 for user in id_list}
    
    # 결과 메일 발송
    for receiver, senders in unique_reports.items():
        if receiver in suspended:
            for sender in senders:
                returns[sender] += 1  # 정지된 사용자를 신고한 사람에게 메일 보냄
    
    return list(returns.values())
