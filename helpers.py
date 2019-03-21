import wmi

print("<Properties>")
for i in wmi.WMI().Win32_BIOS.properties.keys():
	print(i)

print("\n\n")

print("<Methods>")
for i in wmi.WMI().Win32_BIOS.methods.keys():
	print(i)