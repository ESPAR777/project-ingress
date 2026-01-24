# Use the lightweight Nginx image
FROM nginx:alpine

# Copy your frontend files to the default Nginx public directory
# This assumes your HTML file is named index.html
COPY . /usr/share/nginx/html/

# Expose port 80 for the web server
EXPOSE 80

# Nginx starts automatically, so no CMD is strictly needed, 
# but it's good practice to keep it explicit
CMD ["nginx", "-g", "daemon off;"]