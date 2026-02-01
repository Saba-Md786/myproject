This project is a static DevOps learning website served using NGINX and containerized with Docker.
It explains the evolution of software development from Waterfall → Agile → DevOps and introduces important DevOps tools in a simple, student-friendly way.

The application is lightweight, fast, and suitable for real-world DevOps hosting scenarios.

🛠️ Technologies Used

HTML – Static web content

NGINX – Web server

Docker – Containerization

Linux – Base environment

📂 Project Structure

nginx-devops-project/
│
├── index.html
├── Dockerfile
└── README.md

🐳 Dockerfile Explanation

The project uses an NGINX base image to serve static HTML content.

FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80


nginx:alpine → Lightweight NGINX image

COPY → Copies HTML file to NGINX default web directory

EXPOSE 80 → Exposes HTTP port

▶️ How to Build and Run the Project
Step 1: Build Docker Image
docker build -t nginximg .

Step 2: Run Docker Container
docker run -d -p 80:80 nginxapp_cont

Step 3: Access in Browser
http://localhost


(or use EC2 public IP if deployed on cloud)
