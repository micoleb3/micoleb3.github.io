# Portfolio

채윤식(임베디드 · 산업 자동화) 개인 포트폴리오 웹사이트.

## Live Site

https://micoleb3.github.io

## Overview

- 프로젝트 중심 구성 (문제 → 역할 → 구현 → 검증 → 결과 → 배운 점)
- 직접 담당한 역할만 기술
- 웹은 다크 테마 / 인쇄(PDF)는 라이트 테마로 분리
- 정적 사이트 (외부 라이브러리 없음)

## Projects

- **ChaPaRi** — RC 집게차(그래플 트럭), STM32 모터 제어
- **Safe Eye** — Raspberry Pi 5 PPE·위험구역 감지 CCTV
- **Pinky Patrol & Docking** — ROS2/Gazebo 자율 순찰·도킹

## Tech Stack

`STM32` `ROS 2` `PLC` `C` `C++` `Python` `Linux`

## Local Preview

```bash
python3 preview.py
# http://127.0.0.1:4174/
```

## Branch Workflow

```text
dev
 ↓
Pull Request
 ↓
main
 ↓
GitHub Pages
```

## Files

```text
index.html    사이트 본문
style.css     레이아웃 · 컴포넌트
themes.css    색상 토큰 · 테마 · 인쇄
app.js        네비/복사/로컬 테마 비교
assets/       이미지 · QR 등
preview.py    로컬 프리뷰 서버(자동 새로고침)
```

> README = 저장소 설명 / Portfolio Website = 실제 상세 콘텐츠. 역할을 분리한다.
