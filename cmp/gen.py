"""Python script to generate keybindings to add to ext
"""
import json

with open("linux_1_58_2.json") as linuxF:
	linux = json.loads(linuxF.read())
with open("windows_1_58_2.json") as windowsF:
	windows = json.loads(windowsF.read().replace("win", "meta"))
with open("mac_1_40.json") as macF:
	mac = json.loads(macF.read().replace("cmd", "meta"))


# find largest...
def argmax(seq):
	return max(range(len(seq)), key=seq.__getitem__)


# separate reference (largest) and rest
oskeys = [("linux", linux), ("windows", windows), ("mac", mac)]
idx = argmax([len(linux), len(windows), len(mac)])
ref = oskeys[idx]
oskeys.pop(idx)
print(ref[0])

# remove if present in all: exact match
for keybind in ref[1]:
	dup = 0  # duplicates is zero to start for one key
	dup_refs = []
	for keys in oskeys:
		for kb in keys[1]:
			if keybind == kb:
				dup += 1
				# print(keys[0])
				dup_refs.append(kb)

	if dup == 2:
		# print(keybind)
		ref[1].remove(keybind)
		for keys in oskeys:
			keys[1].remove(keybind)

oskeys.insert(idx, ref)
for index, keys in enumerate(oskeys):
	with open("out_" + ["linux.json", "win.json", "mac.json"][index], "w") as oF:
		oF.write(json.dumps(keys[1]).replace("meta", ["meta", "win", "cmd"][index]))
