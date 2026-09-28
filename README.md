# Foodhead 🍳

Foodhead is a small recipe-sharing web app built as a first-semester web development project (frontend, backend and data). Users can sign up, log in and share their own recipes with ingredients, step-by-step instructions and a photo. Everyone can browse the recipes, and owners can edit or delete their own.

## Features

- **User accounts**: sign up, log in and log out, with hashed passwords and server-side sessions
- **Recipes**: create, view, edit and delete recipes with title, description, prep/cook time, servings, image, ingredients and instructions
- **Ownership checks**: only the author of a recipe can edit or delete it
- **Validation on both sides**: the same rules (in `regex.py`) drive the HTML form attributes and the server-side checks
- **Image uploads**: PNG, JPG and WebP up to 2 MB, saved under a random filename
- **Partial page updates** with [mixhtml](https://mixhtml.com): the server returns small HTML snippets that update the page without full reloads
- **Accessibility**: skip link, focus handling, screen reader announcements and error messages that stay until dismissed

## Tech stack

| Layer    | Tools |
|----------|-------|
| Backend  | Python 3.9, Flask, Flask-Session |
| Database | MariaDB 10.6 (managed via phpMyAdmin) |
| Frontend | Jinja templates, plain CSS, TypeScript, mixhtml |
| Tooling  | Docker and Docker Compose |

## Try it yourself

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
- Git

### 1. Clone the project

```bash
git clone https://github.com/katelijacobsen/web-dev-semester-1-fro-back-data.git
cd web-dev-semester-1-fro-back-data
```

### 2. Start the containers

```bash
docker compose up --build
```

This starts three containers:

| Service    | URL                    |
|------------|------------------------|
| Flask app  | http://localhost       |
| phpMyAdmin | http://localhost:8080  |
| MariaDB    | `localhost:3306`       |

### 3. Import the database

The database starts empty, so import the schema and sample data from `db/foodhead.sql`:

1. Open phpMyAdmin at http://localhost:8080 and log in with user `root` and password `password`.
2. Select the `foodhead` database on the left.
3. Go to **Import**, choose `db/foodhead.sql` and click **Import**.

Or from a terminal, while the containers are running:

```bash
docker exec -i x_mariadb mariadb -uroot -ppassword foodhead < db/foodhead.sql
```

### 4. Open the app

Go to http://localhost, create an account on the **Sign up** page, log in and share your first recipe.

To stop everything, press `Ctrl+C` in the terminal or run `docker compose down`.

> **Note:** The database credentials in `docker-compose.yml` and `config.py` are for local development only.

## Project structure

```
├── app.py              # Flask app: pages, recipe API routes and queries
├── api/user.py         # Sign up and login API routes
├── config.py           # Database connection
├── regex.py            # Shared validation rules and limits
├── helpers/            # Validation, formatting, caching and mixhtml response helpers
├── templates/          # Jinja templates (pages and partials)
├── static/
│   ├── app.css         # Styles
│   ├── src/app.ts      # TypeScript source
│   ├── dist/app.js     # Compiled JavaScript (committed, no build needed)
│   ├── mixhtml.js      # mixhtml library
│   └── uploads/        # Uploaded recipe images
├── db/foodhead.sql     # Database schema and sample data
├── Dockerfile
└── docker-compose.yml
```

## Editing the TypeScript

The compiled `static/dist/app.js` is already included, so you only need this if you change `static/src/app.ts`:

```bash
npx tsc
```

## Credits

- [mixhtml](https://mixhtml.com) by Santiago Donoso (MIT License)
