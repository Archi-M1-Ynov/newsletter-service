# newsletter-service

📬 Objectif
Ce microservice permet à un utilisateur de s'inscrire à une newsletter en validant son email. Les données sont stockées dans PostgreSQL.

⚙️ Stack utilisée
Python 3.10+

FastAPI

SQLAlchemy

PostgreSQL (via Docker)

Pydantic (EmailStr)


📦 Installation

git clone git@github.com:eshop-backend/newsletter-service.git
cd newsletter-service


python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🔐 .env requis

.env
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/newsletter_db
PORT=4004


🐳 Démarrer PostgreSQL (si besoin)
docker run -d \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=newsletter_db \
  -p 5433:5432 \
  --name newsletter-db postgres


🚀 Lancer le service

uvicorn main:app --reload --port 4004


📄 Endpoints disponibles

Méthode	URL	Description
POST	/subscribe	Ajoute un email à la liste
GET	/list	Récupère tous les inscrits


✅ Exemple d’inscription

POST /subscribe
Content-Type: application/json

{
  "email": "test@example.com"
}