# Report Relay

Discord 채널 메시지를 Slack으로 자동 전달하는 봇입니다.

## 기능

- 지정된 Discord 채널의 새 메시지 실시간 감지
- Slack Incoming Webhook으로 메시지 전달
- 첨부파일 링크 포함 지원
- Docker 컨테이너 배포 지원

## 설정

### 1. 환경변수 설정

```bash
cp .env.example .env
```

`.env` 파일을 편집하여 다음 값을 설정합니다:

| 변수 | 설명 |
|------|------|
| `DISCORD_BOT_TOKEN` | Discord 봇 토큰 |
| `DISCORD_CHANNEL_ID` | 감시할 채널 ID |
| `SLACK_WEBHOOK_URL` | Slack Incoming Webhook URL |

### 2. Discord 봇 설정

[DISCORD_BOT_SETUP_GUIDE.md](DISCORD_BOT_SETUP_GUIDE.md) 참고

### 3. Slack Webhook 설정

1. [Slack API](https://api.slack.com/apps)에서 앱 생성
2. **Incoming Webhooks** 활성화
3. **Add New Webhook to Workspace** 클릭
4. 메시지를 받을 채널 선택
5. Webhook URL 복사

## 실행

### Docker (권장)

```bash
docker-compose up -d --build
```

### 로컬 실행

```bash
pip install -r requirements.txt
cd src
python main.py
```

## 로그 확인

```bash
docker-compose logs -f report-relay
```
