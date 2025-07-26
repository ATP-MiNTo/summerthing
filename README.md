# 🚀 Starry Todo App

This is a beautiful, animated, and feature-rich Todo web app built with FastAPI and Docker Compose.

## ✨ Features

- **Add Todos:** Create new todos with a name and due date.
- **Edit Todos:** Edit the name and due date of any todo (click "Edit" to unlock fields).
- **Delete Todos:** Remove any todo you no longer need.
- **Toggle Status:** Mark todos as "Done" or "Undone" with a single click. All todos start as "Undone".
- **Status Colors:**
  - "Undone" todos have a coral background (`#FF746C`).
  - "Done" todos have a green background (`#B2FBA5`).
- **Due Date Display:** The due date is always visible, and for "Undone" todos, it's shown in white for clarity.
- **Filter & View:**
  - Show all todos
  - Show only upcoming todos (not yet due)
  - Show only "Done" or "Undone" todos (toggle with a button)
- **Responsive UI:** All controls and content stay centered and adapt to your screen.
- **Animated Star Background:** Enjoy a relaxing, animated starfield with falling, twinkling stars.

## 🛠️ Tech Stack
- FastAPI (backend)
- Jinja2 (templates)
- HTML/CSS/JS (frontend)
- Docker Compose (deployment)

## 🧑‍💻 How to Use
1. Start the app with Docker Compose.
2. Open the web UI in your browser.
3. Add, edit, delete, and toggle todos as you wish!
4. Use the filter buttons to view upcoming, done, or undone todos.

Enjoy your productive, starry todo experience!

---

## 📝 Copilot Prompt to Build This Web

Copy and paste the following prompt into GitHub Copilot (or your favorite AI coding assistant) to generate a similar starry todo web app:

```
Build a FastAPI-based Todo web app with the following features:
- Add, edit, and delete todos (each with a name and due date)
- Each todo has a status: "Undone" (default) or "Done"; allow toggling status with a button
- Show all todos on the homepage, with background color indicating status (Undone = #FF746C, Done = #B2FBA5)
- Show due date for each todo; for "Undone" todos, display the due date in white
- Filter buttons: Show All, Show Upcoming (not yet due), and a toggle button to switch between Done and Undone todos
- Responsive, modern UI with all controls centered
- Animated starry background: 400+ small, slow, falling, twinkling stars using JavaScript and CSS
- Use Jinja2 for templates and organize routes in separate files for scalability
```

Just copy, paste, and let Copilot do the rest!
