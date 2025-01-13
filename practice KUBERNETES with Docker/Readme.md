1. Image Management
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Build an image                         | docker build -t <image_name> .             | Builds an image from a Dockerfile.                  
List images                            | docker images                              | Displays all locally available images.              
Remove an image                        | docker rmi <image_name_or_id>              | Removes a specific image.                           
Tag an image                           | docker tag <image> <new_name:tag>          | Tags an image with a new name and tag.              
Pull an image from Docker Hub          | docker pull <image_name>                   | Pulls an image from the registry.                   
Push an image to Docker Hub            | docker push <image_name>                   | Pushes a local image to the registry.               
Inspect image details                  | docker inspect <image_name>                | Shows detailed information about the image.         

2. Container Management
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Run a container                        | docker run <image_name>                    | Runs a container from an image.                     
Run in detached mode                   | docker run -d <image_name>                 | Runs a container in the background.                 
Run with port mapping                  | docker run -p <host_port>:<container_port> <image_name> | Maps a container port to the host.         
Run with volume mapping                | docker run -v <host_path>:<container_path> <image_name> | Maps a volume between host and container.
Run interactively                      | docker run -it <image_name>                | Runs a container in interactive mode (terminal).    
List running containers                | docker ps                                  | Displays all running containers.                    
List all containers                    | docker ps -a                               | Displays all containers, including stopped ones.    
Stop a container                       | docker stop <container_id_or_name>         | Stops a running container.                          
Start a stopped container              | docker start <container_id_or_name>        | Starts a stopped container.                         
Remove a container                     | docker rm <container_id_or_name>           | Removes a container.                                 
Attach to a running container          | docker attach <container_id_or_name>       | Attach to a container's terminal.                   
Logs of a container                    | docker logs <container_id_or_name>         | Displays the logs of a container.                   
Inspect container details              | docker inspect <container_id_or_name>      | Shows detailed information about a container.       
Execute a command in a container       | docker exec -it <container_id_or_name> <command> | Runs a command inside a running container.

3. Volume Management
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Create a volume                        | docker volume create <volume_name>         | Creates a named volume.                             
List all volumes                       | docker volume ls                           | Lists all Docker volumes.                           
Remove a volume                        | docker volume rm <volume_name>             | Removes a specific volume.                          
Inspect volume details                 | docker volume inspect <volume_name>        | Shows detailed information about a volume.          

4. Network Management
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Create a network                       | docker network create <network_name>       | Creates a Docker network.                           
List all networks                      | docker network ls                          | Lists all Docker networks.                          
Remove a network                       | docker network rm <network_name>           | Removes a specific network.                         
Connect a container to a network       | docker network connect <network_name> <container_id_or_name> | Connects a container to a network.
Disconnect a container from a network  | docker network disconnect <network_name> <container_id_or_name> | Disconnects a container from a network.

5. Docker Compose
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Start services defined in docker-compose.yml | docker-compose up                    | Starts all services.                                 
Start services in detached mode        | docker-compose up -d                      | Starts services in the background.                  
Stop running services                  | docker-compose down                       | Stops and removes all services and containers.       
View logs                              | docker-compose logs                       | Displays logs from all services.                    
Execute a command in a service         | docker-compose exec <service_name> <command> | Runs a command inside a service container.     
Scale a service                        | docker-compose scale <service_name>=<count> | Scales a specific service.                          

6. Docker System Commands
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Show Docker system information         | docker info                                | Displays system-wide information about Docker.       
Clean up unused resources              | docker system prune                        | Removes unused images, containers, volumes, and networks.
Check Docker version                   | docker version                             | Displays the installed Docker version.              

7. Miscellaneous
Task                                   | Command                                     | Description                                          
------------------------------------------------------------------------------------------------
Save an image as a tar file            | docker save -o <filename>.tar <image_name> | Exports a Docker image to a tar file.               
Load an image from a tar file          | docker load -i <filename>.tar              | Imports a Docker image from a tar file.             
View container resource usage          | docker stats                               | Displays live resource usage of containers.         
Check container top processes          | docker top <container_id_or_name>          | Displays processes running in a container.
"""