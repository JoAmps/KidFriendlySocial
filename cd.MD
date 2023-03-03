minikube start --driver=docker --alsologtostderr  virtualbox
kubectl get ns -> show namespace
kubectl config set-context --current --namespace modelprediction --> set namespace
minikiube status --> status of the minikube
minikube ip --> check ip address running the kubernetes
minikube ssh --> connect to the docker service
kubectl cluster-info
kubectl get nodes --> list available nodes
kubectl get pods --namespace=name
kubectl run name --image=name of image in docker
kubectl describe pod name

whiles inside of the docker container:
    docker exec -it logname sh
    hostname

kubectl get pods -o wide --> display more info
kubectl delete pod name
alias k="kubectl"  --> creates an alias
kubectl create deployment name --image=name of image in docker
kubectl get deployment --> shows all deployments
kubectl scale deployment name --replicas = number   --> scale deployments
curl ipnumber -- inside the cluster --> shows details 
kubectl expose deployment name --port=port number --target-port=kube portnumber
kubectl get services --> list services
cluster Ip available only inside cluster, and cannot be accesed by outside world, it can only be accessed from inside a node
kubectl describe service nameofservice
kubectl delete deployment name
kubectl delete service name
minikube ssh, once inside, curl IP:portnumber
curl port number; echo --> get response inside minikube ssh
kubectl delete svc service name
kubectl expose deployment name --type=NodePort --port=port number --> create nodeport to access k8 pod from in browser
minkube service nameofservice --> open web browser that is exposed
kubectl expose deployment name --type=LoadBalancer --port=port number --> create load balancer
kubectl describe deploy nameofservice
kubectl set image deployment nameofdeployment nameofdeployment=nameofimageplustag --> creates updated image in cluster
after above command run --> kubectl rollout status deploy nameofdeployment --> replace existing pods with updated ones
minikube dashboard --> create kubernetes dashboard on browser
kubectl delete all --all --> delete all resources
imperative approach --> type each command separately, declarative approach --> put neccesary instructions into yaml file
kubectl apply -f nameoffile.yaml --> to apply to the yaml created file
to delete the contents that declarative files produced --> kubectl delete -f name.yaml -f name.yaml etc
kubectl exec nameofpod -- nslookup nameofservice

stage('Clone repository') {
            steps {
                git 'https://github.com/JoAmps/AI-Enhancing-the-Language-of-Tweets-for-Young-Audiences.git'
            }
        }


src/
├── mains.py
    └── authenticaion_service
        └── auth_routes.py
