# FlowForge: Full-Stack Task Management System

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=flat&logo=react&logoColor=%2361DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)

FlowForge is a robust Kanban-style task management application built to demonstrate modern full-stack architecture. It
features a reactive Drag-and-Drop* interface (in progress), a high-performance Python backend, and fully containerised
deployment.

## Tech Stack

* **Frontend:** React (Vite), TypeScript, Tailwind CSS
* **Backend:** Python, FastAPI, Pydantic, SQLAlchemy
* **Database:** SQLite (Dev) / PostgreSQL (Prod ready)
* **DevOps:** Docker, Docker Compose, Nginx

## Key Features

* **Kanban Workflow:** Organise tasks by status (To Do, In Progress, Done).
* **Instant Interaction:** Create, Delete, Edit, and Move tasks with real-time UI updates.
* **Robust API:** Fully documented REST API with automatic Swagger UI generation.
* **Dockerised:** Single-command deployment for both frontend and backend services.

## How to Run

Prerequisites: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/debiludebilas/Full-Stack-Task-Management-Issue-Tracker-App.git](https://github.com/debiludebilas/Full-Stack-Task-Management-Issue-Tracker-App.git)
   cd flowforge
   ```

2. **Start the application:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   * **Frontend (Task Board):** [http://localhost:5173](http://localhost:5173)
   * **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

## Future Roadmap (In Order)

1. **Visual Polish**
* **Goal:** Make it look like Trello or Jira.
* **Tech:** Tailwind
* **Ideas:** 
  * Color-coded badges (Red for "Urgent" and green for "chill").
  * Uploadable avatars or custom given ones.
  * Animations 

2. **Drag & Drop Tasks**
* **Goal:** Made so the cards are actually draggable.
* **Tech:** Library - `@dnd-kit/core`

3. **Authentication**
* **Goal:** "Log In" screen. Users can only see their own tasks.
* **Tech:** JWT (JSON Web Tokens), `bcrypt` (password hashing), React Context.
* **Notes:** Going to be quite hard as I'll need to rewrite the database and API points.