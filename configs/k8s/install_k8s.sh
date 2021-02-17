# ubuntu install kubeadm kubelet kubectl
curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -

sudo tee /etc/apt/sources.list.d/kubernetes.list <
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF

sudo apt update

sudo apt install -y kubelet kubeadm kubectl

# install k8s
sudo kubeadm init --pod-network-cidr=10.31.3.0/24

# cp k8s config
mkdir ~/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
