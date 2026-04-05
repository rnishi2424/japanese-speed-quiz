FROM node:24

WORKDIR /app

# dependencies
COPY package.json package-lock.json* ./
RUN npm install

COPY . .

# expost Next.js port
EXPOSE 3000

# run dev server
CMD ["npm", "run", "dev"]