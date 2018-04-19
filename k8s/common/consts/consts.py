#* Copyright 2018 ARICENT HOLDINGS LUXEMBOURG SARL and Cable Television
# Laboratories, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script is responsible for deploying Aricent_Iaas environments and
# Kubernetes Services

"""
Constants.py
"""
import os
from pathlib import Path
p = str(Path(__file__).parents[2])

CWD= p + "/"
print "CWD_IAAS path is exported implicitly"
print CWD
ANSIBLE_PATH=CWD+"ansible_p/"
DEPLOYMENT_TYPE="deployement_type"
PROJECT_NAME="Project_name"
PROJECT_PATH="PROJECT_PATH"
GIT_BRANCH="Git_branch"
SERVICE_SUBNET="service_subnet"
POD_SUBNET="pod_subnet"
NETWORKING_PLUGIN="networking_plugin"
HOST_NAME="hostname"
PROXIES = "proxies"
HTTP_PROXY = "http_proxy"
HTTPS_PROXY = "https_proxy"
FTP_PROXY = "ftp_proxy"
NO_PROXY = "no_proxy"
HOSTS = "node_configuration"
CEPH_VOLUME = "Ceph_Volume"
PERSISTENT_VOLUME = "Persistent_Volumes"

HOST = "host"
CEPH_CLAIMS = "Ceph_claims"
NODE_TYPE = "node_type"
STORAGE_TYPE = "second_storage"
IP = "ip"
TYPE = "type"
SERVICE_PASSWORD = "service_password"
SERVICE_HOST = "service_host"
HOSTNAME = "hostname"
NAME="name"
USER="user"
PASSWORD="password"
ANSIBLE_HOSTS_FILE="/etc/ansible/hosts"
HOSTS_FILE="/etc/hosts"
ANSIBLE_CONF="/etc/ansible/ansible.cfg"
PROXY_DATA_FILE=ANSIBLE_PATH+"ansible_utils/proxy_data.yaml"
VARIABLE_FILE=ANSIBLE_PATH+"ansible_utils/variable.yaml"
PROXY_PATH=CWD+"ansible_p/ansible_utils/proxy_data.yaml"
COUNT="count"
KUBERNETES="kubernetes"
BASIC_AUTHENTICATION="basic_authentication"
ETCD_CHANGES="etcd_changes"
USER_PASSWORD="user_password"
USER_ID="user_id"
USER_NAME="user_name"
DOCKER_REPO="Docker_Repo"
HOST_VOL="Host_Volume"
#CEPH_VOL="Ceph_Volume"
PORT="port"
STORAGE="storage"
CEPH_STORAGE="storage"
CLAIM_NAME="Claim_name"
CEPH_CLAIM_NAME="claim_name"
CLAIM_PARAMETERS="claim_parameteres"
CEPH_NODE_IP="ceph_node_ip"
#KARGO_PATH="KARGO_PATH"
KUBESPRAY_PATH="KUBESPRAY_PATH"
ENABLE_ISTIO="enable_istio"
ENABLE_AMBASSADOR="enable_ambassador"
AMBASSADOR_RBAC="ambassador_rbac"
LABEL_VALUE="label_value"
LABEL_KEY="label_key"
""" Folder Paths *****************"""
K8_SOURCE_PATH=CWD+"packages/source/"
INVENTORY_SOURCE_FOLDER=K8_SOURCE_PATH+"inventory/"
APT_ARCHIVES_PATH="/var/cache/apt/archives/"
MULTUS_CNI="multus_cni"
ADDITIONAL_NW_PLUGINS="additionalNetworkPlugins"
FLANNEL="flannel"
WEAVE="weave"
CALICO="calico"
CONTIV="contiv"
SRIOV_CNI="sriov_cni"
SRIOV_INTF="sriov_intf"
SRIOV_MAC="sriov_mac"
SRIOV_ST_RNG="sriov_st_rng"
SRIOV_EN_RNG="sriov_en_rng"
SRIOV_SUBNET="sriov_subnet"
SRIOV_GETWAY="sriov_gtwy"
NO_OF_INTF_IN_FLANNEL="noOfInteracesInFlannel"
FLANNEL_NETWORK="networkCreationInFlannel"
INTERFACE="interface"
NETWORK="network"
SUBNET_LEN="subnetLen"
SUBNET_MIN="subnetMin"
SUBNET_MAX="subnetMax"
VNI="vni"
MACVLAN="MACVLAN"
NO_OF_INTERFACES_IN_MACVLAN="noOfInteracesInMacvlan"
MACVLAN_INTERFACES="macvlan_interface"
PARENT_INTERFACE="parent interface"
VLAN_ID="vlanid"
HOSTNAME="hostname"
IP="ip"
NETWORK_CREATION_IN_MACVLAN="Networks"
MACVLAN_NETWORKS="macvlan_networks"
HOSTNAME="hostname"
MASTER_PLUGIN="masterplugin"
NETWORK_NAME="network name"
MASTER="master"
SUBNET="subnet"
RANGE_START="rangeStart"
RANGE_END="rangeEnd"
ROUTES_DST="routes_dst"
GATEWAY="gateway"
METRICS_SERVER="enable_metrics_server"#added  by yashwant

K8_YAML=ANSIBLE_PATH+"commission/kubernetes/playbooks/deploy_mode/k8/"
K8_INVENTORY=CWD+"kargo_folder/kargo/inventory/"
K8_CLEAN_UP=K8_YAML+"k8_clean_up.yaml"
K8_REMOVE_FOLDER=K8_YAML+"k8_remove_project_folder.yaml"
K8_LAUNCHER_PROXY=K8_YAML+"k8_launcher_proxy.yaml"
K8_REMOVE_NODE_K8=K8_YAML+"k8_remove_nodes.yaml"
K8_DELETE_NODE=K8_YAML+"k8_delete_node.yaml"
K8_CLEAN_UP_NODES=K8_YAML+"k8_dynamic_clean.yaml"
K8_CLEAN_NODES=K8_YAML+"k8_dynamic_clean_node.yaml"
K8_DEPLOY_NODES=K8_YAML+"k8_dynamic_deploy.yaml"
K8_SET_PACKAGES=K8_YAML+"setup_k8.yaml"
K8_NODE_LABELING=K8_YAML+"k8_node_label.yaml"
K8_CONF_DOCKER_REPO=K8_YAML+"private_docker.yaml"
K8_DYNAMIC_DOCKER_CONF=K8_YAML+"dynamic_docker_conf.yaml"
K8_PRIVATE_DOCKER=K8_YAML+"create_private_docker.yaml"
KUBERNETES_SET_LAUNCHER=K8_YAML+"launcher_setup.yaml"
KUBERNETES_CREATE_INVENTORY=K8_YAML+"inventory_file.yaml"
KUBERNETES_ADD_NODE_INVENTORY=K8_YAML+"add_node_inventory_file.yaml"
KUBERNETES_NEW_INVENTORY=K8_YAML+"new_inventory_file.yaml"
KUBERNETES_NODE_INVENTORY=K8_YAML+"node_inventory_file.yaml"
KUBERNETES_WEAVE_SCOPE=K8_YAML+"k8_weave_scope.yaml"
KUBERNETES_PERSISTENT_VOL=K8_YAML+"persistent_volume.yaml"
KUBERNETES_AUTHENTICATION=K8_YAML+"Authentication.yaml"
ETCD_CHANGES=K8_YAML+"etcd_changes.yaml"
KUBERNETES_USER_LIST=K8_YAML+"user_list.yaml"
KUBERNETES_CEPH_VOL=K8_YAML+"ceph_volume_final.yaml"
KUBERNETES_CEPH_STORAGE=K8_YAML+"ceph_volume_storage_type_final.yaml"
KUBERNETES_CEPH_VOL2=K8_YAML+"ceph_volume2_final.yaml"
KUBERNETES_CEPH_VOL_FIRST=K8_YAML+"ceph_volume_final2.yaml"
KUBERNETES_CEPH_DELETE_SECRET=K8_YAML+"ceph_delete_secret.yaml"
UNINSTALL_ISTIO=K8_YAML+"uninstall_istio.yaml"
UNINSTALL_AMBASSADOR=K8_YAML+"uninstall_ambassador.yaml"
SETUP_ISTIO=K8_YAML+"setup_istio.yaml"
CEPH_DEPLOY=K8_YAML+"ceph_deploy.yaml"
CEPH_MDS=K8_YAML+"ceph_mds.yaml"
CEPH_DEPLOY_ADMIN=K8_YAML+"ceph_deploy_admin.yaml"
CEPH_MON=K8_YAML+"ceph_mon.yaml"
SETUP_AMBASSADOR=K8_YAML+"setup_ambassador.yaml"
K8_COPY_KEY=K8_YAML+"copy_key_gen.yaml"
K8_PUSH_KEY=K8_YAML+"push_key_gen.yaml"
HTTP_PROXY_SRC=K8_SOURCE_PATH+"http-proxy_bak.conf"
INVENTORY_SRC=K8_SOURCE_PATH+"inventory"
SSH_PATH="/root/.ssh"
K8_CREATE_CRD_NETWORK=K8_YAML+"crd_network_k8.yaml"
K8_MULTUS_SET_MASTER=K8_YAML+"multus_master_k8.yaml"
K8_MULTUS_SCP_MULTUS_CNI=K8_YAML+"multus_scp_k8.yaml"
K8_MULTUS_SET_NODE=K8_YAML+"multus_node_k8.yaml"
K8_MULTUS_SCP_MULTUS_CNI_DYNAMIC_NODE=K8_YAML+"multus_scp_dynamic_node_k8.yaml"
K8_MULTUS_SET_DYNAMIC_NODE=K8_YAML+"multus_dynamic_node_k8.yaml"
K8_CONF_FLANNEL_INTERFACE_AT_MASTER=K8_YAML+"flannel_intf_master.yaml"
K8_CONF_FLANNEL_INTERFACE_AT_NODE=K8_YAML+"flannel_intf_node.yaml"
K8_CONF_FLANNEL_NETWORK_CREATION=K8_YAML+"flannel_network_creation.yaml"
K8_CONF_FLANNEL_INTERFACE_AT_MASTER_FOR_DYNAMIC_NODE=K8_YAML+"flannel_intf_master_dynamic_node.yaml"
K8_CONF_FLANNEL_INTERFACE_AT_DYNAMIC_NODE=K8_YAML+"flannel_intf_dynamic_node.yaml"
K8_DELETE_FLANNEL_INTERFACE=K8_YAML+"flannel_interface_deletion.yaml"
K8_CONF_FLANNEL_DAEMON_AT_MASTER=K8_YAML+"flannel_daemon_at_master.yaml"
K8_CONF_FLANNEL_INTF_CREATION_AT_MASTER=K8_YAML+"flannel_interface_creation.yaml"
K8_CONF_WEAVE_NETWORK_CREATION=K8_YAML+"weave_network_creation.yaml"
K8_CONF_FILES_DELETION_AFTER_MULTUS=K8_YAML+"weave_conf_deletion.yaml"
K8_SRIOV_CNI_BUILD=K8_YAML+"k8_sriov_build_cni.yaml"
K8_SRIOV_DPDK_CNI=K8_YAML+"k8_sriov_dpdk_cni.yaml"
K8_SRIOV_ENABLE=K8_YAML+"k8_sriov_enable.yaml"
K8_SRIOV_CNI_BIN_INST=K8_YAML+"k8_sriov_cni_bin_inst.yaml"
K8_SRIOV_DPDK_CNI_BIN_INST=K8_YAML+"k8_sriov_dpdk_cni_bin_inst.yaml"
K8_SRIOV_DPDK_DRIVER_LOAD=K8_YAML+"k8_sriov_dpdk_kernel_load.yaml"
K8_SRIOV_CR_NW=K8_YAML+"sriov_network_creation.yaml"
K8_SRIOV_DPDK_CR_NW=K8_YAML+"sriov_dpdk_network_creation.yaml"
K8_SRIOV_DHCP_CR_NW=K8_YAML+"sriov_dhcp_network_creation.yaml"
K8_SRIOV_CONF=K8_YAML+"sriov_conf.yaml"
K8_SRIOV_CONFIG_SCRIPT=K8_YAML+"sriov_configuration.sh"
K8_VLAN_INTERFACE_PATH=K8_YAML+"vlan_tag_interface_creation.yaml"
K8_VLAN_INTERFACE_REMOVAL_PATH=K8_YAML+"vlan_tag_interface_removal.yaml"
K8_MACVLAN_MASTER_NETWORK_PATH=K8_YAML+"macvlan_master_network_creation.yaml"
K8_MACVLAN_NETWORK_PATH=K8_YAML+"macvlan_network_creation.yaml"
K8_MACVLAN_MASTER_NETWORK_DHCP_PATH=K8_YAML+"macvlan_master_network_dhcp_creation.yaml"
K8_MACVLAN_NETWORK_DHCP_PATH=K8_YAML+"macvlan_network_dhcp_creation.yaml"
K8_MACVLAN_NETWORK_REMOVAL_PATH=K8_YAML+"macvlan_network_removal.yaml"
K8_DHCP_PATH=K8_YAML+"dhcp_daemon.yaml"
K8_DHCP_REMOVAL_PATH=K8_YAML+"dhcp_daemon_removal.yaml"
K8_METRRICS_SERVER=K8_YAML+"metrics_server_install1.yaml"#added by yashwant for metrics server
K8_METRRICS_SERVER_CLEAN=K8_YAML+"metrics_server_clean.yaml"#added by yashwant for metrics server clean
K8_CONF_FILES_DELETION_DYNAMIC_CODE=K8_YAML+"k8_delete_conf_files_dynamic_node.yaml"
K8_CREATE_DEFAULT_NETWORK=K8_YAML+"k8_create_default_network.yaml"
K8_CREATE_INVENTORY_FILE=K8_YAML+"k8_create_inventory_file.yaml"
NETWORKS="Networks"
DEFAULT_NETWORK="Default_Network"
NETWORKING_PLUGIN="networking_plugin"
SERVICE_SUBNET="service_subnet"
FLANNEL_NETWORK="Flannel"
WEAVE_NETWORK="Weave"
