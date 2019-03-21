import wmi

print("<Properties>")
for i in wmi.WMI().Win32_Process.properties.keys():
	print(i)

print("\n\n")

print("<Methods>")
for i in wmi.WMI().Win32_Process.methods.keys():
	print(i)