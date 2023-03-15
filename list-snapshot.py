from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# Establecer conexión con el servidor vCenter
si = None
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE
si = SmartConnect(host='<vCenter_Hostname_or_IP>', user='<vCenter_username>', pwd='<vCenter_password>', sslContext=context)

# Obtener el objeto de servicio de búsqueda
content = si.RetrieveContent()
searcher = content.searchIndex

# Recuperar la lista de todas las máquinas virtuales
vm_list = searcher.FindAllByType("VirtualMachine")

# Recorrer la lista de todas las máquinas virtuales y listar sus snapshots
for vm in vm_list:
    print("Máquina virtual: {}".format(vm.name))
    snapshots = vm.snapshot.rootSnapshotList
    if snapshots:
        for snapshot in snapshots:
            print("  - Snapshot name: {}".format(snapshot.name))
            print("    Snapshot description: {}".format(snapshot.description))
            print("    Snapshot created at: {}\n".format(snapshot.createTime))
    else:
        print("No hay snapshots en esta máquina virtual.\n")

# Desconectar del servidor vCenter
Disconnect(si)
