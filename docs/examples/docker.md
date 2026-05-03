# Example: Docker Deployment

Generate deployment files:

```sh
resux deploy . --preset docker
```

A typical Dockerfile looks like:

```Dockerfile
FROM node:24-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm prune --omit=dev

FROM node:24-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000
COPY --from=build /app /app
EXPOSE 3000
CMD ["npm", "run", "start"]
```

Build and run:

```sh
docker build -t resux-app .
docker run --rm -p 3000:3000 resux-app
```

Check health:

```sh
curl http://localhost:3000/__resux/health
```

If your reverse proxy owns security headers, start Resux with:

```sh
resux start . --no-security-headers
```
