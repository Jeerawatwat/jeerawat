""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:

total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """
def analyze_scores(scores):
    total = sum(scores)
    average = round(total / len(scores), 1) if scores else 0
    highest = max(scores) if scores else None
    lowest = min(scores) if scores else None
    passed = sum(1 for score in scores if score >= 70)
    
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }
scores = [80, 65, 90, 70, 55]
result = analyze_scores(scores)
print(result)
