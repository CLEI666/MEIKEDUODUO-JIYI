# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## API Keys

### Brave Search
- **Key:** BSA8XydppwY2wZT6yG7ITbbNtS5M8Cv

---

## 飞书发图脚本

**运行飞书发图脚本时必须先设置编码：**
```powershell
$env:PYTHONIOENCODING="utf8"; python <脚本路径> <图片路径> <open_id> <app_id> <app_secret>
```

- **脚本**：`C:\Users\Administrator\.openclaw\workspace\skills\feishu-send-file\scripts\send_image.py`
- **app_id**：`cli_a94880223db81cc6`
- **app_secret**：`Pu678ngxjEfBgUmbn8MyHciFsnmjZQur`
- **用户open_id**：`ou_21ff06ffa3f93234461308e06a89f3af`
- **注意**：必须先加 `$env:PYTHONIOENCODING="utf8"` 否则报GBK编码错误

Add whatever helps you do your job. This is your cheat sheet.
