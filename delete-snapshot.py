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

# Buscar el snapshot y eliminarlo
snapshots = vm.snapshot.rootSnapshotList
for snapshot in snapshots:
    if snapshot.name == snapshot_name:
        snapshot.RemoveSnapshot_Task(removeChildren=False)
        print("El snapshot {} se ha eliminado correctamente.".format(snapshot_name))
        break

# Desconectar del servidor vCenter
Disconnect(si)
