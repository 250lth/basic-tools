# Install the Tigera Calico operator and custom resource definitions.
kubectl create -f https://docs.projectcalico.org/manifests/tigera-operator.yaml

# Install Calico by creating the necessary custom resource.
kubectl create -f https://docs.projectcalico.org/manifests/custom-resources.yaml

# Confirm that all of the pods are running with the following command
watch kubectl get pods -n calico-system # Wait until each pod has the STATUS of Running.

# Remove the taints on the master so that you can schedule pods on it.
kubectl taint nodes --all node-role.kubernetes.io/master-

# Confirm that you now have a node in your cluster with the following command.
kubectl get nodes -o wide
