# 🚌 巴士到站 · 天氣

香港門口巴士到站監察器 — 即時九巴 / 城巴 ETA，附天氣資訊。

[![開啟 Web App](https://img.shields.io/badge/開啟-Web_App-f59e0b?style=for-the-badge)](https://nik-neural.github.io/hk-bus/)
[![站牌 Kiosk 模式](https://img.shields.io/badge/站牌-Kiosk_模式-c41e1e?style=for-the-badge)](https://nik-neural.github.io/hk-bus/kiosk.html)

## 功能

- 自訂多個巴士站，即時顯示到站時間
- 支援九巴 / 龍運、城巴路線
- 香港天氣 widget + 自動更新
- 可加入主畫面，全螢幕 kiosk 模式
- **[站牌 Kiosk 模式](https://nik-neural.github.io/hk-bus/kiosk.html)** — 直立細屏站牌 UI（HKO 天氣、大字 ETA）

## 站牌 Kiosk 模式

適合 Raspberry Pi、細 TFT 屏或門口直立顯示：

| 模式 | 連結 |
|------|------|
| 一般 UI | [nik-neural.github.io/hk-bus/](https://nik-neural.github.io/hk-bus/) |
| **站牌 Kiosk** | [nik-neural.github.io/hk-bus/kiosk.html](https://nik-neural.github.io/hk-bus/kiosk.html) |

一般版同 Kiosk 係分開入口；Raspberry Pi 請 bookmark `kiosk.html`

## 加入主畫面（PWA）

1. 用手機或電腦開啟上方連結
2. **Safari / Chrome** → 分享 / 選單 → **加入主畫面**

## 同系列 App

| | App | 說明 | 連結 |
|---|-----|------|------|
| 🚌 | **巴士到站** | 九巴 / 城巴 ETA + 天氣 | [nik-neural.github.io/hk-bus](https://nik-neural.github.io/hk-bus/) |
| 💰 | **圓子基金** | 群組消費記帳 + 圓子基金 | [nik-neural.github.io/circle-fund](https://nik-neural.github.io/circle-fund/) |
| ⚡ | **香港 EV 泊車** | 全港 EV 停車場即時空位 | [nik-neural.github.io/hk-ev-park](https://nik-neural.github.io/hk-ev-park/) |

## 技術

- 單一 HTML · Tailwind CDN · 零後端
- [GitHub Pages](https://pages.github.com/) 部署
- PWA（`manifest.json` + `icons/`）

## 資料來源

- 九巴 / 龍運：[data.etabus.gov.hk](https://data.etabus.gov.hk)
- 城巴：[rt.data.gov.hk](https://rt.data.gov.hk)
- 天氣（一般 UI）：[Open-Meteo](https://open-meteo.com) · Kiosk：[香港天文台](https://www.hko.gov.hk/)