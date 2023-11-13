# Stage 1: Build react app with Node.js
FROM node:18 AS builder

WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

# Stage 2: Serve app with Nginx server
FROM nginx:stable-alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
