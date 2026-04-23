Here’s a clean, no-nonsense `.md` file you can drop straight into your project and follow tomorrow:

---

```md
# 🎓 CodeCraft Website Plan (Anti-Piracy + Access Control)

## 🎯 Goal
Create a simple website that:
- Confirms legitimate students
- Protects lesson recordings
- Reduces piracy and link sharing

---

## 🏗️ MVP Structure

### 1. Landing Page
Purpose: Build trust and legitimacy

Include:
- Program name (CodeCraft)
- Description of what students will learn
- Schedule and duration
- Contact (WhatsApp)

---

### 2. Student Verification Page

Route:
```

/verify?user=<username>

```

Shows:
- ✅ Registered student
- Plan (e.g., 12-week program)
- Status (Active / Expired)

Purpose:
- Prevent fake “I already paid” claims

---

### 3. Login System

Basic auth system:
- Username + password
- Session-based login (JWT or Flask session)

Only logged-in users can:
- Access videos
- Get Drive links

---

## 🎥 Video Delivery (Google Drive + iframe)

### Basic Setup
- Upload videos to Google Drive
- Use iframe embed inside your site

---

## 🔐 Anti-Piracy System

### 1. Backend-Controlled Links
DO NOT expose raw Google Drive links directly.

Instead:
- Store links on backend
- Return link only after login
- Optionally rotate links

---

### 2. Dynamic Watermark (IMPORTANT)

Overlay on video:
```

User: <username> | Date | CodeCraft

```

Implementation:
- Place a div over the iframe
- Position: absolute
- Low opacity

Purpose:
- Trace leaks to specific users
- Discourage sharing

---

### 3. Session Expiry

- Sessions expire after 1–2 hours
- Require re-login

Result:
- Shared links stop working

---

### 4. Weekly Access Code

Each class:
- Generate code like:
```

WEEK7-AB12

```

Require users to enter it before unlocking video.

---

### 5. Disable Easy Actions (Optional)

- Disable right-click
- Hide obvious controls
- Prevent easy copying

Note:
These are just deterrents, not real protection.

---

### 6. Activity Logging

Track:
- User
- Video accessed
- Timestamp

Flag:
- Extremely fast or repeated access

---

### 7. Content Splitting

Instead of:
- One full video

Use:
- Multiple parts (Part 1, Part 2, etc.)

Result:
- Makes piracy more annoying

---

### 8. Notice (Psychological Deterrent)

Display message:

```

Each video is uniquely tagged. Sharing may result in removal from the program.

```

---

## ⚙️ Tech Stack

### Backend
- Flask
- JWT or session auth
- SQLite/PostgreSQL

### Frontend
- HTML + CSS + JS
OR
- Vue (optional)

---

## 🚀 Build Order (IMPORTANT)

### Day 1
- Landing page
- Basic login system

### Day 2
- Protected video page
- Embed Google Drive iframe

### Day 3
- Add watermark overlay
- Add verification page

### Day 4
- Add session expiry
- Add weekly access codes

---

## ⚠️ Reality Check

You cannot fully stop screen recording.

Goal is to:
- Make sharing inconvenient
- Make leaks traceable
- Maintain control over access

---

## ✅ Final System

You will have:
- A legit online presence
- Controlled student access
- Reduced piracy risk
- A scalable foundation

---

Sleep. Build tomorrow. Ship fast.
```

---

If you want next step tomorrow, I can help you turn this into:

* actual Flask routes
* or the exact HTML/CSS for the watermark overlay

Just say “continue” when you’re back.
