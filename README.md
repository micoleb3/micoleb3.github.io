# 채윤식 · Embedded & Industrial Automation Portfolio

하드웨어부터 펌웨어까지, 직접 만드는 제어 시스템.
STM32 임베디드 제어, On-Device AI 비전, PLC 산업 자동화 프로젝트를 정리한 포트폴리오입니다.

**🔗 https://micoleb3.github.io**

---

## Projects

| 프로젝트 | 내용 | 내 역할 | 코드 |
|---|---|---|---|
| **ChaPaRi** — 모바일 물품 회수 로봇 | STM32 4WD 차량 + 5축 로봇팔, 스마트폰 원격 제어 | 주행 제어 · 로봇팔 서보 제어 · 하드웨어/전원 설계 | [mobile-retrieval-robot](https://github.com/sditr0414/mobile-retrieval-robot) |
| **Safe Eye** — On-Device AI 안전 감지 | Raspberry Pi 5에서 PPE 미착용·위험구역 접근 실시간 감지 | PPE MLC 모델 설계·학습 · 위험구역 감지 시스템 | [safe-eye](https://github.com/micoleb3/safe-eye) |
| **PLC 분류 적재·배출 자동화** | 금속/비금속 판별 → 층별 적재 → 배출 | 래더 로직 · 서보 위치결정 · HMI · 안전 설계 | — |

## Tech Stack

`STM32` `C` `HAL` `FreeRTOS` `Python` `YOLO11` `MobileNetV3` `TFLite` `ROS 2` `Mitsubishi PLC` `GX Works2` `GT Designer3`

---

<details>
<summary>이 저장소 구조 · 로컬 실행</summary>

```text
index.html    사이트 본문
style.css     레이아웃 · 컴포넌트
themes.css    색상 토큰 · 다크/인쇄 테마
app.js        네비게이션 · 이메일 복사 · 로컬 테마 비교
assets/       프로젝트 이미지 · 프로필 · QR
preview.py    로컬 프리뷰 서버 (자동 새로고침)
```

```bash
python3 preview.py
# http://127.0.0.1:4174/
```

</details>
