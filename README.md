# AgriAssist AI

AgriAssist AI is a multi-modal agricultural advisor providing localized recommendations on irrigation, pest/disease management, market prices, and government schemes.  
This repository contains the **mock backend** setup to allow frontend development to start in parallel.

---

## 📦 Features Implemented (Day 1)
- **FastAPI backend** with initial folder structure.
- **Mock endpoints** for MVP:
  - `POST /api/v1/query` → Returns a sample irrigation recommendation.
  - `POST /api/v1/image/pest` → Returns mock pest detection result.
  - `GET /api/v1/recommendation/irrigation` → Returns mock irrigation advice.
  - `GET /api/v1/market/price` → Returns mock market trend.
  - `WS /ws/live` → Streams mock progress messages.
- **CORS middleware** configured for frontend compatibility.
- **Swagger UI** auto-generated for easy API exploration.

---
