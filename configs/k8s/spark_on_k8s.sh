kubectl create serviceaccount spark

kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default

# --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark
