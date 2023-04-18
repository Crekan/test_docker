# base image
FROM node:14.15.4-alpine

COPY test_docker /test_docker

# set working directory
WORKDIR /test_docker
EXPOSE 3000

# install app dependencies
COPY package*.json ./
RUN npm install

# build app
RUN npm run build

# start app
CMD ["npm", "start"]
