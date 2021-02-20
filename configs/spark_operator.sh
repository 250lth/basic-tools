# add helm repo
helm repo add incubator https://charts.helm.sh/incubator --force-update

# install spark operator
helm install my-release incubator/sparkoperator --namespace spark-operator --create-namespace
