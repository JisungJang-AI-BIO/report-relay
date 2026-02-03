# Discord 봇 생성 안내서

Report Relay 봇 구동을 위해 아래 단계를 따라 Discord 봇을 생성해 주세요.

---

## 1. Discord Developer Portal 접속

1. [Discord Developer Portal](https://discord.com/developers/applications)에 접속합니다.
2. Discord 계정으로 로그인합니다.

---

## 2. 애플리케이션 생성

1. **"New Application"** 버튼을 클릭합니다.
2. 애플리케이션 이름을 입력합니다 (예: `Report Relay Bot`).
3. 약관에 동의하고 **"Create"** 버튼을 클릭합니다.

---

## 3. Bot 설정

1. 왼쪽 메뉴에서 **"Bot"**을 클릭합니다.
2. **"Add Bot"** 버튼을 클릭하고 확인합니다.
3. **Bot 설정에서 아래 항목을 활성화합니다:**
   - ✅ `MESSAGE CONTENT INTENT` (필수! 메시지 내용을 읽기 위해 필요)

---

## 4. Bot Token 복사

1. Bot 페이지에서 **"Reset Token"** 버튼을 클릭합니다.
2. 표시된 토큰을 **안전하게 복사하여 저장**합니다.

> ⚠️ **주의**: 토큰은 비밀번호와 같습니다. 절대 공개하지 마세요!

---

## 5. 서버에 봇 초대

1. 왼쪽 메뉴에서 **"OAuth2" → "URL Generator"**를 클릭합니다.
2. **SCOPES**에서 선택:
   - ✅ `bot`
3. **BOT PERMISSIONS**에서 선택:
   - ✅ `Read Messages/View Channels`
   - ✅ `Read Message History`
4. 하단에 생성된 URL을 복사하여 브라우저에서 열고, 원하는 서버에 봇을 추가합니다.

---

## 6. 채널 ID 확인

1. Discord 앱에서 **설정 → 앱 설정 → 고급**으로 이동합니다.
2. **"개발자 모드"**를 활성화합니다.
3. 감시할 채널을 우클릭하고 **"ID 복사"**를 선택합니다.

---

## 필요한 정보 전달 사항

개발팀에 아래 정보를 전달해 주세요:

| 항목 | 값 |
|------|-----|
| Bot Token | `[복사한 토큰]` |
| Channel ID | `[복사한 채널 ID]` |

---

## 문의

설정 중 문제가 발생하면 개발팀에 문의해 주세요.
