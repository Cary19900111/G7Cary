import psutil

def cpu_info():
    '''
    user:用户进程花费的时间（seconds）
    idle：闲置时间
    system：内核模式进程花费的时间
    nice(UNIX)：用户模式执行Niced优先级进程花费的时间
    iowait(Linux):等待I/O完成的时间
    irq(Linux, FreeBSD)：处理硬件中断的时间
    softirq(Linux)：处理软件中断的时间
    steal(Linux >= 2.6.11)：虚拟化环境中运行的其他操作系统花费的时间
    guest(Linux >= 2.6.24)：在linux内核的控制下为客户端操作系统运行虚拟CPU所花费的时间
    guest_nice(Linux >= 3.2.0)：虚拟机运行niced所花费的时间
    '''
    cpu_tuple = psutil.cpu_times()
    print(cpu_tuple)
    print(cpu_tuple.system)

def memory_info():
    '''
    total:总物理内存(bit)
    available:可用的内存
    used:使用的内存
    free：完全没有使用的内存
    active：当前正在使用的内存
    inactive：标记为未使用的内存
    buffers：缓存文件系统元数据使用的内存
    cached:缓存各种文件的内存
    shared:可以被多个进程同时访问的内存
    slab:内核数据结构缓存的内存
    '''
    mem_tuple = psutil.virtual_memory()
    print(mem_tuple)
    
def swap_info():
    '''
    total：以字节为单位的总交换内存
    used：以字节为单位使用交换内存
    free：以字节为单位的可用交换内存
    percent：使用百分比
    sin：系统从磁盘交换的字节数
    sout：系统从磁盘换出的字节数
    '''
    swap_tuple = psutil.swap_memory()  #获取swap内存信息
    print(swap_tuple)

def disk_info():
    '''
    device：磁盘路径
    fstype：文件系统类型
    opts:选项
    '''
    disk_list = psutil.disk_partitions(all=False)
    print(len(disk_list))

def disusage_info():
    '''
    total:
    used:
    free:
    '''
    disusage_tuple = psutil.disk_usage("/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app/Contents/MacOS/Microsoft AU Daemon.app")
    print(disusage_tuple)

def disk_io_info():
    '''
    read_count：读取次数
    write_count：写入次数
    read_bytes：读取的字节数
    write_bytes：写入的字节数
    read_time：从磁盘读取的时间（以毫秒为单位）
    write_time：写入磁盘的时间（毫秒为单位）
    busy_time：花费在实际I/O上的时间
    read_merged_count：合并读取的数量
    write_merged_count：合并写入次数
    '''
    diskio_tuple = psutil.disk_io_counters(perdisk=False)
    print(diskio_tuple)

def net_info():
    '''
    bytes_sent：发送的字节数
    bytes_recv：收到的字节数
    packets_sent：发送的数据包数量
    packets_recv：接收的数据包数量
    errin：接收时的错误总数
    errout：发送时的错误总数
    dropin：丢弃的传入数据包总数
    dripout：丢弃的传出数据包总数（在OSX和BSD上始终为0
    '''
    net_tuple = psutil.net_io_counters()
    print(net_tuple)

def socket_connection_info():
    '''
    socket链接信息及相关使用进程
    '''
    socket_info = psutil.net_connections(kind='udp4')
    print(socket_info)

def system_if_dict():
    '''
    每个网络接口的关联地址
    isup是否启动
    duplex双工模式
    speed速率
    mtu最大传输单位(字节)
    '''
    if_dict = psutil.net_if_addrs()
    print(if_dict['lo0'][0])
    if_stats = psutil.net_if_stats()
    print(if_stats)

def system_start_time():
    import datetime
    time = datetime.datetime.fromtimestamp(psutil.boot_time())
    print(time)

def pid_info():
    '''psutil.process_iter(attrs=None,ad_value=None)过滤
     psutil.Popen开进程
     #消耗超过5M内存的进程：
     from pprint import pprint as pp
      pp([(p.pid,p.info['name'],p.info['memory_info'].rss) for p in psutil.pro
    ...: cess_iter(attrs=['name','memory_info']) if p.info['memory_info'].rss > 5
    ...:  * 1024 * 1024])
     '''
    pid_info = psutil.pids()
    # print(psutilpid_info)
    p = psutil.Process(1369)
    print(type(p))
    print(p.status())

def sys_user():
    user_info = psutil.users()
    print(user_info)
if __name__=="__main__":
    sys_user()