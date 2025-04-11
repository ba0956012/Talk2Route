# 🧭 Smart Indoor Navigator (Powered by Azure OpenAI & A* Pathfinding)

This project is a **smart indoor navigation system** that leverages natural language input and AI inference to find and visualize optimal paths within a grid-based indoor map. It combines:

- 🧠 Azure OpenAI (ChatGPT) for semantic destination recognition
- 📍 A* (A-Star) algorithm for path planning
- 🗺️ Matplotlib for map visualization and labeled routes

---

## 🚀 Features

- ✨ **Natural Language Destination Detection**  
  Type queries like _“I want to go to the restroom”_ and let the AI decide the most relevant destination.

- 🔍 **A* Pathfinding Algorithm**  
  Calculates the shortest path from your current location to the target.

- 🎨 **Map Visualization**  
  Clearly displays the map grid and planned path with color-coded labels and legends.

- 📢 **Step-by-Step Direction Output**  
  Guides the user with direction-based step instructions (e.g., "Go right 5 steps").

---

## 🛠️ Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
