from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# Establecer conexión con el servidor vCenter
si = None
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE
si = SmartConnect(host='<vCenter_Hostname_or_IP>', user='<vCenter_username>', pwd='<vCenter_password>', sslContext=context)

# Especificar el nombre de la máquina virtual y el nombre del snapshot
vm_name = "<Nombre_de_la_maquina_virtual>"
snapshot_name = "<Nombre_del_snapshot>"

# Obtener la instancia del objeto vm
content = si.RetrieveContent()
vm = content.searchIndex.FindByFullName(None, vm_name)

# Crear el objeto snapshot
snapshot = vm.CreateSnapshot(snapshot_name, memory=False, quiesce=False)

# Desconectar del servidor vCenter
Disconnect(si)