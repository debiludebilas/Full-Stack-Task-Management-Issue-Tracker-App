FROM node:20-alpine as builder

WORKDIR /app

# Copy package files and install dependancies
COPY package.json package-lock.json ./
RUN npm install

# Copy source code and build it
COPY . .
RUN npm run build

# Serve with Nginx (web server)
FROM nginx:alpine

# Copy the built files to Ngnix's html folder
COPY --from=builder /app/dist /usr/share/nginx/html

# Open port 80, which is the standard
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]