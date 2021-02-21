# helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

# check helm
helm status -n spark-operator my-spark

# sparkctl
sparkctl create spark-pi.yaml
sparkctl status spark-pi
sparkctl event spark-pi
sparkctl log spark-pi
