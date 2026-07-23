# -*- coding: utf-8 -*-
"""아침 브리핑 봇 — 골격.

『나는 AI를 사장으로 고용했다』 부록 E, 템플릿 ②(5장용).

받자마자 하는 일: "좋은 아침입니다"라는 인사와 함께, CHECKS에 들어 있는 모든 확인 항목의
결과를 한 줄씩 정리해 텔레그램으로 한 통 보냅니다. 기본 상태에서는 확인 항목이 딱 하나뿐이고,
그마저도 항상 통과하는 자리표시자입니다 — 바로 그 자리를 여러분이 채우면 됩니다.

이 파일을 쓰는 가장 빠른 방법은 손으로 직접 고치는 게 아닙니다. 이 파일을 클로드에게 보여주고
이렇게 말하세요.

    내 텔레그램 토큰이랑 chat_id를 여기에 넣어줘. 토큰은 (붙여넣기), chat_id는 (붙여넣기)야.

그다음:

    자리표시자 확인 항목을 <내가 진짜로 신경 쓰는 것>을 확인하는 코드로 채워줘.

일부러 이렇게 설계한 두 가지가 있습니다. 둘 다 이 책 저자가 이미 겪은 사고라서 넣어 둔 장치입니다.

  * 콘솔에는 절대 이모지를 출력하지 않습니다. print()에 이모지 하나가 섞였다가 한글 윈도우에서
    24시간 돌던 봇을 죽인 적이 있습니다. 텔레그램 *메시지* 안의 이모지는 괜찮습니다 — 그건
    콘솔이 아니니까요.
  * 확인 항목 하나가 오류를 내도 브리핑 전체가 죽지 않습니다. 그 항목만 오류 줄로 보고되고
    나머지는 그대로 실행됩니다. 조용히 죽는 감시 스크립트는 감시 스크립트가 아예 없는 것보다
    더 나쁩니다.
"""

from __future__ import annotations

import datetime as _dt
import traceback
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# 1. 이 두 줄을 채우세요. 값이 어디서 나오는지는 5장에 나옵니다.
#    실제 값을 여기에 붙여넣는 순간 이 파일은 시크릿을 담게 됩니다: 깃에 올리지 말고,
#    가능한 한 빨리 .env 파일로 옮기세요(4장 참고).
# ---------------------------------------------------------------------------
BOT_TOKEN = "여기에_붙여넣기"
CHAT_ID = "여기에_붙여넣기"


# ---------------------------------------------------------------------------
# 2. 여러분의 확인 항목. 각 함수는 (성공여부, 한 줄 메시지)를 돌려줍니다.
# ---------------------------------------------------------------------------
def check_example_placeholder() -> tuple[bool, str]:
    """예시 자리입니다. 이 함수 몸통을 진짜 확인 코드로 바꾸세요.

    클로드에게 이렇게 요청하세요: "이 자리를 <무언가>를 확인하는 코드로 채워줘." 추가 라이브러리가
    필요 없는 아이디어들: 어떤 파일이 N시간보다 최신인가, 어떤 폴더가 존재하는가, 예약 작업이
    마지막에 정상 종료(0)했는가, 어떤 웹사이트가 200을 돌려주는가.
    """
    return True, "자리표시자 확인 항목 — 진짜 확인으로 바꿔 주세요"


CHECKS = [
    ("예시", check_example_placeholder),
    # ("오늘 블로그 발행됨", check_blog_published),
    # ("백업 드라이브 연결됨", check_backup_drive),
]


# ---------------------------------------------------------------------------
# 3. 배관. 이 줄 아래는 손댈 필요가 없습니다.
# ---------------------------------------------------------------------------
def send_telegram(text: str) -> None:
    if BOT_TOKEN == "여기에_붙여넣기" or CHAT_ID == "여기에_붙여넣기":
        raise SystemExit(
            "BOT_TOKEN / CHAT_ID가 아직 자리표시자('여기에_붙여넣기') 그대로입니다. 먼저 값을 "
            "채우거나(5장), 클로드에게 채워 달라고 요청하세요."
        )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text}).encode("utf-8")
    with urllib.request.urlopen(url, data=data, timeout=20) as resp:
        resp.read()


def build_report() -> str:
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"좋은 아침입니다. 오늘의 회사 상태입니다 ({now})", ""]
    for label, fn in CHECKS:
        try:
            ok, message = fn()
        except Exception:                      # 확인 항목 하나가 죽어도 브리핑 전체는 살린다
            ok, message = False, traceback.format_exc(limit=1).strip().splitlines()[-1]
        lines.append(f"{'정상 ' if ok else '실패 '} {label}: {message}")
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    print(report)                              # 순수 텍스트만, 이모지 금지 — 위 설명 참고
    send_telegram(report)


if __name__ == "__main__":
    main()
